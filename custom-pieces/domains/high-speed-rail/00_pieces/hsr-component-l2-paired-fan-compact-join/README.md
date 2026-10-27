# HSR L2 Compact Paired Fan Join

Purpose: Explain the reusable paired fan, its matching split/merge connections, compact platform edge and current test coverage.

Two opposite-direction HSR tracks at **15.5 m** separate into matching curved connections. At the default orientation, southbound traffic arriving from the north takes the western curve; traffic arriving on the eastern curve continues north. The north-facing end uses the ordinary paired HSR profile.

Connect the eastern curved end to **[HSR L2 Compact Fan Diverge](../hsr-component-l2-compact-fan-diverge/README.md)**. Connect the western curved end to **[HSR L2 Short Opposed Merge Core](../hsr-component-l2-short-opposed-merge-core/README.md)**. These curved ports have specific positions and headings; they do not accept a normal cardinal straight directly.

The platform's outer corner is shaped to allow an ordinary mainline straight beside the compact diverge. The train routes and seven support positions remain those of the full fan. This is a separate selectable type; the earlier fan remains available for its existing layout.

The piece occupies **15 tiles** inside a **7 × 5 tile** construction rectangle. Its software construction reference can be in an empty square, so align the complete model and its connections. Placement, moving trains, rotation controls and save/reload remain unverified inside SimCity 4.

Both views show the same complete compiled piece at its default **0° orientation**. Their local southwest tile centre is **(X0, Y0)**; the top view keeps north upward. These software pictures do not establish operation inside the game.

[Angled view](previews/preview.png) · [North-up top view](previews/preview-top.png)

Definition: [piece.json](piece.json). Independent geometry: [geometry.json](geometry.json). The generated connection overview and exact test cases below describe the current saved resources.

<!-- BEGIN PIECE OVERVIEW -->

Paired fan connection with native15.5m paths and a coordinated outer corner for the Compact Fan Diverge; retains the established curved connection positions and support spacing.

Exact reusable identifier: `hsr-component-l2-paired-fan-compact-join`.

Footprint: **7 × 5 tiles**. Exact menu name: **HSR L2 Compact Paired Fan Join**.

Choose this exact name in Transportation → Rail. Press Home or End to rotate; use only the supported states listed below. Join each end to a matching port profile and direction.

- [Connections and journeys](#connections-and-journeys)
- [Test checklist](#test-checklist)

![HSR L2 Compact Paired Fan Join](previews/preview.png)

![HSR L2 Compact Paired Fan Join — top view](previews/preview-top.png)

<!-- END PIECE OVERVIEW -->

<!-- BEGIN MANUAL SUMMARY -->

## Manual status

Generated from [the exact test cases](#test-checklist) and [authoritative observations](checks/manual-tests.json).

- [ ] Preview review: 0/2 applicable cases passed; 0 failed, 0 stale.
- [ ] In-game rendering: 0/4 applicable cases passed; 0 failed, 0 stale.
- [ ] Directed journeys: 0/8 applicable cases passed; 0 failed, 0 stale.

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
| `Wout` | hsr / 7 / primary | out | [16.562689, -72.0, 15.5]; [-0.9121771234450041, -0.4097961633100019]; 0.0 | `path-interface-cbe8d469a6c3c876ed7f` |
| `Nin` | hsr / 7 / primary | in | [46.0, 8.0, 15.5]; [0.0, -1.0]; 0.0 | `path-interface-12d12be31d2057c5763d` |
| `Nout` | hsr / 7 / primary | out | [50.0, 8.0, 15.5]; [0.0, 1.0]; 0.0 | `path-interface-fba09fbeb87ad95c667a` |
| `Ein` | hsr / 7 / primary | in | [79.437311, -72.0, 15.5]; [-0.9121771234450041, 0.4097961633100019]; 0.0 | `path-interface-187e749c1d9d220c3c88` |

### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| hsr | `Nin` → `Wout` | primary |
| hsr | `Ein` → `Nout` | primary |

### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| hsr / `Nin` | hsr / `Nout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| hsr / `Ein` | hsr / `Wout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

<!-- BEGIN MANUAL CHECKS -->

## Test checklist

Generated from [the authoritative record](checks/manual-tests.json). Only explicit human observations create manual passes; software and preview checks remain separate. Expand a check/service group to see its rotation table, then expand the matching exact scope to copy a case ID and inspect its pose, reviewer, environment, and evidence. Grouping changes only this view; every declared case remains separate.

**States:** [x] passed; [ ] unverified, failed, or stale; N/A is an explicit inapplicable declaration. A dash means no case was declared in that column. Every pass covers only its recorded environment. T means a distinct construction-transposed state.

Four proper rotations are covered. No additional reflected state is established by this record; repeated construction aliases do not create new orientations.

Current totals: unverified: 34, passed: 2, failed: 0, stale: 0, not_applicable: 0.

### Record an observation

Follow the [shared testing guide](../../../../docs/TESTING.md); copy [the unconfirmed example](checks/observation.example.json) to `checks/observation.json`. Case identifiers are in the expandable sections below. Do not edit generated checkboxes.

From the repository folder containing `custom-pieces`, run after filling `checks/observation.json` and explicitly confirming the exact observation:

```sh
python3 -m scp.content record --record custom-pieces/domains/high-speed-rail/00_pieces/hsr-component-l2-paired-fan-compact-join/checks/manual-tests.json --observation custom-pieces/domains/high-speed-rail/00_pieces/hsr-component-l2-paired-fan-compact-join/checks/observation.json
```

### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; passed: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-bc65ebc1e8aece8c8a6d">[x] passed</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-bc65ebc1e8aece8c8a6d"></a>

**General: passed** — `software_resources-bc65ebc1e8aece8c8a6d`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: software; reviewer: verify_hsr_trumpet_v4.py plus current compiled-resource checks; confirmed at: 2026-10-20T11:45:51.432103+00:00; evidence: [../../01_assemblies/straight-stem-trumpet-v4/evidence/validation.json]; environment: 

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; passed: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-bc65ebc1e8aece8c8a6d">[x] passed</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-bc65ebc1e8aece8c8a6d"></a>

**General: passed** — `software_connectivity-bc65ebc1e8aece8c8a6d`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: software; reviewer: verify_hsr_trumpet_v4.py plus current compiled-resource checks; confirmed at: 2026-10-20T11:45:51.438799+00:00; evidence: [../../01_assemblies/straight-stem-trumpet-v4/evidence/validation.json]; environment: 

</details>

</details>

<details>
<summary>Preview review — Images — 2 cases; unverified: 2</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:hsr-component-l2-paired-fan-compact-join:canonical-southeast | <a href="#case-preview_review-3cb6c2661802b929620d">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:hsr-component-l2-paired-fan-compact-join:canonical-top | <a href="#case-preview_review-f59bcfa100a7ff0db938">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:hsr-component-l2-paired-fan-compact-join:canonical-southeast</summary>

<a id="case-preview_review-3cb6c2661802b929620d"></a>

**General: unverified** — `preview_review-3cb6c2661802b929620d`.

Inspect this exact preview for tracks, walls, piers, seams and shadows.

Scope: Image: image:hsr-component-l2-paired-fan-compact-join:canonical-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:hsr-component-l2-paired-fan-compact-join:canonical-top</summary>

<a id="case-preview_review-f59bcfa100a7ff0db938"></a>

**General: unverified** — `preview_review-f59bcfa100a7ff0db938`.

Inspect this exact preview for tracks, walls, piers, seams and shadows.

Scope: Image: image:hsr-component-l2-paired-fan-compact-join:canonical-top.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-2953a796038b1c66047b">[ ] unverified</a> | <a href="#case-in_game_render-9f1c3339be8608575afb">[ ] unverified</a> | <a href="#case-in_game_render-3ebb754476ae4beaee16">[ ] unverified</a> | <a href="#case-in_game_render-aa233b7e5bab139363c3">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-2953a796038b1c66047b"></a>

**0° CCW: unverified** — `in_game_render-2953a796038b1c66047b`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-9f1c3339be8608575afb"></a>

**90° CCW: unverified** — `in_game_render-9f1c3339be8608575afb`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-3ebb754476ae4beaee16"></a>

**180° CCW: unverified** — `in_game_render-3ebb754476ae4beaee16`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-aa233b7e5bab139363c3"></a>

**270° CCW: unverified** — `in_game_render-aa233b7e5bab139363c3`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-2953a796038b1c66047b">[ ] unverified</a> | <a href="#case-in_game_placement-9f1c3339be8608575afb">[ ] unverified</a> | <a href="#case-in_game_placement-3ebb754476ae4beaee16">[ ] unverified</a> | <a href="#case-in_game_placement-aa233b7e5bab139363c3">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-2953a796038b1c66047b"></a>

**0° CCW: unverified** — `in_game_placement-2953a796038b1c66047b`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-9f1c3339be8608575afb"></a>

**90° CCW: unverified** — `in_game_placement-9f1c3339be8608575afb`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-3ebb754476ae4beaee16"></a>

**180° CCW: unverified** — `in_game_placement-3ebb754476ae4beaee16`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-aa233b7e5bab139363c3"></a>

**270° CCW: unverified** — `in_game_placement-aa233b7e5bab139363c3`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-2953a796038b1c66047b">[ ] unverified</a> | <a href="#case-in_game_demolition-9f1c3339be8608575afb">[ ] unverified</a> | <a href="#case-in_game_demolition-3ebb754476ae4beaee16">[ ] unverified</a> | <a href="#case-in_game_demolition-aa233b7e5bab139363c3">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-2953a796038b1c66047b"></a>

**0° CCW: unverified** — `in_game_demolition-2953a796038b1c66047b`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-9f1c3339be8608575afb"></a>

**90° CCW: unverified** — `in_game_demolition-9f1c3339be8608575afb`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-3ebb754476ae4beaee16"></a>

**180° CCW: unverified** — `in_game_demolition-3ebb754476ae4beaee16`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-aa233b7e5bab139363c3"></a>

**270° CCW: unverified** — `in_game_demolition-aa233b7e5bab139363c3`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-2953a796038b1c66047b">[ ] unverified</a> | <a href="#case-in_game_save_reload-9f1c3339be8608575afb">[ ] unverified</a> | <a href="#case-in_game_save_reload-3ebb754476ae4beaee16">[ ] unverified</a> | <a href="#case-in_game_save_reload-aa233b7e5bab139363c3">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-2953a796038b1c66047b"></a>

**0° CCW: unverified** — `in_game_save_reload-2953a796038b1c66047b`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-9f1c3339be8608575afb"></a>

**90° CCW: unverified** — `in_game_save_reload-9f1c3339be8608575afb`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-3ebb754476ae4beaee16"></a>

**180° CCW: unverified** — `in_game_save_reload-3ebb754476ae4beaee16`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-aa233b7e5bab139363c3"></a>

**270° CCW: unverified** — `in_game_save_reload-aa233b7e5bab139363c3`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Journey — hsr — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Journey**<br>Service: hsr; role: primary; journey: 7:Nin>Wout; entry: Nin; exit: Wout | — | <a href="#case-in_game_journey-efa01c69d3d0a595addc">[ ] unverified</a> | <a href="#case-in_game_journey-f0765824bce6e2085023">[ ] unverified</a> | <a href="#case-in_game_journey-accf1bc882028a242b30">[ ] unverified</a> | <a href="#case-in_game_journey-6168c4cc5136e21b2f7b">[ ] unverified</a> |
| **Journey**<br>Service: hsr; role: primary; journey: 7:Ein>Nout; entry: Ein; exit: Nout | — | <a href="#case-in_game_journey-65a9b6549c48f167a40e">[ ] unverified</a> | <a href="#case-in_game_journey-fe64d25bac6aea848487">[ ] unverified</a> | <a href="#case-in_game_journey-89e5e4b7f562bc923192">[ ] unverified</a> | <a href="#case-in_game_journey-cec0cc3b6c354f5dbbcf">[ ] unverified</a> |


<details>
<summary>Journey — Service: hsr; role: primary; journey: 7:Nin>Wout; entry: Nin; exit: Wout</summary>

<a id="case-in_game_journey-efa01c69d3d0a595addc"></a>

**0° CCW: unverified** — `in_game_journey-efa01c69d3d0a595addc`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Wout; entry: Nin; exit: Wout.

No observation recorded.

<a id="case-in_game_journey-f0765824bce6e2085023"></a>

**90° CCW: unverified** — `in_game_journey-f0765824bce6e2085023`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Wout; entry: Nin; exit: Wout.

No observation recorded.

<a id="case-in_game_journey-accf1bc882028a242b30"></a>

**180° CCW: unverified** — `in_game_journey-accf1bc882028a242b30`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Wout; entry: Nin; exit: Wout.

No observation recorded.

<a id="case-in_game_journey-6168c4cc5136e21b2f7b"></a>

**270° CCW: unverified** — `in_game_journey-6168c4cc5136e21b2f7b`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Wout; entry: Nin; exit: Wout.

No observation recorded.

</details>


<details>
<summary>Journey — Service: hsr; role: primary; journey: 7:Ein>Nout; entry: Ein; exit: Nout</summary>

<a id="case-in_game_journey-65a9b6549c48f167a40e"></a>

**0° CCW: unverified** — `in_game_journey-65a9b6549c48f167a40e`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Ein>Nout; entry: Ein; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-fe64d25bac6aea848487"></a>

**90° CCW: unverified** — `in_game_journey-fe64d25bac6aea848487`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Ein>Nout; entry: Ein; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-89e5e4b7f562bc923192"></a>

**180° CCW: unverified** — `in_game_journey-89e5e4b7f562bc923192`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Ein>Nout; entry: Ein; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-cec0cc3b6c354f5dbbcf"></a>

**270° CCW: unverified** — `in_game_journey-cec0cc3b6c354f5dbbcf`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Ein>Nout; entry: Ein; exit: Nout.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — hsr → hsr — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3ad08e7a19456cd90fd0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4d4bf82777d040a92574">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f8a6e6bba23dded7d7ae">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-690df8549dc3f5fda576">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Ein; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-97aa23dd677c7b8c9e3c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cf602616988bd0a9a85a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c35a186b255281e199c9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c046e5e0bc2afa332fca">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3ad08e7a19456cd90fd0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3ad08e7a19456cd90fd0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4d4bf82777d040a92574"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4d4bf82777d040a92574`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f8a6e6bba23dded7d7ae"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f8a6e6bba23dded7d7ae`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-690df8549dc3f5fda576"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-690df8549dc3f5fda576`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Ein; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-97aa23dd677c7b8c9e3c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-97aa23dd677c7b8c9e3c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cf602616988bd0a9a85a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-cf602616988bd0a9a85a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c35a186b255281e199c9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c35a186b255281e199c9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c046e5e0bc2afa332fca"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c046e5e0bc2afa332fca`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->
