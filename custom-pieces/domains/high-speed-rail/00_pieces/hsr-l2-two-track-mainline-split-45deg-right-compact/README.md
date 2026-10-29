<a id="hsr-l2-split-45-degree-compact"></a>

# HSR Level 2 (15.5 m) — Split 45° Right from Two-Track Mainline — Compact

<!-- SUBJECT IDENTITY MIGRATION -->

Identity migration: `interchange-hsr-split-45-compact` → `hsr-l2-two-track-mainline-split-45deg-right-compact`. Earlier measurements, observations, and pictures retain their recorded names and fingerprints; they do not establish verification of the renamed build. See the [identity migration rules](../../../../docs/NAMING_CONVENTIONS.md#10-choosing-and-changing-names).

Purpose: explain this reusable piece, its matching connections and current test coverage.

<!-- BEGIN PIECE OVERVIEW -->

HSR Level 2 (15.5 m) — Split 45° Right from Two-Track Mainline — Compact. Fixed click-to-place piece in a 3 by 4 tile area. Follow the arrows and join only matching track widths, directions, and height labels. Four proper rotations; the second four states repeat them. Experimental; game testing pending. The mainline retains both directions; only the branch is one-way.

Exact reusable identifier: `hsr-l2-two-track-mainline-split-45deg-right-compact`.

Footprint: **3 × 4 tiles**. Exact menu name: **HSR Level 2 (15.5 m) — Split 45° Right from Two-Track Mainline — Compact**.

Choose this exact name in Transportation → Rail. Press Home or End to rotate; use only the supported states listed below. Join each end to a matching port profile and direction.

- [Connections and journeys](#connections-and-journeys)
- [Test checklist](#test-checklist)

### Design review

**REVIEW NEEDED** — Closely spaced pillars need a support-consolidation review.

- Separate 1.3 m-square pillar foundations have centres less than 2.6 m apart near shared rail geometry. The foundations do not overlap, but the close pair should be reviewed and consolidated to address the reported duplicate-pillar appearance. The 2.6 m review cutoff is an authoring convention, not a structural or game collision threshold.

[Design-review evidence](../../junction-design-review.json).

![HSR Level 2 (15.5 m) — Split 45° Right from Two-Track Mainline — Compact](previews/preview.png)

<!-- END PIECE OVERVIEW -->

<!-- BEGIN MANUAL SUMMARY -->

## Manual status

Generated from [the exact test cases](#test-checklist) and [authoritative observations](checks/manual-tests.json).

- [ ] Preview review: 0/1 applicable cases passed; 0 failed, 0 stale.
- [ ] In-game rendering: 0/4 applicable cases passed; 0 failed, 0 stale.
- [ ] Directed journeys: 0/12 applicable cases passed; 0 failed, 0 stale.

These observations cover only the named services, directions, poses, rotations, and recorded platforms.

<!-- END MANUAL SUMMARY -->

<!-- BEGIN CONNECTIONS -->

## Connections and journeys

Purpose: describe intrinsic directional interfaces and permitted service journeys.

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.jsonc) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `Sout` | hsr / 7 / primary | out | [-2.0, -56.0, 15.5]; [0.0, -1.0]; 0.0 | `path-interface-12d12be31d2057c5763d` |
| `Nin` | hsr / 7 / primary | in | [-2.0, 8.0, 15.5]; [0.0, -1.0]; 0.0 | `path-interface-12d12be31d2057c5763d` |
| `Sin` | hsr / 7 / primary | in | [2.0, -56.0, 15.5]; [0.0, 1.0]; 0.0 | `path-interface-fba09fbeb87ad95c667a` |
| `Nout` | hsr / 7 / primary | out | [2.0, 8.0, 15.5]; [0.0, 1.0]; 0.0 | `path-interface-fba09fbeb87ad95c667a` |
| `Bout` | hsr / 7 / primary | out | [40.0, 0.0, 15.5]; [0.7071067811865475, 0.7071067811865475]; 0.0 | `path-interface-e765ac771bb89f95414d` |

### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| hsr | `Nin` → `Sout` | primary |
| hsr | `Sin` → `Nout` | primary |
| hsr | `Sin` → `Bout` | primary |

### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| hsr / `Nin` | hsr / `Nout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| hsr / `Nin` | hsr / `Bout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| hsr / `Sin` | hsr / `Sout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

<!-- BEGIN MANUAL CHECKS -->

## Test checklist

Generated from [the authoritative record](checks/manual-tests.json). Only explicit human observations create manual passes; software and preview checks remain separate. Expand a check/service group to see its rotation table, then expand the matching exact scope to copy a case ID and inspect its pose, reviewer, environment, and evidence. Grouping changes only this view; every declared case remains separate.

**States:** [x] passed; [ ] unverified, failed, or stale; N/A is an explicit inapplicable declaration. A dash means no case was declared in that column. Every pass covers only its recorded environment. T means a distinct construction-transposed state.

Four proper rotations are covered. No additional reflected state is established by this record; repeated construction aliases do not create new orientations.

Current totals: unverified: 43, passed: 0, failed: 0, stale: 0, not_applicable: 0.

### Record an observation

Follow the [shared testing guide](../../../../docs/TESTING.md); copy [the unconfirmed example](checks/observation.example.json) to `checks/observation.json`. Case identifiers are in the expandable sections below. Do not edit generated checkboxes.

From the repository folder containing `custom-pieces`, run after filling `checks/observation.json` and explicitly confirming the exact observation:

```sh
python3 -m scp.content record --record custom-pieces/domains/high-speed-rail/00_pieces/hsr-l2-two-track-mainline-split-45deg-right-compact/checks/manual-tests.json --observation custom-pieces/domains/high-speed-rail/00_pieces/hsr-l2-two-track-mainline-split-45deg-right-compact/checks/observation.json
```

### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-2793e73bb3f9bd2b2cd3">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-2793e73bb3f9bd2b2cd3"></a>

**General: unverified** — `software_resources-2793e73bb3f9bd2b2cd3`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-2793e73bb3f9bd2b2cd3">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-2793e73bb3f9bd2b2cd3"></a>

**General: unverified** — `software_connectivity-2793e73bb3f9bd2b2cd3`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:interchange-hsr-split-45-compact:canonical-southeast | <a href="#case-preview_review-0326cbdaf65b917ba754">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:interchange-hsr-split-45-compact:canonical-southeast</summary>

<a id="case-preview_review-0326cbdaf65b917ba754"></a>

**General: unverified** — `preview_review-0326cbdaf65b917ba754`.

Inspect this exact preview for tracks, walls, piers, seams and shadows.

Scope: Image: image:interchange-hsr-split-45-compact:canonical-southeast.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-ef24585cc7f067a8f816">[ ] unverified</a> | <a href="#case-in_game_render-5312d496a47b1f77f237">[ ] unverified</a> | <a href="#case-in_game_render-7b025063dd37f087a18b">[ ] unverified</a> | <a href="#case-in_game_render-38b9cfc7d96e04b65e58">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-ef24585cc7f067a8f816"></a>

**0° CCW: unverified** — `in_game_render-ef24585cc7f067a8f816`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-5312d496a47b1f77f237"></a>

**90° CCW: unverified** — `in_game_render-5312d496a47b1f77f237`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-7b025063dd37f087a18b"></a>

**180° CCW: unverified** — `in_game_render-7b025063dd37f087a18b`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-38b9cfc7d96e04b65e58"></a>

**270° CCW: unverified** — `in_game_render-38b9cfc7d96e04b65e58`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-ef24585cc7f067a8f816">[ ] unverified</a> | <a href="#case-in_game_placement-5312d496a47b1f77f237">[ ] unverified</a> | <a href="#case-in_game_placement-7b025063dd37f087a18b">[ ] unverified</a> | <a href="#case-in_game_placement-38b9cfc7d96e04b65e58">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-ef24585cc7f067a8f816"></a>

**0° CCW: unverified** — `in_game_placement-ef24585cc7f067a8f816`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-5312d496a47b1f77f237"></a>

**90° CCW: unverified** — `in_game_placement-5312d496a47b1f77f237`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-7b025063dd37f087a18b"></a>

**180° CCW: unverified** — `in_game_placement-7b025063dd37f087a18b`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-38b9cfc7d96e04b65e58"></a>

**270° CCW: unverified** — `in_game_placement-38b9cfc7d96e04b65e58`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-ef24585cc7f067a8f816">[ ] unverified</a> | <a href="#case-in_game_demolition-5312d496a47b1f77f237">[ ] unverified</a> | <a href="#case-in_game_demolition-7b025063dd37f087a18b">[ ] unverified</a> | <a href="#case-in_game_demolition-38b9cfc7d96e04b65e58">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-ef24585cc7f067a8f816"></a>

**0° CCW: unverified** — `in_game_demolition-ef24585cc7f067a8f816`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-5312d496a47b1f77f237"></a>

**90° CCW: unverified** — `in_game_demolition-5312d496a47b1f77f237`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-7b025063dd37f087a18b"></a>

**180° CCW: unverified** — `in_game_demolition-7b025063dd37f087a18b`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-38b9cfc7d96e04b65e58"></a>

**270° CCW: unverified** — `in_game_demolition-38b9cfc7d96e04b65e58`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-ef24585cc7f067a8f816">[ ] unverified</a> | <a href="#case-in_game_save_reload-5312d496a47b1f77f237">[ ] unverified</a> | <a href="#case-in_game_save_reload-7b025063dd37f087a18b">[ ] unverified</a> | <a href="#case-in_game_save_reload-38b9cfc7d96e04b65e58">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-ef24585cc7f067a8f816"></a>

**0° CCW: unverified** — `in_game_save_reload-ef24585cc7f067a8f816`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-5312d496a47b1f77f237"></a>

**90° CCW: unverified** — `in_game_save_reload-5312d496a47b1f77f237`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-7b025063dd37f087a18b"></a>

**180° CCW: unverified** — `in_game_save_reload-7b025063dd37f087a18b`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-38b9cfc7d96e04b65e58"></a>

**270° CCW: unverified** — `in_game_save_reload-38b9cfc7d96e04b65e58`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Journey — hsr — 12 cases; unverified: 12</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Journey**<br>Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout | — | <a href="#case-in_game_journey-6fde9111868e23f234d6">[ ] unverified</a> | <a href="#case-in_game_journey-e90cadb8eaebad0c7793">[ ] unverified</a> | <a href="#case-in_game_journey-c4969980ea639ab062ba">[ ] unverified</a> | <a href="#case-in_game_journey-74571df8ad49700c69e4">[ ] unverified</a> |
| **Journey**<br>Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout | — | <a href="#case-in_game_journey-aafa47b33ca1ec7bf3f7">[ ] unverified</a> | <a href="#case-in_game_journey-4e7c8863e7c9c69dc64e">[ ] unverified</a> | <a href="#case-in_game_journey-b8fd9b17ecdcf3ea1706">[ ] unverified</a> | <a href="#case-in_game_journey-64a9f39724adab119214">[ ] unverified</a> |
| **Journey**<br>Service: hsr; role: primary; journey: 7:Sin>Bout; entry: Sin; exit: Bout | — | <a href="#case-in_game_journey-9e0a93214107bd05367a">[ ] unverified</a> | <a href="#case-in_game_journey-fcad96fb7e97b2a5e65b">[ ] unverified</a> | <a href="#case-in_game_journey-78610313b1a34a4ace3c">[ ] unverified</a> | <a href="#case-in_game_journey-5b1836bc9b394e9deeb0">[ ] unverified</a> |


<details>
<summary>Journey — Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout</summary>

<a id="case-in_game_journey-6fde9111868e23f234d6"></a>

**0° CCW: unverified** — `in_game_journey-6fde9111868e23f234d6`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

<a id="case-in_game_journey-e90cadb8eaebad0c7793"></a>

**90° CCW: unverified** — `in_game_journey-e90cadb8eaebad0c7793`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

<a id="case-in_game_journey-c4969980ea639ab062ba"></a>

**180° CCW: unverified** — `in_game_journey-c4969980ea639ab062ba`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

<a id="case-in_game_journey-74571df8ad49700c69e4"></a>

**270° CCW: unverified** — `in_game_journey-74571df8ad49700c69e4`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

</details>


<details>
<summary>Journey — Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout</summary>

<a id="case-in_game_journey-aafa47b33ca1ec7bf3f7"></a>

**0° CCW: unverified** — `in_game_journey-aafa47b33ca1ec7bf3f7`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-4e7c8863e7c9c69dc64e"></a>

**90° CCW: unverified** — `in_game_journey-4e7c8863e7c9c69dc64e`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-b8fd9b17ecdcf3ea1706"></a>

**180° CCW: unverified** — `in_game_journey-b8fd9b17ecdcf3ea1706`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-64a9f39724adab119214"></a>

**270° CCW: unverified** — `in_game_journey-64a9f39724adab119214`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

</details>


<details>
<summary>Journey — Service: hsr; role: primary; journey: 7:Sin>Bout; entry: Sin; exit: Bout</summary>

<a id="case-in_game_journey-9e0a93214107bd05367a"></a>

**0° CCW: unverified** — `in_game_journey-9e0a93214107bd05367a`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Bout; entry: Sin; exit: Bout.

No observation recorded.

<a id="case-in_game_journey-fcad96fb7e97b2a5e65b"></a>

**90° CCW: unverified** — `in_game_journey-fcad96fb7e97b2a5e65b`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Bout; entry: Sin; exit: Bout.

No observation recorded.

<a id="case-in_game_journey-78610313b1a34a4ace3c"></a>

**180° CCW: unverified** — `in_game_journey-78610313b1a34a4ace3c`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Bout; entry: Sin; exit: Bout.

No observation recorded.

<a id="case-in_game_journey-5b1836bc9b394e9deeb0"></a>

**270° CCW: unverified** — `in_game_journey-5b1836bc9b394e9deeb0`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Bout; entry: Sin; exit: Bout.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — hsr → hsr — 12 cases; unverified: 12</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c02093c8752d7df4c60d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fe62c05110a25e3b1d73">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ddc4d00fb1b49af40301">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e47d8a06282981ddaf60">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Nin; to port: Bout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ade31defb647201930c3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bfccaa191f8a0b250d0a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-126750bd3c9293031051">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f9d1c80be63d7f7cac0a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-bbcfc1e7f0fc946708c0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8bc6ceb95b9600bb7b59">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1ad5209238c6d0a9b8dc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-acc5f620e14f9e8c13fa">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c02093c8752d7df4c60d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c02093c8752d7df4c60d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fe62c05110a25e3b1d73"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-fe62c05110a25e3b1d73`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ddc4d00fb1b49af40301"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ddc4d00fb1b49af40301`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e47d8a06282981ddaf60"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e47d8a06282981ddaf60`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Nin; to port: Bout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ade31defb647201930c3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ade31defb647201930c3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Bout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bfccaa191f8a0b250d0a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-bfccaa191f8a0b250d0a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Bout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-126750bd3c9293031051"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-126750bd3c9293031051`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Bout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f9d1c80be63d7f7cac0a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f9d1c80be63d7f7cac0a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Bout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-bbcfc1e7f0fc946708c0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-bbcfc1e7f0fc946708c0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8bc6ceb95b9600bb7b59"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8bc6ceb95b9600bb7b59`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1ad5209238c6d0a9b8dc"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1ad5209238c6d0a9b8dc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-acc5f620e14f9e8c13fa"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-acc5f620e14f9e8c13fa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->
