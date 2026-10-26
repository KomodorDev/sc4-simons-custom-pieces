# HSR L2 Parallel One-Way Split

Purpose: explain this reusable piece, its matching connections and current test coverage.

<!-- BEGIN PIECE OVERVIEW -->

Keep the two-track mainline straight while its right-hand forward track separates into a parallel one-way track one tile away.

Exact reusable identifier: `hsr-component-lower-zero-turn-split`.

Footprint: **2 × 8 tiles**. Exact menu name: **HSR L2 Parallel One-Way Split**.

Choose this exact name in Transportation → Rail. Press Home or End to rotate; use only the supported states listed below. Join each end to a matching port profile and direction.

- [Connections and journeys](#connections-and-journeys)
- [Test checklist](#test-checklist)

![HSR L2 Parallel One-Way Split](preview.png)

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

Generated from [connections.json](connections.json). Coordinates are canonical east, north and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.json) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `Sout` | hsr / 7 / primary | out | [-2.0, -120.0, 15.5]; [0.0, -1.0]; 0.0 | `path-interface-12d12be31d2057c5763d` |
| `Nin` | hsr / 7 / primary | in | [-2.0, 8.0, 15.5]; [0.0, -1.0]; 0.0 | `path-interface-12d12be31d2057c5763d` |
| `Sin` | hsr / 7 / primary | in | [2.0, -120.0, 15.5]; [0.0, 1.0]; 0.0 | `path-interface-fba09fbeb87ad95c667a` |
| `Nout` | hsr / 7 / primary | out | [2.0, 8.0, 15.5]; [0.0, 1.0]; 0.0 | `path-interface-fba09fbeb87ad95c667a` |
| `Bout` | hsr / 7 / primary | out | [16.0, 8.0, 15.5]; [0.0, 1.0]; 0.0 | `path-interface-ac60d237d23f01143255` |

### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| hsr | `Nin` → `Sout` | primary |
| hsr | `Sin` → `Bout` | primary |
| hsr | `Sin` → `Nout` | primary |

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
python3 -m scp.content record --record custom-pieces/domains/high-speed-rail/00_pieces/hsr-component-lower-zero-turn-split/checks/manual-tests.json --observation custom-pieces/domains/high-speed-rail/00_pieces/hsr-component-lower-zero-turn-split/checks/observation.json
```

### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-fda22a68c35f9b4a9f2d">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-fda22a68c35f9b4a9f2d"></a>

**General: unverified** — `software_resources-fda22a68c35f9b4a9f2d`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-fda22a68c35f9b4a9f2d">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-fda22a68c35f9b4a9f2d"></a>

**General: unverified** — `software_connectivity-fda22a68c35f9b4a9f2d`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:hsr-component-lower-zero-turn-split:canonical-southeast | <a href="#case-preview_review-4defbf132a96244056e0">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:hsr-component-lower-zero-turn-split:canonical-southeast</summary>

<a id="case-preview_review-4defbf132a96244056e0"></a>

**General: unverified** — `preview_review-4defbf132a96244056e0`.

Inspect this exact preview for tracks, walls, piers, seams and shadows.

Scope: Image: image:hsr-component-lower-zero-turn-split:canonical-southeast.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-13ab1fa767e82b77f51c">[ ] unverified</a> | <a href="#case-in_game_render-7cdeb6dd31b125891e53">[ ] unverified</a> | <a href="#case-in_game_render-9793d2fd5c33ebcd8c50">[ ] unverified</a> | <a href="#case-in_game_render-963d0e5aedddabec1e38">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-13ab1fa767e82b77f51c"></a>

**0° CCW: unverified** — `in_game_render-13ab1fa767e82b77f51c`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-7cdeb6dd31b125891e53"></a>

**90° CCW: unverified** — `in_game_render-7cdeb6dd31b125891e53`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-9793d2fd5c33ebcd8c50"></a>

**180° CCW: unverified** — `in_game_render-9793d2fd5c33ebcd8c50`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-963d0e5aedddabec1e38"></a>

**270° CCW: unverified** — `in_game_render-963d0e5aedddabec1e38`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-13ab1fa767e82b77f51c">[ ] unverified</a> | <a href="#case-in_game_placement-7cdeb6dd31b125891e53">[ ] unverified</a> | <a href="#case-in_game_placement-9793d2fd5c33ebcd8c50">[ ] unverified</a> | <a href="#case-in_game_placement-963d0e5aedddabec1e38">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-13ab1fa767e82b77f51c"></a>

**0° CCW: unverified** — `in_game_placement-13ab1fa767e82b77f51c`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-7cdeb6dd31b125891e53"></a>

**90° CCW: unverified** — `in_game_placement-7cdeb6dd31b125891e53`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-9793d2fd5c33ebcd8c50"></a>

**180° CCW: unverified** — `in_game_placement-9793d2fd5c33ebcd8c50`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-963d0e5aedddabec1e38"></a>

**270° CCW: unverified** — `in_game_placement-963d0e5aedddabec1e38`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-13ab1fa767e82b77f51c">[ ] unverified</a> | <a href="#case-in_game_demolition-7cdeb6dd31b125891e53">[ ] unverified</a> | <a href="#case-in_game_demolition-9793d2fd5c33ebcd8c50">[ ] unverified</a> | <a href="#case-in_game_demolition-963d0e5aedddabec1e38">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-13ab1fa767e82b77f51c"></a>

**0° CCW: unverified** — `in_game_demolition-13ab1fa767e82b77f51c`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-7cdeb6dd31b125891e53"></a>

**90° CCW: unverified** — `in_game_demolition-7cdeb6dd31b125891e53`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-9793d2fd5c33ebcd8c50"></a>

**180° CCW: unverified** — `in_game_demolition-9793d2fd5c33ebcd8c50`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-963d0e5aedddabec1e38"></a>

**270° CCW: unverified** — `in_game_demolition-963d0e5aedddabec1e38`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-13ab1fa767e82b77f51c">[ ] unverified</a> | <a href="#case-in_game_save_reload-7cdeb6dd31b125891e53">[ ] unverified</a> | <a href="#case-in_game_save_reload-9793d2fd5c33ebcd8c50">[ ] unverified</a> | <a href="#case-in_game_save_reload-963d0e5aedddabec1e38">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-13ab1fa767e82b77f51c"></a>

**0° CCW: unverified** — `in_game_save_reload-13ab1fa767e82b77f51c`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-7cdeb6dd31b125891e53"></a>

**90° CCW: unverified** — `in_game_save_reload-7cdeb6dd31b125891e53`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-9793d2fd5c33ebcd8c50"></a>

**180° CCW: unverified** — `in_game_save_reload-9793d2fd5c33ebcd8c50`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-963d0e5aedddabec1e38"></a>

**270° CCW: unverified** — `in_game_save_reload-963d0e5aedddabec1e38`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Journey — hsr — 12 cases; unverified: 12</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Journey**<br>Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout | — | <a href="#case-in_game_journey-4d8766101808f72671a1">[ ] unverified</a> | <a href="#case-in_game_journey-bc9c33678d4d7dbf68e1">[ ] unverified</a> | <a href="#case-in_game_journey-8bb0e6da492bca35adaf">[ ] unverified</a> | <a href="#case-in_game_journey-0750475af3456b216609">[ ] unverified</a> |
| **Journey**<br>Service: hsr; role: primary; journey: 7:Sin>Bout; entry: Sin; exit: Bout | — | <a href="#case-in_game_journey-ffb474a71b42a3b7741a">[ ] unverified</a> | <a href="#case-in_game_journey-d11991b0b93fe0ad2fb6">[ ] unverified</a> | <a href="#case-in_game_journey-560c705331fe07fb63d5">[ ] unverified</a> | <a href="#case-in_game_journey-e5bb47ef18d31559ae90">[ ] unverified</a> |
| **Journey**<br>Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout | — | <a href="#case-in_game_journey-4dcdf6c807ecebf20026">[ ] unverified</a> | <a href="#case-in_game_journey-7b1d666ad0283a14ebf6">[ ] unverified</a> | <a href="#case-in_game_journey-10c6b3ded84870fd3f70">[ ] unverified</a> | <a href="#case-in_game_journey-a697736531b865663a6b">[ ] unverified</a> |


<details>
<summary>Journey — Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout</summary>

<a id="case-in_game_journey-4d8766101808f72671a1"></a>

**0° CCW: unverified** — `in_game_journey-4d8766101808f72671a1`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

<a id="case-in_game_journey-bc9c33678d4d7dbf68e1"></a>

**90° CCW: unverified** — `in_game_journey-bc9c33678d4d7dbf68e1`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

<a id="case-in_game_journey-8bb0e6da492bca35adaf"></a>

**180° CCW: unverified** — `in_game_journey-8bb0e6da492bca35adaf`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

<a id="case-in_game_journey-0750475af3456b216609"></a>

**270° CCW: unverified** — `in_game_journey-0750475af3456b216609`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

</details>


<details>
<summary>Journey — Service: hsr; role: primary; journey: 7:Sin>Bout; entry: Sin; exit: Bout</summary>

<a id="case-in_game_journey-ffb474a71b42a3b7741a"></a>

**0° CCW: unverified** — `in_game_journey-ffb474a71b42a3b7741a`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Bout; entry: Sin; exit: Bout.

No observation recorded.

<a id="case-in_game_journey-d11991b0b93fe0ad2fb6"></a>

**90° CCW: unverified** — `in_game_journey-d11991b0b93fe0ad2fb6`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Bout; entry: Sin; exit: Bout.

No observation recorded.

<a id="case-in_game_journey-560c705331fe07fb63d5"></a>

**180° CCW: unverified** — `in_game_journey-560c705331fe07fb63d5`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Bout; entry: Sin; exit: Bout.

No observation recorded.

<a id="case-in_game_journey-e5bb47ef18d31559ae90"></a>

**270° CCW: unverified** — `in_game_journey-e5bb47ef18d31559ae90`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Bout; entry: Sin; exit: Bout.

No observation recorded.

</details>


<details>
<summary>Journey — Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout</summary>

<a id="case-in_game_journey-4dcdf6c807ecebf20026"></a>

**0° CCW: unverified** — `in_game_journey-4dcdf6c807ecebf20026`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-7b1d666ad0283a14ebf6"></a>

**90° CCW: unverified** — `in_game_journey-7b1d666ad0283a14ebf6`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-10c6b3ded84870fd3f70"></a>

**180° CCW: unverified** — `in_game_journey-10c6b3ded84870fd3f70`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-a697736531b865663a6b"></a>

**270° CCW: unverified** — `in_game_journey-a697736531b865663a6b`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — hsr → hsr — 12 cases; unverified: 12</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b687a224bdaca491cb23">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-81fc26010ce41041cd3d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f34af9ab27d55d4d69eb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-85c61d39fe6fbcd9ae3b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Nin; to port: Bout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-005adad08736fbdd454d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ae0d3a0dffa2e4c2da8c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cc4f4389329f551e607b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c73eabc6174b47e295d3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-79b418b5206cb64b8483">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3b6d16a7f40f37b7da9d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ef2bc7542201f7bad4c9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0b0affe88f0e86b52eb4">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b687a224bdaca491cb23"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b687a224bdaca491cb23`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-81fc26010ce41041cd3d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-81fc26010ce41041cd3d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f34af9ab27d55d4d69eb"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f34af9ab27d55d4d69eb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-85c61d39fe6fbcd9ae3b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-85c61d39fe6fbcd9ae3b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Nin; to port: Bout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-005adad08736fbdd454d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-005adad08736fbdd454d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Bout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ae0d3a0dffa2e4c2da8c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ae0d3a0dffa2e4c2da8c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Bout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cc4f4389329f551e607b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-cc4f4389329f551e607b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Bout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c73eabc6174b47e295d3"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c73eabc6174b47e295d3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Bout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-79b418b5206cb64b8483"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-79b418b5206cb64b8483`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3b6d16a7f40f37b7da9d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3b6d16a7f40f37b7da9d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ef2bc7542201f7bad4c9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ef2bc7542201f7bad4c9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0b0affe88f0e86b52eb4"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0b0affe88f0e86b52eb4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->
