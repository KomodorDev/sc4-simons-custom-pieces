<a id="hsr-l2-split-135-degree-wide"></a>

# HSR Level 2 (15.5 m) — Split 135° Right from Two-Track Mainline — Wide

<!-- SUBJECT IDENTITY MIGRATION -->

Identity migration: `interchange-hsr-split-135-wide` → `hsr-l2-two-track-mainline-split-135deg-right-wide`. Earlier measurements, observations, and pictures retain their recorded names and fingerprints; they do not establish verification of the renamed build. See the [identity migration rules](../../../../docs/NAMING_CONVENTIONS.md#10-choosing-and-changing-names).

Purpose: explain this reusable piece, its matching connections and current test coverage.

<!-- BEGIN PIECE OVERVIEW -->

HSR Level 2 (15.5 m) — Split 135° Right from Two-Track Mainline — Wide. Fixed click-to-place piece in a 12 by 13 tile area. Follow the arrows and join only matching track widths, directions, and height labels. Four proper rotations; the second four states repeat them. Experimental; game testing pending. The mainline retains both directions; only the branch is one-way.

Exact reusable identifier: `hsr-l2-two-track-mainline-split-135deg-right-wide`.

Footprint: **12 × 13 tiles**. Exact menu name: **HSR Level 2 (15.5 m) — Split 135° Right from Two-Track Mainline — Wide**.

Choose this exact name in Transportation → Rail. Press Home or End to rotate; use only the supported states listed below. Join each end to a matching port profile and direction.

- [Connections and journeys](#connections-and-journeys)
- [Test checklist](#test-checklist)

### Design review

**REVIEW NEEDED** — Closely spaced pillars need a support-consolidation review.

- Separate 1.3 m-square pillar foundations have centres less than 2.6 m apart near shared rail geometry. The foundations do not overlap, but the close pair should be reviewed and consolidated to address the reported duplicate-pillar appearance. The 2.6 m review cutoff is an authoring convention, not a structural or game collision threshold.

[Design-review evidence](../../junction-design-review.json).

![HSR Level 2 (15.5 m) — Split 135° Right from Two-Track Mainline — Wide](previews/preview.png)

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
| `Sout` | hsr / 7 / primary | out | [-2.0, -200.0, 15.5]; [0.0, -1.0]; 0.0 | `path-interface-12d12be31d2057c5763d` |
| `Nin` | hsr / 7 / primary | in | [-2.0, -8.0, 15.5]; [0.0, -1.0]; 0.0 | `path-interface-12d12be31d2057c5763d` |
| `Sin` | hsr / 7 / primary | in | [2.0, -200.0, 15.5]; [0.0, 1.0]; 0.0 | `path-interface-fba09fbeb87ad95c667a` |
| `Nout` | hsr / 7 / primary | out | [2.0, -8.0, 15.5]; [0.0, 1.0]; 0.0 | `path-interface-fba09fbeb87ad95c667a` |
| `Bout` | hsr / 7 / primary | out | [184.0, -48.0, 15.5]; [0.7071067811865475, -0.7071067811865475]; 0.0 | `path-interface-e52e55553f098fa8572d` |

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
python3 -m scp.content record --record custom-pieces/domains/high-speed-rail/00_pieces/hsr-l2-two-track-mainline-split-135deg-right-wide/checks/manual-tests.json --observation custom-pieces/domains/high-speed-rail/00_pieces/hsr-l2-two-track-mainline-split-135deg-right-wide/checks/observation.json
```

### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-6a0f7e9f6fe2ddca90e6">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-6a0f7e9f6fe2ddca90e6"></a>

**General: unverified** — `software_resources-6a0f7e9f6fe2ddca90e6`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-6a0f7e9f6fe2ddca90e6">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-6a0f7e9f6fe2ddca90e6"></a>

**General: unverified** — `software_connectivity-6a0f7e9f6fe2ddca90e6`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:interchange-hsr-split-135-wide:canonical-southeast | <a href="#case-preview_review-d2bd09719aa7b9d8f63f">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:interchange-hsr-split-135-wide:canonical-southeast</summary>

<a id="case-preview_review-d2bd09719aa7b9d8f63f"></a>

**General: unverified** — `preview_review-d2bd09719aa7b9d8f63f`.

Inspect this exact preview for tracks, walls, piers, seams and shadows.

Scope: Image: image:interchange-hsr-split-135-wide:canonical-southeast.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-9298a29ba1f88e7932f9">[ ] unverified</a> | <a href="#case-in_game_render-7bd718c1cde312d4f69d">[ ] unverified</a> | <a href="#case-in_game_render-1f4e27da2845edb6de42">[ ] unverified</a> | <a href="#case-in_game_render-6b2cc3df8da25adc5142">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-9298a29ba1f88e7932f9"></a>

**0° CCW: unverified** — `in_game_render-9298a29ba1f88e7932f9`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-7bd718c1cde312d4f69d"></a>

**90° CCW: unverified** — `in_game_render-7bd718c1cde312d4f69d`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-1f4e27da2845edb6de42"></a>

**180° CCW: unverified** — `in_game_render-1f4e27da2845edb6de42`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-6b2cc3df8da25adc5142"></a>

**270° CCW: unverified** — `in_game_render-6b2cc3df8da25adc5142`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-9298a29ba1f88e7932f9">[ ] unverified</a> | <a href="#case-in_game_placement-7bd718c1cde312d4f69d">[ ] unverified</a> | <a href="#case-in_game_placement-1f4e27da2845edb6de42">[ ] unverified</a> | <a href="#case-in_game_placement-6b2cc3df8da25adc5142">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-9298a29ba1f88e7932f9"></a>

**0° CCW: unverified** — `in_game_placement-9298a29ba1f88e7932f9`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-7bd718c1cde312d4f69d"></a>

**90° CCW: unverified** — `in_game_placement-7bd718c1cde312d4f69d`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-1f4e27da2845edb6de42"></a>

**180° CCW: unverified** — `in_game_placement-1f4e27da2845edb6de42`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-6b2cc3df8da25adc5142"></a>

**270° CCW: unverified** — `in_game_placement-6b2cc3df8da25adc5142`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-9298a29ba1f88e7932f9">[ ] unverified</a> | <a href="#case-in_game_demolition-7bd718c1cde312d4f69d">[ ] unverified</a> | <a href="#case-in_game_demolition-1f4e27da2845edb6de42">[ ] unverified</a> | <a href="#case-in_game_demolition-6b2cc3df8da25adc5142">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-9298a29ba1f88e7932f9"></a>

**0° CCW: unverified** — `in_game_demolition-9298a29ba1f88e7932f9`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-7bd718c1cde312d4f69d"></a>

**90° CCW: unverified** — `in_game_demolition-7bd718c1cde312d4f69d`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-1f4e27da2845edb6de42"></a>

**180° CCW: unverified** — `in_game_demolition-1f4e27da2845edb6de42`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-6b2cc3df8da25adc5142"></a>

**270° CCW: unverified** — `in_game_demolition-6b2cc3df8da25adc5142`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-9298a29ba1f88e7932f9">[ ] unverified</a> | <a href="#case-in_game_save_reload-7bd718c1cde312d4f69d">[ ] unverified</a> | <a href="#case-in_game_save_reload-1f4e27da2845edb6de42">[ ] unverified</a> | <a href="#case-in_game_save_reload-6b2cc3df8da25adc5142">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-9298a29ba1f88e7932f9"></a>

**0° CCW: unverified** — `in_game_save_reload-9298a29ba1f88e7932f9`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-7bd718c1cde312d4f69d"></a>

**90° CCW: unverified** — `in_game_save_reload-7bd718c1cde312d4f69d`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-1f4e27da2845edb6de42"></a>

**180° CCW: unverified** — `in_game_save_reload-1f4e27da2845edb6de42`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-6b2cc3df8da25adc5142"></a>

**270° CCW: unverified** — `in_game_save_reload-6b2cc3df8da25adc5142`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Journey — hsr — 12 cases; unverified: 12</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Journey**<br>Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout | — | <a href="#case-in_game_journey-d679ae0398f41b71d9dd">[ ] unverified</a> | <a href="#case-in_game_journey-cb67b139581cf54843b6">[ ] unverified</a> | <a href="#case-in_game_journey-71a1715c5df6d7cf1df7">[ ] unverified</a> | <a href="#case-in_game_journey-274c62427ebad2b45584">[ ] unverified</a> |
| **Journey**<br>Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout | — | <a href="#case-in_game_journey-deca3253bfcb6b6aa195">[ ] unverified</a> | <a href="#case-in_game_journey-6fbd468a503c8f8426c9">[ ] unverified</a> | <a href="#case-in_game_journey-57d37b74169ee4fad6a5">[ ] unverified</a> | <a href="#case-in_game_journey-d6adf055e95268ef307d">[ ] unverified</a> |
| **Journey**<br>Service: hsr; role: primary; journey: 7:Sin>Bout; entry: Sin; exit: Bout | — | <a href="#case-in_game_journey-b9ec75d28e9d1626ace0">[ ] unverified</a> | <a href="#case-in_game_journey-389b42796ce29d6ced58">[ ] unverified</a> | <a href="#case-in_game_journey-57f7260d9223a0ca2220">[ ] unverified</a> | <a href="#case-in_game_journey-e1d369516b538c6a5ccf">[ ] unverified</a> |


<details>
<summary>Journey — Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout</summary>

<a id="case-in_game_journey-d679ae0398f41b71d9dd"></a>

**0° CCW: unverified** — `in_game_journey-d679ae0398f41b71d9dd`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

<a id="case-in_game_journey-cb67b139581cf54843b6"></a>

**90° CCW: unverified** — `in_game_journey-cb67b139581cf54843b6`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

<a id="case-in_game_journey-71a1715c5df6d7cf1df7"></a>

**180° CCW: unverified** — `in_game_journey-71a1715c5df6d7cf1df7`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

<a id="case-in_game_journey-274c62427ebad2b45584"></a>

**270° CCW: unverified** — `in_game_journey-274c62427ebad2b45584`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

</details>


<details>
<summary>Journey — Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout</summary>

<a id="case-in_game_journey-deca3253bfcb6b6aa195"></a>

**0° CCW: unverified** — `in_game_journey-deca3253bfcb6b6aa195`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-6fbd468a503c8f8426c9"></a>

**90° CCW: unverified** — `in_game_journey-6fbd468a503c8f8426c9`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-57d37b74169ee4fad6a5"></a>

**180° CCW: unverified** — `in_game_journey-57d37b74169ee4fad6a5`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-d6adf055e95268ef307d"></a>

**270° CCW: unverified** — `in_game_journey-d6adf055e95268ef307d`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

</details>


<details>
<summary>Journey — Service: hsr; role: primary; journey: 7:Sin>Bout; entry: Sin; exit: Bout</summary>

<a id="case-in_game_journey-b9ec75d28e9d1626ace0"></a>

**0° CCW: unverified** — `in_game_journey-b9ec75d28e9d1626ace0`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Bout; entry: Sin; exit: Bout.

No observation recorded.

<a id="case-in_game_journey-389b42796ce29d6ced58"></a>

**90° CCW: unverified** — `in_game_journey-389b42796ce29d6ced58`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Bout; entry: Sin; exit: Bout.

No observation recorded.

<a id="case-in_game_journey-57f7260d9223a0ca2220"></a>

**180° CCW: unverified** — `in_game_journey-57f7260d9223a0ca2220`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Bout; entry: Sin; exit: Bout.

No observation recorded.

<a id="case-in_game_journey-e1d369516b538c6a5ccf"></a>

**270° CCW: unverified** — `in_game_journey-e1d369516b538c6a5ccf`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Bout; entry: Sin; exit: Bout.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — hsr → hsr — 12 cases; unverified: 12</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c9a25c9b73108b9f59e8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2bd1d5c72b6fb1ec8b16">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cb8812b2445e6793ccab">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1bed570d52449f009b15">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Nin; to port: Bout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-163a4aac13ecb5474e98">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c47b497dc2c6f8927b1a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2d46c396d6bd08717252">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9555b029a476b796a820">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-89e0fce67e4a5eebb9e8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0a51ec0a46d135532dc5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-99d0d9994164db64b856">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a60a1be8b4446469ef38">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c9a25c9b73108b9f59e8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c9a25c9b73108b9f59e8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2bd1d5c72b6fb1ec8b16"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2bd1d5c72b6fb1ec8b16`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cb8812b2445e6793ccab"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-cb8812b2445e6793ccab`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1bed570d52449f009b15"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1bed570d52449f009b15`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Nin; to port: Bout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-163a4aac13ecb5474e98"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-163a4aac13ecb5474e98`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Bout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c47b497dc2c6f8927b1a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c47b497dc2c6f8927b1a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Bout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2d46c396d6bd08717252"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2d46c396d6bd08717252`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Bout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9555b029a476b796a820"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9555b029a476b796a820`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Bout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-89e0fce67e4a5eebb9e8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-89e0fce67e4a5eebb9e8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0a51ec0a46d135532dc5"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0a51ec0a46d135532dc5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-99d0d9994164db64b856"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-99d0d9994164db64b856`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a60a1be8b4446469ef38"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a60a1be8b4446469ef38`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->
