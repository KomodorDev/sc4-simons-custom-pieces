---
title: "Testing: DD RHW-4 Level 1 (7.5 m) and Level 2 (15 m) over GHSR Ground (1 m) \u2014 Mixed Crossing \u2014 Both Diagonal 90\u00b0 \u2014 Alignment B"
summary: "Inspect this piece\u2019s exact checks, resource evidence, and explicit human observations."
audience: "contributors"
document_type: "reference"
---

# Testing: DD RHW-4 Level 1 (7.5 m) and Level 2 (15 m) over GHSR Ground (1 m) — Mixed Crossing — Both Diagonal 90° — Alignment B

<!-- PIECE TESTING LAYOUT: 1 -->

[Piece overview ↗ (README)](README.md) · [1. Test scope](#1-test-scope) · [2. Test setup](#2-test-setup) · [3. Software checks](#3-software-checks) · [4. Game checks](#4-game-checks) · [5. Results and known issues](#5-results-and-known-issues) · [6. Design history](#6-design-history)

## 1. Test scope

This scope is Alignment B of the two-tile diagonal DD RHW-4 over GHSR crossing. It owns two horizontally adjacent core tiles at 0°, with four native approaches in a 2 × 3 area. The railway carries two directions at 1 m; the lower deck carries two car lanes at 7.5 m, and the upper deck carries the opposing two lanes at 15 m. Check all six directed journeys, twelve complete boundary members, and thirty excluded entrance/exit transfers.

Check the next adjacent railway position while keeping the same highway line and deck travel directions. [Alignment A](../ddrhw-l1-and-l2-over-ghsr-ground-mixed-crossing-diagonal-90deg/TESTING.md) and B must be checked separately in all four proper rotations. Camera rotation is another operation. Repeated states do not establish another spatial alignment, and a Route Query line does not establish actual moving cars or trains.

<!-- BEGIN CONNECTIONS -->

### Connections and journeys

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.jsonc) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `lower-lane-01-in` | road / 1 / primary | in | [-3.2, -8.0, 7.5]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-3ecbd7f665c425929ca6` |
| `upper-lane-01-out` | road / 1 / primary | out | [-3.2, -8.0, 15.0]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-55ad67244a3a7bbd6c4b` |
| `lower-lane-02-in` | road / 1 / primary | in | [3.2, -8.0, 7.5]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-aad60a85e4675eaba5de` |
| `upper-lane-02-out` | road / 1 / primary | out | [3.2, -8.0, 15.0]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-50bfaaffb0d43ee83a9b` |
| `lower-lane-01-out` | road / 1 / primary | out | [12.8, 8.0, 7.5]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-3ecbd7f665c425929ca6` |
| `upper-lane-01-in` | road / 1 / primary | in | [12.8, 8.0, 15.0]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-55ad67244a3a7bbd6c4b` |
| `lower-lane-02-out` | road / 1 / primary | out | [19.2, 8.0, 7.5]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-aad60a85e4675eaba5de` |
| `upper-lane-02-in` | road / 1 / primary | in | [19.2, 8.0, 15.0]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-50bfaaffb0d43ee83a9b` |
| `ghsr-track-01-in` | ghsr / 7 / primary | in | [-2.8, 8.0, 1.0]; [0.7139382485962432, -0.7002086668924692]; 0.0 | `path-interface-ea9aec3cf7f13a65eeea` |
| `ghsr-track-02-out` | ghsr / 7 / primary | out | [2.9, 8.0, 1.0]; [-0.7071067811865476, 0.7071067811865475]; 0.0 | `path-interface-6ed8ad7d9e460ea9e26e` |
| `ghsr-track-01-out` | ghsr / 7 / primary | out | [13.1, -8.0, 1.0]; [0.7071067811865476, -0.7071067811865475]; 0.0 | `path-interface-6ed8ad7d9e460ea9e26e` |
| `ghsr-track-02-in` | ghsr / 7 / primary | in | [18.8, -8.0, 1.0]; [-0.7139382485962432, 0.7002086668924692]; 0.0 | `path-interface-ea9aec3cf7f13a65eeea` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| road | `lower-lane-01-in` → `lower-lane-01-out` | primary |
| road | `lower-lane-02-in` → `lower-lane-02-out` | primary |
| road | `upper-lane-01-in` → `upper-lane-01-out` | primary |
| road | `upper-lane-02-in` → `upper-lane-02-out` | primary |
| ghsr | `ghsr-track-01-in` → `ghsr-track-01-out` | primary |
| ghsr | `ghsr-track-02-in` → `ghsr-track-02-out` | primary |

#### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| road / `lower-lane-01-in` | road / `upper-lane-01-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `lower-lane-01-in` | road / `upper-lane-02-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `lower-lane-01-in` | road / `lower-lane-02-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `lower-lane-01-in` | ghsr / `ghsr-track-02-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `lower-lane-01-in` | ghsr / `ghsr-track-01-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `lower-lane-02-in` | road / `upper-lane-01-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `lower-lane-02-in` | road / `upper-lane-02-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `lower-lane-02-in` | road / `lower-lane-01-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `lower-lane-02-in` | ghsr / `ghsr-track-02-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `lower-lane-02-in` | ghsr / `ghsr-track-01-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `upper-lane-01-in` | road / `upper-lane-02-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `upper-lane-01-in` | road / `lower-lane-01-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `upper-lane-01-in` | road / `lower-lane-02-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `upper-lane-01-in` | ghsr / `ghsr-track-02-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `upper-lane-01-in` | ghsr / `ghsr-track-01-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `upper-lane-02-in` | road / `upper-lane-01-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `upper-lane-02-in` | road / `lower-lane-01-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `upper-lane-02-in` | road / `lower-lane-02-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `upper-lane-02-in` | ghsr / `ghsr-track-02-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `upper-lane-02-in` | ghsr / `ghsr-track-01-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| ghsr / `ghsr-track-01-in` | road / `upper-lane-01-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| ghsr / `ghsr-track-01-in` | road / `upper-lane-02-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| ghsr / `ghsr-track-01-in` | road / `lower-lane-01-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| ghsr / `ghsr-track-01-in` | road / `lower-lane-02-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| ghsr / `ghsr-track-01-in` | ghsr / `ghsr-track-02-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| ghsr / `ghsr-track-02-in` | road / `upper-lane-01-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| ghsr / `ghsr-track-02-in` | road / `upper-lane-02-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| ghsr / `ghsr-track-02-in` | road / `lower-lane-01-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| ghsr / `ghsr-track-02-in` | road / `lower-lane-02-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| ghsr / `ghsr-track-02-in` | ghsr / `ghsr-track-01-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

## 2. Test setup

Use Windows SimCity 4 1.1.641 and the audited NAM 50 right-hand-traffic files. The original shadow-carrier candidate also used the native-lighting capture; the selected no-shadow source no longer requires it. Record Windows, Wine, or CrossOver as actually used. Read the [shared input and installation guide](../../../../docs/BUILD_AND_INSTALL.md), then prepare a flat disposable city with working native GHSR and DD control lines.

Use the [README table and exact menu/tool steps](README.md#23-place-and-extend-alignment-b). The final combined candidate contains both A and B under the original crossing button, plus the unchanged existing pieces. A B-only development build instead has its own Alignment B button. Installing a candidate requires a closed game. The current revision intentionally supplies no cast shadows and removes the shadow-only T21 attachments; a T21 is a network-tile record that places attached objects. Restart, and place B fresh so its native helper markers are created without relying on older saved shadow attachments being removed by reload alone. Existing-city cleanup remains a separate unverified check; A retains its identifiers and geometry.

## 3. Software checks

The [2026-11-01 compiled shadow-removal audit](../../evidence/ddrhw-shadow-removal-20261101.jsonc) covers both GHSR/DD alignments and all fifteen existing parallel components in a 37-type selection. It records 287 removed shadow resources, three adaptive T21 changes, unchanged remaining selected resource payloads, and twenty unaffected DATs preserved byte for byte. Traffic PATHs, visible models, native helpers, adaptive sidewalk resources, and the allocation ledger are preserved. This is exact saved-resource evidence for its recorded candidate and manifest; it records no installation, fresh render, or game observation.

Run these commands from the repository root. The source build below is the actual saved Alignment B evidence build; a later delivery package must also pass its own verification.

```sh
python3 -B custom-pieces/scp.py verify --output custom-pieces/dist/ghsr-dd-alignment-b-source-01
python3 -B custom-pieces/scp.py connectors check --domain highway --piece ddrhw-l1-l2-over-ghsr-ground-crossing-diagonal-90deg-alignment-b --build dist/ghsr-dd-alignment-b-source-01
python3 -B custom-pieces/scp.py docs-check --piece ddrhw-l1-l2-over-ghsr-ground-crossing-diagonal-90deg-alignment-b
python3 -B tools/run_tests.py
```

The [authoring recipe](../../implementation/scp_highway/ghsr_crossing.py), [independent verifier](../../implementation/scp_highway/ghsr_crossing_verify.py), and [native approach adapter](../../implementation/scp_highway/ghsr_approaches.py) own this implementation. The [frozen original native contract](evidence/native-contract.jsonc) binds that earlier saved DAT/resources, independently inspected native model streams, rail transitions, helper rules, and historical shadow carriers. Preserve its exact earlier scope; its carrier results do not establish the current no-shadow revision. The [paired alignment audit](evidence/diagonal-alignment-coverage.jsonc) checks actual saved A and B traffic paths against a fixed directed highway, including both spatial positions and four rotations. It does not certify a diamond layout.

B retains native DD routes and visible native rail geometry. The original rail chord is asymmetric: each B exterior joining coordinate needs a 0.1 m correction to meet its actual unmodified native helper. Four-node rail paths use a 3 m exterior collar along that helper's travel heading, a short blend, and a 1 m exact-diagonal internal collar. Internal rail endpoints already meet and remain unchanged. The measured maximum sideways deviation from the original core chord is approximately 0.099835519095 m. Check this B-specific transition independently of A's different internal correction.

The PATH header explicitly retains authored elevations with UseElevation=1. The 5 m-wide, 5 m-high reviewed train envelope rises from the 1 m railway to a 6 m roof; the selected DD underside is at least 6.5 m, giving 0.5 m geometric clearance. This declared envelope is not a measured collision box for every custom train. The current revision removes both shadow-only T21 attachments and their carrier resources, while retaining their reserved source inventory. Check the saved no-shadow result independently, including the absence of carrier props, carrier models, mask textures, and fixed network-shadow mappings; keep visible models and native approaches intact. Native RUL2 remains unchanged; the existing narrow native-helper RUL1 solutions are shared by both alignments without adding conflicting rules.

## 4. Game checks

### 4.1 Test both adjacent railway positions

1. Build a working diagonal DD highway with the exact NAM starter named in the README. Keep its position and deck directions fixed for this comparison.
2. Prepare a northwest/southeast GHSR control line at an Alignment A position. Leave a gap for the fixed core and its native approaches. Select A, place it, and extend its native arms with RHW-2 and Monorail. Record placement, Route Query, and actual moving vehicles against A's cases.
3. Prepare a second crossing site on the same directed highway. Move the diagonal railway to the next adjacent parallel grid position by shifting its grid placement one ordinary city square east or north. Do not move it a complete two-axis diagonal step, which repeats the same alignment. Keep the highway unchanged.
4. Select the original SCP crossing button, press Tab for Alignment B, and read Alignment B in the placement query. Match its two horizontal core tiles and four approach tiles to the README table. Confirm that B fits the missing intermediate position without turning the highway directions around.
5. Test both build orders: place B on clear flat ground and drag outward from its four approaches; then prepare native approach arms first, leave the two core tiles empty, and place a fresh B into that gap. Record each result separately. Use RHW-2 for highway, and Monorail for GHSR.
6. Connect the arms to working traffic sources and destinations. Follow actual cars across the entire lower and upper decks, and actual trains through both railway directions. Record stops, disappearance, wrong heights, transfer, and seam gaps separately from Route Query.
7. Repeat A and B in 90°, 180°, and 270° placements with appropriately directed control highways. Test Tab and Shift+Tab between A and B, Home and End within each alignment, cancellation, and selecting the button again. Cycling must stay within A/B and must not enter any diamond assembly cycle.

### 4.2 Shadows and object lifetime

1. Inspect the ground railway and both decks at every zoom and all four city-camera views. The railway must remain beneath the lower deck, and both road directions must remain at their own heights.
2. Set shadows to Medium, inspect every zoom and all four city-camera views, and repeat with High. B intentionally supplies no cast shadows: look for any remaining deck-shaped shadow, detached triangle, or phantom neighbouring structure. Distinguish other objects’ shadows from this crossing, and record any Low-quality comparison separately; absence at Low alone does not establish removal at Medium or High.
3. Save the test city, quit the game completely, reload it, and repeat actual vehicle travel, heights, and shadow checks.
4. Demolish B in the disposable area. Inspect both former owned tiles and the four native approaches separately for leftover models or shadows. Redraw the native lines, place a fresh crossing, and repeat the connection check.

Record only explicit matching observations through [the shared testing procedure](../../../../docs/TESTING.md). A report about A, an Avenue crossing, or a preview cannot approve B's exact game cases.

## 5. Results and known issues

Alignment B is experimental. The current appearance policy is no cast shadows for both GHSR/DD alignments, following the user’s report about the adjoining draggable DD highway. That report does not independently establish every native resource’s behavior. Actual placement, native dragging, Tab selection, moving cars, moving trains, absence of unwanted shadows, demolition, and save/reload require matching human observations. All generated game cases start unverified; software checks cannot create manual passes.

Native ground track-bed faces extend approximately 0.989332 m below ground and 1.989332 m above it. Isolated model previews can expose below-ground sides because their grid does not hide geometry like game terrain. Inspect actual terrain occlusion and train appearance separately. The exact geometric train clearance is not a guarantee for every replacement train.

This repair applies only to the DD/GHSR crossing. The three Avenue diamonds retain their previous geometry and single-alignment limitation until separately authorized work.

<!-- BEGIN MANUAL SUMMARY -->

### Manual status

Generated from [the exact test cases](#test-checklist) and [authoritative observations](checks/manual-tests.json).

- [ ] Preview review: 0/3 applicable cases passed; 0 failed, 0 stale.
- [ ] In-game rendering: 0/4 applicable cases passed; 0 failed, 0 stale.
- [ ] Route Query: 0/24 applicable cases passed; 0 failed, 0 stale.
- [ ] Visible travel: 0/24 applicable cases passed; 0 failed, 0 stale.

These observations cover only the named services, directions, poses, rotations, and recorded platforms.

<!-- END MANUAL SUMMARY -->

<!-- BEGIN MANUAL CHECKS -->

### Test checklist

Generated from [the authoritative record](checks/manual-tests.json). Only explicit human observations create manual passes; software and preview checks remain separate. Expand a check/service group to see its rotation table, then expand the matching exact scope to copy a case ID and inspect its pose, reviewer, environment, and evidence. Grouping changes only this view; every declared case remains separate.

**States:** [x] passed; [ ] unverified, failed, or stale; N/A is an explicit inapplicable declaration. A dash means no case was declared in that column. Every pass covers only its recorded environment. T means a distinct construction-transposed state.

Four proper rotations are covered. No additional reflected state is established by this record; repeated construction aliases do not create new orientations.

Current totals: unverified: 189, passed: 0, failed: 0, stale: 0, not_applicable: 0.

#### Record an observation

Follow the [shared testing guide](../../../../docs/TESTING.md); copy [the unconfirmed example](checks/observation.example.json) to `checks/observation.json`. Case identifiers are in the expandable sections below. Do not edit generated checkboxes.

From the repository folder containing `custom-pieces`, run after filling `checks/observation.json` and explicitly confirming the exact observation:

```sh
python3 -m scp.content record --record custom-pieces/domains/highway/00_pieces/ddrhw-l1-l2-over-ghsr-ground-crossing-diagonal-90deg-alignment-b/checks/manual-tests.json --observation custom-pieces/domains/highway/00_pieces/ddrhw-l1-l2-over-ghsr-ground-crossing-diagonal-90deg-alignment-b/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-240be4715171a2175c4f">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-240be4715171a2175c4f"></a>

**General: unverified** — `software_resources-240be4715171a2175c4f`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-240be4715171a2175c4f">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-240be4715171a2175c4f"></a>

**General: unverified** — `software_connectivity-240be4715171a2175c4f`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 3 cases; unverified: 3</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:ddrhw-l1-l2-over-ghsr-ground-crossing-diagonal-90deg-alignment-b:canonical-southeast | <a href="#case-preview_review-d6abcd7b012b2ae96004">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-l1-l2-over-ghsr-ground-crossing-diagonal-90deg-alignment-b:canonical-top | <a href="#case-preview_review-89a492ae15085813a0a3">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-l1-l2-over-ghsr-ground-crossing-diagonal-90deg-alignment-b:connection-overview | <a href="#case-preview_review-3c9fb283b1e20dd90df3">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:ddrhw-l1-l2-over-ghsr-ground-crossing-diagonal-90deg-alignment-b:canonical-southeast</summary>

<a id="case-preview_review-d6abcd7b012b2ae96004"></a>

**General: unverified** — `preview_review-d6abcd7b012b2ae96004`.

Inspect this exact preview for tracks, walls, piers, seams, and shadows.

Scope: Image: image:ddrhw-l1-l2-over-ghsr-ground-crossing-diagonal-90deg-alignment-b:canonical-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-l1-l2-over-ghsr-ground-crossing-diagonal-90deg-alignment-b:canonical-top</summary>

<a id="case-preview_review-89a492ae15085813a0a3"></a>

**General: unverified** — `preview_review-89a492ae15085813a0a3`.

Inspect this exact preview for tracks, walls, piers, seams, and shadows.

Scope: Image: image:ddrhw-l1-l2-over-ghsr-ground-crossing-diagonal-90deg-alignment-b:canonical-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-l1-l2-over-ghsr-ground-crossing-diagonal-90deg-alignment-b:connection-overview</summary>

<a id="case-preview_review-3c9fb283b1e20dd90df3"></a>

**General: unverified** — `preview_review-3c9fb283b1e20dd90df3`.

Inspect this exact preview for tracks, walls, piers, seams, and shadows.

Scope: Image: image:ddrhw-l1-l2-over-ghsr-ground-crossing-diagonal-90deg-alignment-b:connection-overview.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-3107d4ec938f3c22bea2">[ ] unverified</a> | <a href="#case-in_game_render-312649283068da6ebb4a">[ ] unverified</a> | <a href="#case-in_game_render-42496ed5ec92e644b07b">[ ] unverified</a> | <a href="#case-in_game_render-314777fbdc2b947a63da">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-3107d4ec938f3c22bea2"></a>

**0° CCW: unverified** — `in_game_render-3107d4ec938f3c22bea2`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-312649283068da6ebb4a"></a>

**90° CCW: unverified** — `in_game_render-312649283068da6ebb4a`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-42496ed5ec92e644b07b"></a>

**180° CCW: unverified** — `in_game_render-42496ed5ec92e644b07b`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-314777fbdc2b947a63da"></a>

**270° CCW: unverified** — `in_game_render-314777fbdc2b947a63da`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-3107d4ec938f3c22bea2">[ ] unverified</a> | <a href="#case-in_game_placement-312649283068da6ebb4a">[ ] unverified</a> | <a href="#case-in_game_placement-42496ed5ec92e644b07b">[ ] unverified</a> | <a href="#case-in_game_placement-314777fbdc2b947a63da">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-3107d4ec938f3c22bea2"></a>

**0° CCW: unverified** — `in_game_placement-3107d4ec938f3c22bea2`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-312649283068da6ebb4a"></a>

**90° CCW: unverified** — `in_game_placement-312649283068da6ebb4a`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-42496ed5ec92e644b07b"></a>

**180° CCW: unverified** — `in_game_placement-42496ed5ec92e644b07b`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-314777fbdc2b947a63da"></a>

**270° CCW: unverified** — `in_game_placement-314777fbdc2b947a63da`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-3107d4ec938f3c22bea2">[ ] unverified</a> | <a href="#case-in_game_demolition-312649283068da6ebb4a">[ ] unverified</a> | <a href="#case-in_game_demolition-42496ed5ec92e644b07b">[ ] unverified</a> | <a href="#case-in_game_demolition-314777fbdc2b947a63da">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-3107d4ec938f3c22bea2"></a>

**0° CCW: unverified** — `in_game_demolition-3107d4ec938f3c22bea2`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-312649283068da6ebb4a"></a>

**90° CCW: unverified** — `in_game_demolition-312649283068da6ebb4a`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-42496ed5ec92e644b07b"></a>

**180° CCW: unverified** — `in_game_demolition-42496ed5ec92e644b07b`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-314777fbdc2b947a63da"></a>

**270° CCW: unverified** — `in_game_demolition-314777fbdc2b947a63da`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-3107d4ec938f3c22bea2">[ ] unverified</a> | <a href="#case-in_game_save_reload-312649283068da6ebb4a">[ ] unverified</a> | <a href="#case-in_game_save_reload-42496ed5ec92e644b07b">[ ] unverified</a> | <a href="#case-in_game_save_reload-314777fbdc2b947a63da">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-3107d4ec938f3c22bea2"></a>

**0° CCW: unverified** — `in_game_save_reload-3107d4ec938f3c22bea2`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-312649283068da6ebb4a"></a>

**90° CCW: unverified** — `in_game_save_reload-312649283068da6ebb4a`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-42496ed5ec92e644b07b"></a>

**180° CCW: unverified** — `in_game_save_reload-42496ed5ec92e644b07b`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-314777fbdc2b947a63da"></a>

**270° CCW: unverified** — `in_game_save_reload-314777fbdc2b947a63da`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — road — 16 cases; unverified: 16</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out | — | <a href="#case-in_game_route_query-b4711d8f8bda7b210e0d">[ ] unverified</a> | <a href="#case-in_game_route_query-2fb96859ae762910a5fd">[ ] unverified</a> | <a href="#case-in_game_route_query-56537cd8d3ee549ceccb">[ ] unverified</a> | <a href="#case-in_game_route_query-1e6a516092fc6079277a">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out | — | <a href="#case-in_game_route_query-590e1332b9c7c9fafeee">[ ] unverified</a> | <a href="#case-in_game_route_query-35456c0d68bab4995cfe">[ ] unverified</a> | <a href="#case-in_game_route_query-dfd9739de29e813054b8">[ ] unverified</a> | <a href="#case-in_game_route_query-f95d503267122cd97751">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out | — | <a href="#case-in_game_route_query-2fbd79de7cd740a75c92">[ ] unverified</a> | <a href="#case-in_game_route_query-5369ee733d2385cef919">[ ] unverified</a> | <a href="#case-in_game_route_query-db84130665fc304f6505">[ ] unverified</a> | <a href="#case-in_game_route_query-c01dcd19c3eec1baecd1">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out | — | <a href="#case-in_game_route_query-1993094849d021e36d7c">[ ] unverified</a> | <a href="#case-in_game_route_query-ae398b9ad7702201d997">[ ] unverified</a> | <a href="#case-in_game_route_query-2b1bde48e4016623dcd4">[ ] unverified</a> | <a href="#case-in_game_route_query-e13dea4ea8afd79fded1">[ ] unverified</a> |


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out</summary>

<a id="case-in_game_route_query-b4711d8f8bda7b210e0d"></a>

**0° CCW: unverified** — `in_game_route_query-b4711d8f8bda7b210e0d`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out.

No observation recorded.

<a id="case-in_game_route_query-2fb96859ae762910a5fd"></a>

**90° CCW: unverified** — `in_game_route_query-2fb96859ae762910a5fd`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out.

No observation recorded.

<a id="case-in_game_route_query-56537cd8d3ee549ceccb"></a>

**180° CCW: unverified** — `in_game_route_query-56537cd8d3ee549ceccb`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out.

No observation recorded.

<a id="case-in_game_route_query-1e6a516092fc6079277a"></a>

**270° CCW: unverified** — `in_game_route_query-1e6a516092fc6079277a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out</summary>

<a id="case-in_game_route_query-590e1332b9c7c9fafeee"></a>

**0° CCW: unverified** — `in_game_route_query-590e1332b9c7c9fafeee`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out.

No observation recorded.

<a id="case-in_game_route_query-35456c0d68bab4995cfe"></a>

**90° CCW: unverified** — `in_game_route_query-35456c0d68bab4995cfe`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out.

No observation recorded.

<a id="case-in_game_route_query-dfd9739de29e813054b8"></a>

**180° CCW: unverified** — `in_game_route_query-dfd9739de29e813054b8`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out.

No observation recorded.

<a id="case-in_game_route_query-f95d503267122cd97751"></a>

**270° CCW: unverified** — `in_game_route_query-f95d503267122cd97751`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out</summary>

<a id="case-in_game_route_query-2fbd79de7cd740a75c92"></a>

**0° CCW: unverified** — `in_game_route_query-2fbd79de7cd740a75c92`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out.

No observation recorded.

<a id="case-in_game_route_query-5369ee733d2385cef919"></a>

**90° CCW: unverified** — `in_game_route_query-5369ee733d2385cef919`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out.

No observation recorded.

<a id="case-in_game_route_query-db84130665fc304f6505"></a>

**180° CCW: unverified** — `in_game_route_query-db84130665fc304f6505`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out.

No observation recorded.

<a id="case-in_game_route_query-c01dcd19c3eec1baecd1"></a>

**270° CCW: unverified** — `in_game_route_query-c01dcd19c3eec1baecd1`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out</summary>

<a id="case-in_game_route_query-1993094849d021e36d7c"></a>

**0° CCW: unverified** — `in_game_route_query-1993094849d021e36d7c`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out.

No observation recorded.

<a id="case-in_game_route_query-ae398b9ad7702201d997"></a>

**90° CCW: unverified** — `in_game_route_query-ae398b9ad7702201d997`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out.

No observation recorded.

<a id="case-in_game_route_query-2b1bde48e4016623dcd4"></a>

**180° CCW: unverified** — `in_game_route_query-2b1bde48e4016623dcd4`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out.

No observation recorded.

<a id="case-in_game_route_query-e13dea4ea8afd79fded1"></a>

**270° CCW: unverified** — `in_game_route_query-e13dea4ea8afd79fded1`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — road — 16 cases; unverified: 16</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out | — | <a href="#case-in_game_visible_travel-b4711d8f8bda7b210e0d">[ ] unverified</a> | <a href="#case-in_game_visible_travel-2fb96859ae762910a5fd">[ ] unverified</a> | <a href="#case-in_game_visible_travel-56537cd8d3ee549ceccb">[ ] unverified</a> | <a href="#case-in_game_visible_travel-1e6a516092fc6079277a">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out | — | <a href="#case-in_game_visible_travel-590e1332b9c7c9fafeee">[ ] unverified</a> | <a href="#case-in_game_visible_travel-35456c0d68bab4995cfe">[ ] unverified</a> | <a href="#case-in_game_visible_travel-dfd9739de29e813054b8">[ ] unverified</a> | <a href="#case-in_game_visible_travel-f95d503267122cd97751">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out | — | <a href="#case-in_game_visible_travel-2fbd79de7cd740a75c92">[ ] unverified</a> | <a href="#case-in_game_visible_travel-5369ee733d2385cef919">[ ] unverified</a> | <a href="#case-in_game_visible_travel-db84130665fc304f6505">[ ] unverified</a> | <a href="#case-in_game_visible_travel-c01dcd19c3eec1baecd1">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out | — | <a href="#case-in_game_visible_travel-1993094849d021e36d7c">[ ] unverified</a> | <a href="#case-in_game_visible_travel-ae398b9ad7702201d997">[ ] unverified</a> | <a href="#case-in_game_visible_travel-2b1bde48e4016623dcd4">[ ] unverified</a> | <a href="#case-in_game_visible_travel-e13dea4ea8afd79fded1">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out</summary>

<a id="case-in_game_visible_travel-b4711d8f8bda7b210e0d"></a>

**0° CCW: unverified** — `in_game_visible_travel-b4711d8f8bda7b210e0d`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out.

No observation recorded.

<a id="case-in_game_visible_travel-2fb96859ae762910a5fd"></a>

**90° CCW: unverified** — `in_game_visible_travel-2fb96859ae762910a5fd`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out.

No observation recorded.

<a id="case-in_game_visible_travel-56537cd8d3ee549ceccb"></a>

**180° CCW: unverified** — `in_game_visible_travel-56537cd8d3ee549ceccb`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out.

No observation recorded.

<a id="case-in_game_visible_travel-1e6a516092fc6079277a"></a>

**270° CCW: unverified** — `in_game_visible_travel-1e6a516092fc6079277a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out</summary>

<a id="case-in_game_visible_travel-590e1332b9c7c9fafeee"></a>

**0° CCW: unverified** — `in_game_visible_travel-590e1332b9c7c9fafeee`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out.

No observation recorded.

<a id="case-in_game_visible_travel-35456c0d68bab4995cfe"></a>

**90° CCW: unverified** — `in_game_visible_travel-35456c0d68bab4995cfe`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out.

No observation recorded.

<a id="case-in_game_visible_travel-dfd9739de29e813054b8"></a>

**180° CCW: unverified** — `in_game_visible_travel-dfd9739de29e813054b8`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out.

No observation recorded.

<a id="case-in_game_visible_travel-f95d503267122cd97751"></a>

**270° CCW: unverified** — `in_game_visible_travel-f95d503267122cd97751`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out</summary>

<a id="case-in_game_visible_travel-2fbd79de7cd740a75c92"></a>

**0° CCW: unverified** — `in_game_visible_travel-2fbd79de7cd740a75c92`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out.

No observation recorded.

<a id="case-in_game_visible_travel-5369ee733d2385cef919"></a>

**90° CCW: unverified** — `in_game_visible_travel-5369ee733d2385cef919`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out.

No observation recorded.

<a id="case-in_game_visible_travel-db84130665fc304f6505"></a>

**180° CCW: unverified** — `in_game_visible_travel-db84130665fc304f6505`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out.

No observation recorded.

<a id="case-in_game_visible_travel-c01dcd19c3eec1baecd1"></a>

**270° CCW: unverified** — `in_game_visible_travel-c01dcd19c3eec1baecd1`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out</summary>

<a id="case-in_game_visible_travel-1993094849d021e36d7c"></a>

**0° CCW: unverified** — `in_game_visible_travel-1993094849d021e36d7c`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out.

No observation recorded.

<a id="case-in_game_visible_travel-ae398b9ad7702201d997"></a>

**90° CCW: unverified** — `in_game_visible_travel-ae398b9ad7702201d997`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out.

No observation recorded.

<a id="case-in_game_visible_travel-2b1bde48e4016623dcd4"></a>

**180° CCW: unverified** — `in_game_visible_travel-2b1bde48e4016623dcd4`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out.

No observation recorded.

<a id="case-in_game_visible_travel-e13dea4ea8afd79fded1"></a>

**270° CCW: unverified** — `in_game_visible_travel-e13dea4ea8afd79fded1`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — ghsr — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: ghsr; role: primary; journey: 7:ghsr-track-01-in>ghsr-track-01-out; entry: ghsr-track-01-in; exit: ghsr-track-01-out | — | <a href="#case-in_game_route_query-9d4c8d0b3bb1b8424074">[ ] unverified</a> | <a href="#case-in_game_route_query-100a766e19662d89c9ed">[ ] unverified</a> | <a href="#case-in_game_route_query-9608888f553baef36131">[ ] unverified</a> | <a href="#case-in_game_route_query-584510f3ec0c3d9372a1">[ ] unverified</a> |
| **Route Query**<br>Service: ghsr; role: primary; journey: 7:ghsr-track-02-in>ghsr-track-02-out; entry: ghsr-track-02-in; exit: ghsr-track-02-out | — | <a href="#case-in_game_route_query-6e27109cabaee54de1c1">[ ] unverified</a> | <a href="#case-in_game_route_query-133a618e32bf8b2769ff">[ ] unverified</a> | <a href="#case-in_game_route_query-338ce3d9411d845b5a76">[ ] unverified</a> | <a href="#case-in_game_route_query-c906c6082c096ac343e4">[ ] unverified</a> |


<details>
<summary>Route Query — Service: ghsr; role: primary; journey: 7:ghsr-track-01-in>ghsr-track-01-out; entry: ghsr-track-01-in; exit: ghsr-track-01-out</summary>

<a id="case-in_game_route_query-9d4c8d0b3bb1b8424074"></a>

**0° CCW: unverified** — `in_game_route_query-9d4c8d0b3bb1b8424074`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: ghsr; role: primary; journey: 7:ghsr-track-01-in>ghsr-track-01-out; entry: ghsr-track-01-in; exit: ghsr-track-01-out.

No observation recorded.

<a id="case-in_game_route_query-100a766e19662d89c9ed"></a>

**90° CCW: unverified** — `in_game_route_query-100a766e19662d89c9ed`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: ghsr; role: primary; journey: 7:ghsr-track-01-in>ghsr-track-01-out; entry: ghsr-track-01-in; exit: ghsr-track-01-out.

No observation recorded.

<a id="case-in_game_route_query-9608888f553baef36131"></a>

**180° CCW: unverified** — `in_game_route_query-9608888f553baef36131`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: ghsr; role: primary; journey: 7:ghsr-track-01-in>ghsr-track-01-out; entry: ghsr-track-01-in; exit: ghsr-track-01-out.

No observation recorded.

<a id="case-in_game_route_query-584510f3ec0c3d9372a1"></a>

**270° CCW: unverified** — `in_game_route_query-584510f3ec0c3d9372a1`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: ghsr; role: primary; journey: 7:ghsr-track-01-in>ghsr-track-01-out; entry: ghsr-track-01-in; exit: ghsr-track-01-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: ghsr; role: primary; journey: 7:ghsr-track-02-in>ghsr-track-02-out; entry: ghsr-track-02-in; exit: ghsr-track-02-out</summary>

<a id="case-in_game_route_query-6e27109cabaee54de1c1"></a>

**0° CCW: unverified** — `in_game_route_query-6e27109cabaee54de1c1`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: ghsr; role: primary; journey: 7:ghsr-track-02-in>ghsr-track-02-out; entry: ghsr-track-02-in; exit: ghsr-track-02-out.

No observation recorded.

<a id="case-in_game_route_query-133a618e32bf8b2769ff"></a>

**90° CCW: unverified** — `in_game_route_query-133a618e32bf8b2769ff`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: ghsr; role: primary; journey: 7:ghsr-track-02-in>ghsr-track-02-out; entry: ghsr-track-02-in; exit: ghsr-track-02-out.

No observation recorded.

<a id="case-in_game_route_query-338ce3d9411d845b5a76"></a>

**180° CCW: unverified** — `in_game_route_query-338ce3d9411d845b5a76`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: ghsr; role: primary; journey: 7:ghsr-track-02-in>ghsr-track-02-out; entry: ghsr-track-02-in; exit: ghsr-track-02-out.

No observation recorded.

<a id="case-in_game_route_query-c906c6082c096ac343e4"></a>

**270° CCW: unverified** — `in_game_route_query-c906c6082c096ac343e4`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: ghsr; role: primary; journey: 7:ghsr-track-02-in>ghsr-track-02-out; entry: ghsr-track-02-in; exit: ghsr-track-02-out.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — ghsr — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: ghsr; role: primary; journey: 7:ghsr-track-01-in>ghsr-track-01-out; entry: ghsr-track-01-in; exit: ghsr-track-01-out | — | <a href="#case-in_game_visible_travel-9d4c8d0b3bb1b8424074">[ ] unverified</a> | <a href="#case-in_game_visible_travel-100a766e19662d89c9ed">[ ] unverified</a> | <a href="#case-in_game_visible_travel-9608888f553baef36131">[ ] unverified</a> | <a href="#case-in_game_visible_travel-584510f3ec0c3d9372a1">[ ] unverified</a> |
| **Visible travel**<br>Service: ghsr; role: primary; journey: 7:ghsr-track-02-in>ghsr-track-02-out; entry: ghsr-track-02-in; exit: ghsr-track-02-out | — | <a href="#case-in_game_visible_travel-6e27109cabaee54de1c1">[ ] unverified</a> | <a href="#case-in_game_visible_travel-133a618e32bf8b2769ff">[ ] unverified</a> | <a href="#case-in_game_visible_travel-338ce3d9411d845b5a76">[ ] unverified</a> | <a href="#case-in_game_visible_travel-c906c6082c096ac343e4">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: ghsr; role: primary; journey: 7:ghsr-track-01-in>ghsr-track-01-out; entry: ghsr-track-01-in; exit: ghsr-track-01-out</summary>

<a id="case-in_game_visible_travel-9d4c8d0b3bb1b8424074"></a>

**0° CCW: unverified** — `in_game_visible_travel-9d4c8d0b3bb1b8424074`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: ghsr; role: primary; journey: 7:ghsr-track-01-in>ghsr-track-01-out; entry: ghsr-track-01-in; exit: ghsr-track-01-out.

No observation recorded.

<a id="case-in_game_visible_travel-100a766e19662d89c9ed"></a>

**90° CCW: unverified** — `in_game_visible_travel-100a766e19662d89c9ed`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: ghsr; role: primary; journey: 7:ghsr-track-01-in>ghsr-track-01-out; entry: ghsr-track-01-in; exit: ghsr-track-01-out.

No observation recorded.

<a id="case-in_game_visible_travel-9608888f553baef36131"></a>

**180° CCW: unverified** — `in_game_visible_travel-9608888f553baef36131`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: ghsr; role: primary; journey: 7:ghsr-track-01-in>ghsr-track-01-out; entry: ghsr-track-01-in; exit: ghsr-track-01-out.

No observation recorded.

<a id="case-in_game_visible_travel-584510f3ec0c3d9372a1"></a>

**270° CCW: unverified** — `in_game_visible_travel-584510f3ec0c3d9372a1`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: ghsr; role: primary; journey: 7:ghsr-track-01-in>ghsr-track-01-out; entry: ghsr-track-01-in; exit: ghsr-track-01-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: ghsr; role: primary; journey: 7:ghsr-track-02-in>ghsr-track-02-out; entry: ghsr-track-02-in; exit: ghsr-track-02-out</summary>

<a id="case-in_game_visible_travel-6e27109cabaee54de1c1"></a>

**0° CCW: unverified** — `in_game_visible_travel-6e27109cabaee54de1c1`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: ghsr; role: primary; journey: 7:ghsr-track-02-in>ghsr-track-02-out; entry: ghsr-track-02-in; exit: ghsr-track-02-out.

No observation recorded.

<a id="case-in_game_visible_travel-133a618e32bf8b2769ff"></a>

**90° CCW: unverified** — `in_game_visible_travel-133a618e32bf8b2769ff`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: ghsr; role: primary; journey: 7:ghsr-track-02-in>ghsr-track-02-out; entry: ghsr-track-02-in; exit: ghsr-track-02-out.

No observation recorded.

<a id="case-in_game_visible_travel-338ce3d9411d845b5a76"></a>

**180° CCW: unverified** — `in_game_visible_travel-338ce3d9411d845b5a76`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: ghsr; role: primary; journey: 7:ghsr-track-02-in>ghsr-track-02-out; entry: ghsr-track-02-in; exit: ghsr-track-02-out.

No observation recorded.

<a id="case-in_game_visible_travel-c906c6082c096ac343e4"></a>

**270° CCW: unverified** — `in_game_visible_travel-c906c6082c096ac343e4`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: ghsr; role: primary; journey: 7:ghsr-track-02-in>ghsr-track-02-out; entry: ghsr-track-02-in; exit: ghsr-track-02-out.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → road — 48 cases; unverified: 48</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: lower-lane-01-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e3d466a8f45129dd22ba">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f3b152be48a9b34b764f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-57e61bd7151e9a068fcc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e7b9d23ae5b47e0ab3f5">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: lower-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b0b6c0a450555409ada6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d940da30e4e938bf17fa">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-521be50ab36ee470332a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-21aee0a3d65711207964">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: lower-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-bf05162024cb1af14b9e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c9a79929d5a00ff6f3b1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4f45ad9ec5d49cdc33c1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-804fe13a183b3d52eed6">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: lower-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f082e76d068f15e083dd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-74167ed2093ec04443b8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c33915f9a924fff12799">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-15c09415964220c367d4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: lower-lane-02-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7fbd286698e998b16f44">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6fc4f05d88a37ff9f114">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0555357b86b6a7ae7206">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3d21b01a2634fa91eed1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: lower-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ce5b336d9797f26ef837">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a0a01c81d77eb198bafc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2573b58a948aecf7e50e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-afaab4108eae30e93ea9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: upper-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f67195a7caaceddc2768">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9d902603017b9b622afc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-216bfa063723ea1ba367">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0d8b0c348ece1a04a8cf">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: upper-lane-01-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8d5d020b2104fe6f038b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-77bff1c4f50f37de2adc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f9e0e4790a248097a473">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8c6bf0c9f6b63c1c36d9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: upper-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-fb5cc05dd088f623fe46">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f0d18769593370946cf9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-73caa6f0db79f20d0d82">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-de38f7d277e7c9075ed6">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: upper-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a261072d5941839f6d37">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-859241c0021f19dbbdf2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0d07d445e2cc99028c49">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f30d1362692fe8a14749">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: upper-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-bd9d72782c3feaa92ba1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-50a20856c3759694e020">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3f2a9d82ebb657d880f4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3865afafa854c800ecc1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: upper-lane-02-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-627606805459be4dc8bc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ffb8c5f12378bb2f8ebf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-83f69aa20625f699b08f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a26ca128a0bdba19345b">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: lower-lane-01-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e3d466a8f45129dd22ba"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e3d466a8f45129dd22ba`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f3b152be48a9b34b764f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f3b152be48a9b34b764f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-57e61bd7151e9a068fcc"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-57e61bd7151e9a068fcc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e7b9d23ae5b47e0ab3f5"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e7b9d23ae5b47e0ab3f5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: lower-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b0b6c0a450555409ada6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b0b6c0a450555409ada6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d940da30e4e938bf17fa"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d940da30e4e938bf17fa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-521be50ab36ee470332a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-521be50ab36ee470332a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-21aee0a3d65711207964"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-21aee0a3d65711207964`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: lower-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-bf05162024cb1af14b9e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-bf05162024cb1af14b9e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c9a79929d5a00ff6f3b1"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c9a79929d5a00ff6f3b1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4f45ad9ec5d49cdc33c1"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4f45ad9ec5d49cdc33c1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-804fe13a183b3d52eed6"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-804fe13a183b3d52eed6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: lower-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f082e76d068f15e083dd"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f082e76d068f15e083dd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-74167ed2093ec04443b8"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-74167ed2093ec04443b8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c33915f9a924fff12799"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c33915f9a924fff12799`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-15c09415964220c367d4"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-15c09415964220c367d4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: lower-lane-02-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7fbd286698e998b16f44"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7fbd286698e998b16f44`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6fc4f05d88a37ff9f114"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6fc4f05d88a37ff9f114`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0555357b86b6a7ae7206"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-0555357b86b6a7ae7206`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3d21b01a2634fa91eed1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3d21b01a2634fa91eed1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: lower-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ce5b336d9797f26ef837"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ce5b336d9797f26ef837`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a0a01c81d77eb198bafc"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a0a01c81d77eb198bafc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2573b58a948aecf7e50e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2573b58a948aecf7e50e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-afaab4108eae30e93ea9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-afaab4108eae30e93ea9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: upper-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f67195a7caaceddc2768"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f67195a7caaceddc2768`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9d902603017b9b622afc"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9d902603017b9b622afc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-216bfa063723ea1ba367"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-216bfa063723ea1ba367`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0d8b0c348ece1a04a8cf"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0d8b0c348ece1a04a8cf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: upper-lane-01-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8d5d020b2104fe6f038b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8d5d020b2104fe6f038b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-77bff1c4f50f37de2adc"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-77bff1c4f50f37de2adc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f9e0e4790a248097a473"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f9e0e4790a248097a473`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8c6bf0c9f6b63c1c36d9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8c6bf0c9f6b63c1c36d9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: upper-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-fb5cc05dd088f623fe46"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-fb5cc05dd088f623fe46`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f0d18769593370946cf9"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f0d18769593370946cf9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-73caa6f0db79f20d0d82"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-73caa6f0db79f20d0d82`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-de38f7d277e7c9075ed6"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-de38f7d277e7c9075ed6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: upper-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a261072d5941839f6d37"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a261072d5941839f6d37`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-859241c0021f19dbbdf2"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-859241c0021f19dbbdf2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0d07d445e2cc99028c49"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-0d07d445e2cc99028c49`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f30d1362692fe8a14749"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f30d1362692fe8a14749`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: upper-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-bd9d72782c3feaa92ba1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-bd9d72782c3feaa92ba1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-50a20856c3759694e020"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-50a20856c3759694e020`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3f2a9d82ebb657d880f4"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3f2a9d82ebb657d880f4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3865afafa854c800ecc1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3865afafa854c800ecc1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: upper-lane-02-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-627606805459be4dc8bc"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-627606805459be4dc8bc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ffb8c5f12378bb2f8ebf"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ffb8c5f12378bb2f8ebf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-83f69aa20625f699b08f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-83f69aa20625f699b08f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a26ca128a0bdba19345b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a26ca128a0bdba19345b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → ghsr — 32 cases; unverified: 32</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: lower-lane-01-in; to port: ghsr-track-02-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-bb5085c94312226ce288">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ae697350805dfc32de13">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-12b4e67924b3ab21f9f5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2651a41ebeb5de4be27e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: lower-lane-01-in; to port: ghsr-track-01-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-51a0873772f80ab90f78">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f45f71fda892d4c38611">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3252c6535774036d6035">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cb0127f993b51c5b143d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: lower-lane-02-in; to port: ghsr-track-02-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-21d9088b7fd6c10c7958">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-28a8f2ff62651a78db4d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-eea7f0a7255055dbe2bf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a679da4da99dbad2cd2e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: lower-lane-02-in; to port: ghsr-track-01-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6a5fe0e16ad0ce6c1327">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b9c4be76f5e123da3300">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5b5c3f2f6a91742b85a2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5bac83b2ed527ac96371">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: upper-lane-01-in; to port: ghsr-track-02-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2da7b382e74eae37f587">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-af354b2529bdac712c05">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-872de7c0a430260b7656">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-724fac5fabd29b2c0535">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: upper-lane-01-in; to port: ghsr-track-01-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8ceba357564d9c9a12e1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-01ed87fa474e5f3524b1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3e162f11aa17c11c32ef">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-746fd3fb5a1cba4d4369">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: upper-lane-02-in; to port: ghsr-track-02-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-dc9aa7f70d7962f76c9e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c0ebc0763540ce260b2c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cbf9234925560a6dcf4a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cdd4bdc0fee781125a3e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: upper-lane-02-in; to port: ghsr-track-01-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-27a58eed28584a0f55c5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ccbf4802174b86831162">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8ddd025e6da850108d1a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-96c4c08537861503a59e">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: lower-lane-01-in; to port: ghsr-track-02-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-bb5085c94312226ce288"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-bb5085c94312226ce288`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: ghsr-track-02-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ae697350805dfc32de13"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ae697350805dfc32de13`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: ghsr-track-02-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-12b4e67924b3ab21f9f5"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-12b4e67924b3ab21f9f5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: ghsr-track-02-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2651a41ebeb5de4be27e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2651a41ebeb5de4be27e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: ghsr-track-02-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: lower-lane-01-in; to port: ghsr-track-01-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-51a0873772f80ab90f78"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-51a0873772f80ab90f78`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: ghsr-track-01-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f45f71fda892d4c38611"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f45f71fda892d4c38611`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: ghsr-track-01-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3252c6535774036d6035"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3252c6535774036d6035`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: ghsr-track-01-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cb0127f993b51c5b143d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-cb0127f993b51c5b143d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: ghsr-track-01-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: lower-lane-02-in; to port: ghsr-track-02-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-21d9088b7fd6c10c7958"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-21d9088b7fd6c10c7958`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: ghsr-track-02-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-28a8f2ff62651a78db4d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-28a8f2ff62651a78db4d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: ghsr-track-02-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-eea7f0a7255055dbe2bf"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-eea7f0a7255055dbe2bf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: ghsr-track-02-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a679da4da99dbad2cd2e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a679da4da99dbad2cd2e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: ghsr-track-02-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: lower-lane-02-in; to port: ghsr-track-01-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6a5fe0e16ad0ce6c1327"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6a5fe0e16ad0ce6c1327`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: ghsr-track-01-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b9c4be76f5e123da3300"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b9c4be76f5e123da3300`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: ghsr-track-01-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5b5c3f2f6a91742b85a2"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5b5c3f2f6a91742b85a2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: ghsr-track-01-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5bac83b2ed527ac96371"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5bac83b2ed527ac96371`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: ghsr-track-01-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: upper-lane-01-in; to port: ghsr-track-02-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2da7b382e74eae37f587"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2da7b382e74eae37f587`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: ghsr-track-02-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-af354b2529bdac712c05"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-af354b2529bdac712c05`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: ghsr-track-02-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-872de7c0a430260b7656"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-872de7c0a430260b7656`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: ghsr-track-02-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-724fac5fabd29b2c0535"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-724fac5fabd29b2c0535`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: ghsr-track-02-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: upper-lane-01-in; to port: ghsr-track-01-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8ceba357564d9c9a12e1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8ceba357564d9c9a12e1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: ghsr-track-01-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-01ed87fa474e5f3524b1"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-01ed87fa474e5f3524b1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: ghsr-track-01-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3e162f11aa17c11c32ef"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3e162f11aa17c11c32ef`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: ghsr-track-01-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-746fd3fb5a1cba4d4369"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-746fd3fb5a1cba4d4369`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: ghsr-track-01-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: upper-lane-02-in; to port: ghsr-track-02-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-dc9aa7f70d7962f76c9e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-dc9aa7f70d7962f76c9e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: ghsr-track-02-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c0ebc0763540ce260b2c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c0ebc0763540ce260b2c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: ghsr-track-02-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cbf9234925560a6dcf4a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-cbf9234925560a6dcf4a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: ghsr-track-02-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cdd4bdc0fee781125a3e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-cdd4bdc0fee781125a3e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: ghsr-track-02-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: upper-lane-02-in; to port: ghsr-track-01-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-27a58eed28584a0f55c5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-27a58eed28584a0f55c5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: ghsr-track-01-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ccbf4802174b86831162"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ccbf4802174b86831162`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: ghsr-track-01-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8ddd025e6da850108d1a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8ddd025e6da850108d1a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: ghsr-track-01-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-96c4c08537861503a59e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-96c4c08537861503a59e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: ghsr-track-01-out; from service: road; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — ghsr → road — 32 cases; unverified: 32</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: ghsr-track-01-in; to port: upper-lane-01-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-63e86a4305bda809339a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-75a1469a4daa4e7e0702">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ddd6b4adc29c22eb641f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f7d61d213d1699450383">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: ghsr-track-01-in; to port: upper-lane-02-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0e16a01bb748454c4b58">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-23c8636a05b7e7dec8e9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a210daf1800f5ae76439">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bb3bcde529218297894e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: ghsr-track-01-in; to port: lower-lane-01-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e61098710b5ffce1d83a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b54f29d1c3e55fe620ac">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3422410cc2d2509084a2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4f10845c7e83be103e0a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: ghsr-track-01-in; to port: lower-lane-02-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f6840e467494228c7bd9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6a21d76c3ccf344d58b9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8009d48d239d1432c547">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-561968492c256194e696">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: ghsr-track-02-in; to port: upper-lane-01-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-821d723667b6e562da59">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dda031e596634eb47405">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f8061e2ec5a92dd41e08">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-aada98ea762d4bf1512e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: ghsr-track-02-in; to port: upper-lane-02-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2b38e39af31dac102eda">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-83e43d6744853a99212a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-33e2469cd1589fa0dd65">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-96edf1ddaf71487afecf">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: ghsr-track-02-in; to port: lower-lane-01-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c8372f23238fbf194311">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6ac8bc275811426f65f9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f0b133bed979d28382c6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a2dca2521f4561dcff57">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: ghsr-track-02-in; to port: lower-lane-02-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-79a9594109cb09a641ec">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7aec3426f7fc32cb1cdf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-262bb933ed31863c7519">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-11615e1dc7cd82be2701">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: ghsr-track-01-in; to port: upper-lane-01-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-63e86a4305bda809339a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-63e86a4305bda809339a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-01-in; to port: upper-lane-01-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-75a1469a4daa4e7e0702"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-75a1469a4daa4e7e0702`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-01-in; to port: upper-lane-01-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ddd6b4adc29c22eb641f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ddd6b4adc29c22eb641f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-01-in; to port: upper-lane-01-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f7d61d213d1699450383"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f7d61d213d1699450383`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-01-in; to port: upper-lane-01-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: ghsr-track-01-in; to port: upper-lane-02-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0e16a01bb748454c4b58"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0e16a01bb748454c4b58`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-01-in; to port: upper-lane-02-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-23c8636a05b7e7dec8e9"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-23c8636a05b7e7dec8e9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-01-in; to port: upper-lane-02-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a210daf1800f5ae76439"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a210daf1800f5ae76439`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-01-in; to port: upper-lane-02-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bb3bcde529218297894e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-bb3bcde529218297894e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-01-in; to port: upper-lane-02-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: ghsr-track-01-in; to port: lower-lane-01-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e61098710b5ffce1d83a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e61098710b5ffce1d83a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-01-in; to port: lower-lane-01-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b54f29d1c3e55fe620ac"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b54f29d1c3e55fe620ac`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-01-in; to port: lower-lane-01-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3422410cc2d2509084a2"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3422410cc2d2509084a2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-01-in; to port: lower-lane-01-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4f10845c7e83be103e0a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4f10845c7e83be103e0a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-01-in; to port: lower-lane-01-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: ghsr-track-01-in; to port: lower-lane-02-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f6840e467494228c7bd9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f6840e467494228c7bd9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-01-in; to port: lower-lane-02-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6a21d76c3ccf344d58b9"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6a21d76c3ccf344d58b9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-01-in; to port: lower-lane-02-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8009d48d239d1432c547"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8009d48d239d1432c547`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-01-in; to port: lower-lane-02-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-561968492c256194e696"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-561968492c256194e696`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-01-in; to port: lower-lane-02-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: ghsr-track-02-in; to port: upper-lane-01-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-821d723667b6e562da59"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-821d723667b6e562da59`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-02-in; to port: upper-lane-01-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dda031e596634eb47405"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-dda031e596634eb47405`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-02-in; to port: upper-lane-01-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f8061e2ec5a92dd41e08"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f8061e2ec5a92dd41e08`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-02-in; to port: upper-lane-01-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-aada98ea762d4bf1512e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-aada98ea762d4bf1512e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-02-in; to port: upper-lane-01-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: ghsr-track-02-in; to port: upper-lane-02-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2b38e39af31dac102eda"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2b38e39af31dac102eda`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-02-in; to port: upper-lane-02-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-83e43d6744853a99212a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-83e43d6744853a99212a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-02-in; to port: upper-lane-02-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-33e2469cd1589fa0dd65"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-33e2469cd1589fa0dd65`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-02-in; to port: upper-lane-02-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-96edf1ddaf71487afecf"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-96edf1ddaf71487afecf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-02-in; to port: upper-lane-02-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: ghsr-track-02-in; to port: lower-lane-01-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c8372f23238fbf194311"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c8372f23238fbf194311`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-02-in; to port: lower-lane-01-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6ac8bc275811426f65f9"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6ac8bc275811426f65f9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-02-in; to port: lower-lane-01-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f0b133bed979d28382c6"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f0b133bed979d28382c6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-02-in; to port: lower-lane-01-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a2dca2521f4561dcff57"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a2dca2521f4561dcff57`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-02-in; to port: lower-lane-01-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: ghsr-track-02-in; to port: lower-lane-02-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-79a9594109cb09a641ec"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-79a9594109cb09a641ec`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-02-in; to port: lower-lane-02-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7aec3426f7fc32cb1cdf"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7aec3426f7fc32cb1cdf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-02-in; to port: lower-lane-02-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-262bb933ed31863c7519"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-262bb933ed31863c7519`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-02-in; to port: lower-lane-02-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-11615e1dc7cd82be2701"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-11615e1dc7cd82be2701`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-02-in; to port: lower-lane-02-out; from service: ghsr; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — ghsr → ghsr — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: ghsr-track-01-in; to port: ghsr-track-02-out; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-289bc797e6cbed06295d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4e44869106fada8595b7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-79f3a162ea77bd999323">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-811d67b9bd2c164780df">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: ghsr-track-02-in; to port: ghsr-track-01-out; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a004837b7d16e8cfbb86">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-82c14c77a19af2262a7f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-59dca28d423866974a7f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-28a9940d789282083a11">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: ghsr-track-01-in; to port: ghsr-track-02-out; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-289bc797e6cbed06295d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-289bc797e6cbed06295d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-01-in; to port: ghsr-track-02-out; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4e44869106fada8595b7"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4e44869106fada8595b7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-01-in; to port: ghsr-track-02-out; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-79f3a162ea77bd999323"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-79f3a162ea77bd999323`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-01-in; to port: ghsr-track-02-out; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-811d67b9bd2c164780df"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-811d67b9bd2c164780df`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-01-in; to port: ghsr-track-02-out; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: ghsr-track-02-in; to port: ghsr-track-01-out; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a004837b7d16e8cfbb86"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a004837b7d16e8cfbb86`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-02-in; to port: ghsr-track-01-out; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-82c14c77a19af2262a7f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-82c14c77a19af2262a7f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-02-in; to port: ghsr-track-01-out; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-59dca28d423866974a7f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-59dca28d423866974a7f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-02-in; to port: ghsr-track-01-out; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-28a9940d789282083a11"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-28a9940d789282083a11`.

Confirm this undeclared transfer is unavailable.

Scope: from port: ghsr-track-02-in; to port: ghsr-track-01-out; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

The original crossing supplied one spatial alignment with four proper rotations repeated. A user report showed that the next adjacent diagonal ground-network position could not meet the same directed highway. Native rule inspection and independent grid measurements established two alignment classes. B adds the complementary horizontal two-tile arrangement, retains the native DD deck directions, and corrects the different native GHSR exterior chord joins. The general lesson is recorded in the [piece workflow](../../../../docs/WORKFLOW_PIECE_CREATION.md#56-cover-diagonal-grid-alignments) and [highway specification](../../NETWORK_SPEC.md#155-two-diagonal-grid-alignments). Existing A IDs, geometry, and frozen evidence are preserved.

The initial B candidate used independent shadow carriers, recorded in the [original native contract](evidence/native-contract.jsonc). The later user request removes those shadows from both crossing alignments and the parallel diamond. The earlier audit remains historical evidence for its own resources, and supplies no game pass for the new no-shadow revision.
