# GHSR Merge 135 Degree Compact

Purpose: explain this reusable piece, its matching connections and current test coverage.

<!-- BEGIN PIECE OVERVIEW -->

GHSR Merge 135 Degree Compact. Fixed click-to-place piece in a 6 by 6 tile area. Follow the arrows and join only matching track widths, directions, and height labels. Four proper rotations; the second four states repeat them. Experimental; game testing pending. The mainline retains both directions; only the branch is one-way.

Exact reusable identifier: `interchange-ground-merge-135-compact`.

Footprint: **6 × 6 tiles**. Exact menu name: **GHSR Merge 135 Degree Compact**.

Choose this exact name in Transportation → Rail. Press Home or End to rotate; use only the supported states listed below. Join each end to a matching port profile and direction.

- [Connections and journeys](#connections-and-journeys)
- [Test checklist](#test-checklist)

![GHSR Merge 135 Degree Compact](preview.png)

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
| `Sout` | ghsr / 7 / primary | out | [-2.0, -88.0, 1.0]; [0.0, -1.0]; 0.0 | `path-interface-c78c5ac4b558d84b46f2` |
| `Nin` | ghsr / 7 / primary | in | [-2.0, 8.0, 1.0]; [0.0, -1.0]; 0.0 | `path-interface-c78c5ac4b558d84b46f2` |
| `Sin` | ghsr / 7 / primary | in | [2.0, -88.0, 1.0]; [0.0, 1.0]; 0.0 | `path-interface-fab587419de6b5848d74` |
| `Nout` | ghsr / 7 / primary | out | [2.0, 8.0, 1.0]; [0.0, 1.0]; 0.0 | `path-interface-fab587419de6b5848d74` |
| `Bin` | ghsr / 7 / primary | in | [88.0, -64.0, 1.0]; [-0.7071067811865475, -0.7071067811865475]; 0.0 | `path-interface-f99fce9a9cdaf09202fb` |

### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| ghsr | `Nin` → `Sout` | primary |
| ghsr | `Sin` → `Nout` | primary |
| ghsr | `Bin` → `Nout` | primary |

### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| ghsr / `Nin` | ghsr / `Nout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| ghsr / `Sin` | ghsr / `Sout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| ghsr / `Bin` | ghsr / `Sout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |

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
python3 -m scp.content record --record custom-pieces/domains/high-speed-rail/00_pieces/interchange-ground-merge-135-compact/checks/manual-tests.json --observation custom-pieces/domains/high-speed-rail/00_pieces/interchange-ground-merge-135-compact/checks/observation.json
```

### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-0efd1a56ce5002a5bb35">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-0efd1a56ce5002a5bb35"></a>

**General: unverified** — `software_resources-0efd1a56ce5002a5bb35`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-0efd1a56ce5002a5bb35">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-0efd1a56ce5002a5bb35"></a>

**General: unverified** — `software_connectivity-0efd1a56ce5002a5bb35`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:interchange-ground-merge-135-compact:canonical-southeast | <a href="#case-preview_review-bc19255fe868ba606b47">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:interchange-ground-merge-135-compact:canonical-southeast</summary>

<a id="case-preview_review-bc19255fe868ba606b47"></a>

**General: unverified** — `preview_review-bc19255fe868ba606b47`.

Inspect this exact preview for tracks, walls, piers, seams and shadows.

Scope: Image: image:interchange-ground-merge-135-compact:canonical-southeast.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-5c56adda1548f6019b55">[ ] unverified</a> | <a href="#case-in_game_render-3cbf340732c0d49d5b62">[ ] unverified</a> | <a href="#case-in_game_render-ea56ff4a86a0b6650534">[ ] unverified</a> | <a href="#case-in_game_render-c51024c79ace103483ad">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-5c56adda1548f6019b55"></a>

**0° CCW: unverified** — `in_game_render-5c56adda1548f6019b55`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-3cbf340732c0d49d5b62"></a>

**90° CCW: unverified** — `in_game_render-3cbf340732c0d49d5b62`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-ea56ff4a86a0b6650534"></a>

**180° CCW: unverified** — `in_game_render-ea56ff4a86a0b6650534`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-c51024c79ace103483ad"></a>

**270° CCW: unverified** — `in_game_render-c51024c79ace103483ad`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-5c56adda1548f6019b55">[ ] unverified</a> | <a href="#case-in_game_placement-3cbf340732c0d49d5b62">[ ] unverified</a> | <a href="#case-in_game_placement-ea56ff4a86a0b6650534">[ ] unverified</a> | <a href="#case-in_game_placement-c51024c79ace103483ad">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-5c56adda1548f6019b55"></a>

**0° CCW: unverified** — `in_game_placement-5c56adda1548f6019b55`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-3cbf340732c0d49d5b62"></a>

**90° CCW: unverified** — `in_game_placement-3cbf340732c0d49d5b62`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-ea56ff4a86a0b6650534"></a>

**180° CCW: unverified** — `in_game_placement-ea56ff4a86a0b6650534`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-c51024c79ace103483ad"></a>

**270° CCW: unverified** — `in_game_placement-c51024c79ace103483ad`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-5c56adda1548f6019b55">[ ] unverified</a> | <a href="#case-in_game_demolition-3cbf340732c0d49d5b62">[ ] unverified</a> | <a href="#case-in_game_demolition-ea56ff4a86a0b6650534">[ ] unverified</a> | <a href="#case-in_game_demolition-c51024c79ace103483ad">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-5c56adda1548f6019b55"></a>

**0° CCW: unverified** — `in_game_demolition-5c56adda1548f6019b55`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-3cbf340732c0d49d5b62"></a>

**90° CCW: unverified** — `in_game_demolition-3cbf340732c0d49d5b62`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-ea56ff4a86a0b6650534"></a>

**180° CCW: unverified** — `in_game_demolition-ea56ff4a86a0b6650534`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-c51024c79ace103483ad"></a>

**270° CCW: unverified** — `in_game_demolition-c51024c79ace103483ad`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-5c56adda1548f6019b55">[ ] unverified</a> | <a href="#case-in_game_save_reload-3cbf340732c0d49d5b62">[ ] unverified</a> | <a href="#case-in_game_save_reload-ea56ff4a86a0b6650534">[ ] unverified</a> | <a href="#case-in_game_save_reload-c51024c79ace103483ad">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-5c56adda1548f6019b55"></a>

**0° CCW: unverified** — `in_game_save_reload-5c56adda1548f6019b55`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-3cbf340732c0d49d5b62"></a>

**90° CCW: unverified** — `in_game_save_reload-3cbf340732c0d49d5b62`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-ea56ff4a86a0b6650534"></a>

**180° CCW: unverified** — `in_game_save_reload-ea56ff4a86a0b6650534`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-c51024c79ace103483ad"></a>

**270° CCW: unverified** — `in_game_save_reload-c51024c79ace103483ad`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Journey — ghsr — 12 cases; unverified: 12</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Journey**<br>Service: ghsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout | — | <a href="#case-in_game_journey-4e75f983e04a39cb9208">[ ] unverified</a> | <a href="#case-in_game_journey-26af7182ff9386e8b7b6">[ ] unverified</a> | <a href="#case-in_game_journey-503c9989f019a3663a85">[ ] unverified</a> | <a href="#case-in_game_journey-3ed61c264e6c4008c2a6">[ ] unverified</a> |
| **Journey**<br>Service: ghsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout | — | <a href="#case-in_game_journey-ef4eccd47d5f2cb459a8">[ ] unverified</a> | <a href="#case-in_game_journey-acaad059037c450d967b">[ ] unverified</a> | <a href="#case-in_game_journey-34bbeb558ea55173d402">[ ] unverified</a> | <a href="#case-in_game_journey-922fbc0382e28fbd3b03">[ ] unverified</a> |
| **Journey**<br>Service: ghsr; role: primary; journey: 7:Bin>Nout; entry: Bin; exit: Nout | — | <a href="#case-in_game_journey-1a292acab446527dc81d">[ ] unverified</a> | <a href="#case-in_game_journey-23be41d99304c2c01627">[ ] unverified</a> | <a href="#case-in_game_journey-56f8b9227125c1af820d">[ ] unverified</a> | <a href="#case-in_game_journey-c44ac39cf9c3e537c7ef">[ ] unverified</a> |


<details>
<summary>Journey — Service: ghsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout</summary>

<a id="case-in_game_journey-4e75f983e04a39cb9208"></a>

**0° CCW: unverified** — `in_game_journey-4e75f983e04a39cb9208`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

<a id="case-in_game_journey-26af7182ff9386e8b7b6"></a>

**90° CCW: unverified** — `in_game_journey-26af7182ff9386e8b7b6`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

<a id="case-in_game_journey-503c9989f019a3663a85"></a>

**180° CCW: unverified** — `in_game_journey-503c9989f019a3663a85`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

<a id="case-in_game_journey-3ed61c264e6c4008c2a6"></a>

**270° CCW: unverified** — `in_game_journey-3ed61c264e6c4008c2a6`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

</details>


<details>
<summary>Journey — Service: ghsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout</summary>

<a id="case-in_game_journey-ef4eccd47d5f2cb459a8"></a>

**0° CCW: unverified** — `in_game_journey-ef4eccd47d5f2cb459a8`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-acaad059037c450d967b"></a>

**90° CCW: unverified** — `in_game_journey-acaad059037c450d967b`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-34bbeb558ea55173d402"></a>

**180° CCW: unverified** — `in_game_journey-34bbeb558ea55173d402`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-922fbc0382e28fbd3b03"></a>

**270° CCW: unverified** — `in_game_journey-922fbc0382e28fbd3b03`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

</details>


<details>
<summary>Journey — Service: ghsr; role: primary; journey: 7:Bin>Nout; entry: Bin; exit: Nout</summary>

<a id="case-in_game_journey-1a292acab446527dc81d"></a>

**0° CCW: unverified** — `in_game_journey-1a292acab446527dc81d`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:Bin>Nout; entry: Bin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-23be41d99304c2c01627"></a>

**90° CCW: unverified** — `in_game_journey-23be41d99304c2c01627`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:Bin>Nout; entry: Bin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-56f8b9227125c1af820d"></a>

**180° CCW: unverified** — `in_game_journey-56f8b9227125c1af820d`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:Bin>Nout; entry: Bin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-c44ac39cf9c3e537c7ef"></a>

**270° CCW: unverified** — `in_game_journey-c44ac39cf9c3e537c7ef`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:Bin>Nout; entry: Bin; exit: Nout.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — ghsr → ghsr — 12 cases; unverified: 12</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: Nin; to port: Nout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7cd132ec06d8123f2690">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f2921838abaf1b00b7b4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1848f8114308d7b790c2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6f96a6bf7e339e49ebea">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Sin; to port: Sout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-aa00c7e26402533623cc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7990ff2aa6601618350a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3b6f54dd21dc19319c84">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-21abb02b4aeb039df0ad">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Bin; to port: Sout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-119be118bb9b46058114">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-099af6b20a620107f5dd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6a9156a25bce6d348d71">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-04ba4801bd2050535fe2">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: Nin; to port: Nout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7cd132ec06d8123f2690"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7cd132ec06d8123f2690`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f2921838abaf1b00b7b4"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f2921838abaf1b00b7b4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1848f8114308d7b790c2"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1848f8114308d7b790c2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6f96a6bf7e339e49ebea"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-6f96a6bf7e339e49ebea`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Sin; to port: Sout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-aa00c7e26402533623cc"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-aa00c7e26402533623cc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7990ff2aa6601618350a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7990ff2aa6601618350a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3b6f54dd21dc19319c84"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3b6f54dd21dc19319c84`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-21abb02b4aeb039df0ad"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-21abb02b4aeb039df0ad`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Bin; to port: Sout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-119be118bb9b46058114"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-119be118bb9b46058114`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Bin; to port: Sout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-099af6b20a620107f5dd"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-099af6b20a620107f5dd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Bin; to port: Sout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6a9156a25bce6d348d71"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6a9156a25bce6d348d71`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Bin; to port: Sout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-04ba4801bd2050535fe2"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-04ba4801bd2050535fe2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Bin; to port: Sout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->
