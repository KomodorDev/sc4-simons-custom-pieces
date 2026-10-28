---
title: "Piece and assembly naming conventions"
summary: "Choose stable folder identifiers and consistent readable names for pieces and assemblies, and coordinate deliberate changes without altering game identities or historical evidence."
audience: "Piece authors, assembly designers, maintainers, and coding agents"
document_type: "reference"
---

# Piece and assembly naming conventions

<!-- BEGIN DOCUMENT NAVIGATION -->
[1. Names and their authoritative sources](#1-names-and-their-authoritative-sources) · [2. Facts to establish before choosing either name](#2-facts-to-establish-before-choosing-either-name) · [3. Folder spelling and uniqueness](#3-folder-spelling-and-uniqueness) · [4. Piece folder pattern](#4-piece-folder-pattern) · [5. Assembly folder pattern](#5-assembly-folder-pattern) · [6. Readable name pattern](#6-readable-name-pattern) · [7. Assembly display names and height summaries](#7-assembly-display-names-and-height-summaries) · [8. Examples of the complete convention](#8-examples-of-the-complete-convention) · [9. Presentation and current software behavior](#9-presentation-and-current-software-behavior) · [10. Choosing and changing names](#10-choosing-and-changing-names)
<!-- END DOCUMENT NAVIGATION -->

Use descriptive, stable folder names to identify source files, and consistent readable names to help players choose the correct piece or assembly. Both names describe the same subject, but they have different formatting and maintenance rules. These conventions apply across transport domains; the owning network specification supplies the actual network names, levels, permissions, and profiles.

Apply the rules when creating a new subject or deliberately revising its readable name. Existing folders and IDs remain stable, including historical words in their spelling. Adopting this reference does not rename the catalogue, regenerate artwork, or change the software's validation rules. Bounded training examples in the creation workflows retain their explicitly identified placeholder names.

<a id="names-and-their-authoritative-sources"></a>

## 1. Names and their authoritative sources

A **piece** is one reusable construction type. An **assembly** is a documented layout containing placed copies of pieces. A **placement** is one such copy. An **identifier**, or **ID**, is exact text used to find a subject in commands and project data. A **slug** is an ID written with lowercase words separated by hyphens. A **canonical name** is the authoritative readable name from which presentations should be made.

| Name or identifier | Piece source | Assembly source | Purpose |
| --- | --- | --- | --- |
| Folder slug and internal ID | `piece.json` field `id`; the enclosing folder must match it exactly | The folder containing registered `assembly.json`; its basename becomes the ID | Stable selection and file location |
| Canonical readable name | `piece.json` field `name` | `assembly.json` field `title` | Describe the subject to a person |
| Picture heading | Shared renderer adds `Piece - ` and source-backed height formatting | Owning renderer adds `Assembly - ` | Identify the kind of subject and its readable name |
| Installed menu title | Domain menu generator adds the SCP prefix, badge, and applicable design-review warning to the registered piece name | Domain `menu-layout.jsonc`, under `layouts.<layout-key>.cycle_button.title` | Present the subject in the game menu |
| Placement label | Not part of a reusable type's identity | The assembly's recorded labels, such as `P01` | Distinguish copies and positions in one layout |

The required source locations, relative to `custom-pieces/`, are:

```text
domains/<domain>/00_pieces/<piece-id>/piece.json
domains/<domain>/01_assemblies/<assembly-id>/assembly.json
```

Do not add an assembly `id` field merely to imitate a piece definition. The current catalogue derives that ID from the folder. The menu layout key, such as `trumpet`, is a separate selector and can differ from the assembly ID, such as `straight-stem-trumpet`.

Game-resource numbers, a recipe's Python identifier, connector-group IDs, and placement labels are separate identities. A readable-name change does not justify changing them. See [structure and ownership](../STRUCTURE.md#5-source-and-data-ownership) for the full source map.

<a id="facts-to-establish-before-choosing-either-name"></a>

## 2. Facts to establish before choosing either name

Read the subject definition, its measured connection records, and its owning network specification. Establish the network services, nominal levels, measured heights, physical track or lane arrangement, permitted directions, function, geometry, and distinguishing physical profile. A **profile** describes the physical section at a connection, including features such as the deck and structural web. A **nominal level** is a named height category; a measured path height is the actual vertical position of the traffic route in metres.

Keep physical arrangement and traffic permission separate. `Two-Track` counts physical tracks. `One-Way` describes permitted movement. In the reviewed HSR paired family, two tracks carry opposite directions, but that is a source fact about that family rather than a universal meaning of two tracks. A pedestrian mode does not create another road lane, and two directed path records do not necessarily describe two physical tracks. Use the [connector definitions](CONNECTOR_METADATA.md#1-a-connection-is-agreement-at-the-shared-edge).

The [HSR specification](../domains/high-speed-rail/NETWORK_SPEC.md#2-connection-levels-and-piece-families) provides worked examples: Level 2 rail paths are at 15.5 m, Level 4 paths are at 30.5 m, and the tight paired corner has an explicitly unassigned nominal level at its Custom (23 m) joint. A different narrow rail family uses Level 3 at 23 m. Preserve those distinct classifications. The 1 m GHSR ground path and the 0 m ordinary Road path are also different facts.

Use a reviewed network service name, such as `HSR`, `GHSR`, `Road`, or `Tram`. A shared engine traffic class does not make those services interchangeable. Put the detailed channel positions, running convention, slope, spacing, modes, permissions, and connection limits in the connection cards and subject documents. The name contains the facts needed to distinguish and select the subject; the cards retain the complete connection contract.

<a id="folder-spelling-and-uniqueness"></a>

## 3. Folder spelling and uniqueness

For every new piece or assembly slug:

1. Use 2–64 characters in total, including hyphens. Start with a lowercase English letter. Use only lowercase ASCII letters `a`–`z`, digits `0`–`9`, and single hyphens between words.
2. Keep at least one letter or digit in each word. Do not use spaces, underscores, accented characters, punctuation, doubled hyphens, or a trailing hyphen. Use `90deg`, rather than `90°`, and a documented custom-height token, rather than a decimal point.
3. Make piece IDs unique across all domains. Also make assembly IDs unique across all domains; several tools select assemblies by ID without a domain qualifier. Check both registries and existing subject folders before allocating one. Do not rely on different capitalization to distinguish either IDs or readable names.
4. Avoid operating-system reserved names, including `con`, `prn`, `aux`, `nul`, `com1`–`com9`, and `lpt1`–`lpt9`. Keep the complete checkout path manageable, including the enclosing directories; 64 characters is a slug limit rather than a guarantee about every possible full path.
5. Use a functional name. Exclude personal names, dates, temporary task names, test results, and historical suffixes such as `new`, `final`, `fixed`, `revised`, `v2`, or `copy`. Distinguish concurrently maintained designs by their actual function or profile.
6. Leave `piece`, `assembly`, `component`, and `interchange` out when they merely repeat the enclosing folder's classification. Do not add sequence numbers or assembly placement labels, such as `p01`, to reusable piece IDs.

The stricter spelling convention is equivalent to `^[a-z](?:[a-z0-9]|-[a-z0-9])+$`, with the separate 2–64-character limit. A **regular expression** is a pattern for checking text. The current piece validator and scaffold use the looser `[a-z][a-z0-9-]{1,63}` pattern, which also accepts some doubled or trailing hyphens. The stricter convention is an authoring rule; it is not an assertion that every legacy ID has been migrated or that all assembly IDs are already checked in software.

<a id="piece-folder-pattern"></a>

## 4. Piece folder pattern

Use this order for a newly allocated piece ID. Angle brackets indicate a value to supply; square brackets indicate an optional part, rather than literal characters to type.

```text
<network-and-levels>-<arrangement>-<function>[-<geometry>][-<variant>]
```

| Part | Rule and examples |
| --- | --- |
| Network and levels | Start with the service and its declared connection level: `hsr-l2`, `hsr-l4`, `road-l0`, or a domain-defined ground form such as `ghsr-ground`. Include both services where the piece contains different networks. |
| Level relationship | Use `-to-` for an established one-way transition, `-and-` for multiple connection heights without a one-way assertion, and `-over-` for upper and lower separated routes. Examples: `hsr-l2-to-l4`, `hsr-l2-and-l4`, and `hsr-l4-over-hsr-l2`. Repeat the network token across `over` to make ownership explicit. |
| Unassigned custom height | Use `h` followed by the exact height in whole millimetres and `mm`: `h23000mm` means 23 m with no assigned nominal level. For a negative height, insert `neg`: `hneg15000mm` means −15 m. Thus `hsr-h23000mm-and-l4` identifies the custom/Level 4 combination. Do not round a measurement to fit this token; use `custom-<documented-profile-token>` instead if exact millimetres cannot express the distinguishing height. |
| Arrangement | Use `two-track`, `single-track`, or `single-track-oneway` for rail. Use `two-track-mainline` where only the mainline has that count. Use `mixed` when the piece combines different networks or arrangements that need separate descriptions. Other domains define accurate equivalents, such as a lane count, from their own sources. |
| Function | Use the controlled functional vocabulary below: for example, `straight`, `curve`, `ramp`, `split`, `merge`, `crossing`, or `adapter`. |
| Geometry | Include alignment, angle, handedness, and a partial-shape qualifier when they distinguish types, in that order. Examples: `diagonal`, `90deg-right`, and `diagonal-north-half`. |
| Variant | Add a necessary physical or geometric distinction, such as `compact`, `wide`, `tight`, or `recessed-web`. Use the documented family term; these words are not interchangeable. |

For an undirected `and` height pair, list heights from lowest to highest measured path height. For `to`, list entry before exit, even when the route descends. For `over`, list the physically upper route before the lower one. Names with more than two levels must express their actual relationship; an unordered list does not assert journeys between every pair.

Include enough information to distinguish the type without copying every measurement into the ID. If the complete candidate exceeds 64 characters, first remove redundant wording and move non-distinguishing detail to the description. Use a shorter, documented domain profile token only when the full meaning remains unambiguous. Do not truncate an ID, omit a required difference, or append an arbitrary number to bypass a collision.

<a id="assembly-folder-pattern"></a>

## 5. Assembly folder pattern

Use this order for a new assembly:

```text
<network-or-networks>-<layout>[-<variant>]
```

Use the established layout name, such as `trumpet`, followed by a meaningful variant, such as `straight-stem`: `hsr-trumpet-straight-stem`. Join multiple services with `-and-`, in a stable domain-defined order, when they are important to the layout's identity. Do not list every component, placement label, rotation, or construction step in the assembly slug.

Include an explicitly qualified interface difference only when it distinguishes two maintained assemblies. For example, an `external-l2` variant identifies external connection level, whereas an unqualified `l2` could incorrectly suggest that all internal routes stay at that level. Keep the full outside-connection and internal-height summaries in the assembly's description. A different placement rotation of the same complete design does not create a new assembly ID.

The existing `straight-stem-trumpet` assembly keeps its current ID. The network-prefixed form above is the rule for new allocation, not a request to relocate that assembly.

<a id="readable-name-pattern"></a>

## 6. Readable name pattern

Use the following canonical readable forms. Keep the piece's whole name in `piece.json.name`, and the assembly's whole name in `assembly.json.title`.

```text
<Network and connection levels> — <Arrangement and function> — <Necessary variant>
<Network or networks> — <Assembly layout> — <Necessary variant>
```

Omit the final separator and variant when no variant is necessary. Use one space on each side of the em dash `—`. Write recognised acronyms, such as `HSR`, in capitals; write function words in title case, such as `Two-Track Straight`. Use lowercase connecting words, such as `to`, `from`, `over`, `and`, and `with`, within a phrase. Use `Level 2`, rather than `L2`, in readable source names. These names are labels; ordinary explanatory sentences retain normal sentence capitalization.

Store each canonical name as one nonempty line, with single spaces between words, no leading or trailing whitespace, and no sentence-ending punctuation. Do not include tabs, line breaks, control characters, or presentation markup such as Markdown links, HTML, or bold markers. These are authoring rules; the current catalogue validator does not enforce all of them.

Use `Two-Track` consistently in new canonical names rather than alternating it with `Paired`. Explain the current family's opposite-direction operation in its description and cards. Where a single track is also one-way, say `Single-Track One-Way`. Name a mixed branch by its actual role, such as `Split from Two-Track Mainline` or `Merge to Two-Track Mainline`; describe its branch permissions separately. Do not apply `One-Way` to an entire two-way-mainline piece because its branch is one-way.

For a `Two-Track Crossing`, the count qualifies each crossing alignment: two tracks on one route cross two tracks on the other, giving four physical tracks altogether. Use that short form only when both alignments have the same arrangement. For mixed counts, qualify the routes individually, for example `Two-Track over Single-Track Crossing`, and use `mixed` in the arrangement part of a new folder ID. Retain each route's permissions and channel counts in the cards.

Piece names must remain unique across the library without relying on letter case. Apply the same uniqueness rule to canonical assembly names as an authoring convention. A repeated copy of one piece retains its type name; only its placement label changes. A new name must not imply that a piece belongs exclusively to the first assembly that uses it.

<a id="levels-and-measured-heights"></a>

### 6.1 Levels and measured heights

The complete displayed level form is `Level 2 (15.5 m)`. For an unassigned nominal level, use `Custom (23 m)`. Use a decimal point, a space before `m`, and no unnecessary trailing zeros: `23 m`, rather than `23.0 Metres`. Retain precision needed to distinguish the actual interfaces; do not invent or round a height merely to make a label shorter. These values identify traffic-path height, rather than deck-top height, underside clearance, or a promise of compatibility.

Use measured, source-backed height annotations in a new or deliberately migrated canonical name. When the renderer normalizes or supplies those annotations, derive them from the same verified connection records and show each named level and height once. Keep custom classification as well as the number: a 23 m custom end must not acquire a Level 3 label through numerical resemblance. If required facts are missing, leave the subject's deliberate naming migration pending until they are established; do not replace them with a guessed level.

| Relationship | Display rule | Meaning |
| --- | --- | --- |
| One connection level | `HSR Level 2 (15.5 m)` | Identifies the declared connection height; internal curves or gradients still require their own description. |
| One-way height transition | `HSR Level 2 (15.5 m) → Level 4 (30.5 m)` | The declared journey travels from the first end to the second. |
| Height transition with journeys both ways | `HSR Level 2 (15.5 m) ↔ Level 4 (30.5 m)` | The piece provides travel between those heights in both directions. |
| Several heights without that journey assertion | Write the relevant levels with `and`, or use a concise function name and a separate qualified summary | Exposing several heights does not establish all movements between them. |
| Separate crossing routes | `HSR Level 4 (30.5 m) over HSR Level 2 (15.5 m)` | The upper and lower routes have that vertical relationship; the name does not authorize a transfer. |
| Different networks | `HSR Level 2 (15.5 m) over Road Level 0 (0 m)` | Attach each level to its own service, and retain additional required groups, such as pedestrians, in the cards. |

Use the same ascending-height order as folder `and` expressions for `↔`. A paired ramp carries an ascent and a descent, so prefer `Ramp` to an unqualified `Climb` or `Descent`. The arrows describe established travel, rather than the direction in which the player rotates or places the piece. If an interface's grade differs from the interior route, retain that distinction in the cards.

<a id="function-and-geometry-vocabulary"></a>

### 6.2 Function and geometry vocabulary

| Term | Use it for |
| --- | --- |
| Straight | A route with unchanged plan-view heading. Use `Diagonal Straight` when it follows the diagonal grid alignment. |
| Curve | A route that changes heading. Use `Curve 90°`, rather than mixing `Corner`, `Quarter-Turn`, `Turn90`, and `90 Degree Curve`, when adopting the new convention. |
| S-Curve | A sideways shift whose entrance and exit retain the same heading. A zero net heading change does not make it a straight. |
| Ramp | A height-changing route. Use `Curve 90° Ramp` when both the heading change and height transition distinguish it. |
| Transition | A source-defined change between different network or geometric families; explain whether it also changes height. Keep an established domain-specific meaning when it differs from a simple ramp. |
| Split and Merge | A branch departing from, or joining, the stated mainline. Preserve the source's directed distinction. |
| Crossing | Routes crossing in plan view. State `over` for separated levels, and `At Grade` for an established same-height crossing. State transfer permissions in the description and cards. |
| Crossover and Scissors | Distinct transfer arrangements between neighbouring mainlines. Preserve their actual route topology rather than treating them as generic crossings. |
| Adapter | A source-defined change in width, spacing, or physical connection profile. A profile adapter does not automatically change height. |
| Fan, T Junction, and other domain terms | A documented functional arrangement whose routes justify the term. Extend this vocabulary in the owning domain when a new function needs a precise name. |

State an angle in degrees as `45°`, `90°`, or `135°` in readable names, and `45deg`, `90deg`, or `135deg` in slugs. For a curve or branch, this is the declared change in heading; for a crossing, it is the angle between the crossing alignments. Specify which measurement the family uses. Do not substitute a curve radius, diagonal alignment, or camera angle for the route angle.

State `Left` or `Right` only when it distinguishes a real type and has a defined reference. For one-way curves, use the vehicle's direction of travel. For a split, use the mainline's reference travel direction; for a merge, use the declared reference approach into the merge. For two-way curves or other symmetric movements, record the reference approach in the subject's placement instructions and canonical 0° view. If no unique reference has been established, resolve it before adding handedness; do not infer it from a missing `left` suffix in an old ID. Physical rotation preserves the name, and reflection requires its own route and geometry checks before it can identify a distinct type or supported orientation.

Use cardinal directions in a reusable name only when they identify intrinsic authored geometry, such as a `North Half` or `East Half` diagonal in the canonical 0° orientation. Explain that frame in the README. A half-diagonal is a specific complementary shape, not half a track's width or half its traffic permissions. A current assembly role such as `West Approach` belongs to the placement description, not the reusable piece name.

<a id="variants-and-dimensions"></a>

### 6.3 Variants and dimensions

Keep `Compact`, `Wide`, `Tight`, and `Standard` only when the owning family defines their geometric or physical differences. Do not rename `Tight` to `Compact` merely to reduce the vocabulary. Retain profile distinctions such as `Recessed Web` when they change physical fit. Prefer these current properties over historical comparisons such as `Shortened`, `Revised`, or `Improved`.

If a dimension is necessary to distinguish a type, identify what it measures. Write `8 m Deck Width`, rather than `Eight-Metre Straight`, when 8 m describes the slab width. State `1-Tile Footprint` or `2 × 3-Tile Bounding Rectangle` when that information is the relevant distinction. An occupied tile count, a bounding rectangle, and a cleared construction area are different quantities; otherwise keep those dimensions in the description. Use `width8m` or another explicitly documented quantity token in a slug only when that dimension is needed for uniqueness.

Use one canonical word for each reviewed property, and retain all differences needed to distinguish concurrently maintained types. If two subjects still receive the same name, inspect their actual functional or profile difference. Add that difference to both the readable name and a newly allocated slug where appropriate; do not invent a counter or revision label.

<a id="assembly-display-names-and-height-summaries"></a>

## 7. Assembly display names and height summaries

Name the complete layout rather than one component: `HSR — Trumpet — Straight Stem`. Add `Assembly - ` only in the presentation that calls for it. Keep its actual external services and connection levels in an explicitly qualified summary. List internal levels separately so the player can distinguish what connects outside from what rises inside.

For the existing trumpet, a convention-form display example is:

```text
Assembly - HSR — Trumpet — Straight Stem
External connections: HSR Level 2 (15.5 m).
Internal routes also use Level 4 (30.5 m) and Custom (23 m).
```

This example does not rename the current registered title or menu button. When two maintained assemblies need their external levels in their names to distinguish them, use an explicit variant such as `External Connections Level 2 (15.5 m)`. Do not use a bare `Level 2` label for a multilevel layout. List exact arm-by-arm interfaces, quantities, dimensions, and component order in the assembly's existing README and connection records.

<a id="examples-of-the-complete-convention"></a>

## 8. Examples of the complete convention

These examples illustrate candidate names for new allocation or a separately authorized migration. They do not register additional copies of existing types, and they do not replace existing folder IDs automatically. Each assumes its named geometry and permissions have been established.

| Kind | Convention-form folder slug | Complete displayed heading |
| --- | --- | --- |
| Piece | `hsr-l2-two-track-straight` | `Piece - HSR Level 2 (15.5 m) — Two-Track Straight` |
| Piece | `hsr-l2-two-track-straight-recessed-web` | `Piece - HSR Level 2 (15.5 m) — Two-Track Straight — Recessed Web` |
| Piece | `hsr-l2-and-l4-two-track-ramp` | `Piece - HSR Level 2 (15.5 m) ↔ Level 4 (30.5 m) — Two-Track Ramp` |
| Piece | `hsr-h23000mm-and-l4-two-track-curve-ramp-90deg-tight` | `Piece - HSR Custom (23 m) ↔ Level 4 (30.5 m) — Two-Track Curve 90° Ramp — Tight` |
| Piece | `hsr-l4-over-hsr-l2-two-track-crossing-90deg` | `Piece - HSR Level 4 (30.5 m) over HSR Level 2 (15.5 m) — Two-Track Crossing 90°` |
| Piece | `hsr-l2-over-road-l0-mixed-parallel-stack` | `Piece - HSR Level 2 (15.5 m) over Road Level 0 (0 m) — Parallel Stack` |
| Piece | `hsr-l2-single-track-oneway-curve-90deg-right-wide` | `Piece - HSR Level 2 (15.5 m) — Single-Track One-Way Curve 90° Right — Wide` |
| Piece | `hsr-l2-two-track-mainline-split-45deg-right-wide` | `Piece - HSR Level 2 (15.5 m) — Split 45° Right from Two-Track Mainline — Wide` |
| Assembly | `hsr-trumpet-straight-stem` | `Assembly - HSR — Trumpet — Straight Stem` |

An existing straight provides the separate identity example: its folder and ID remain `hsr-component-lower-paired-straight` even if a future readable-name migration gives it `HSR Level 2 (15.5 m) — Two-Track Straight`. An existing historical token is not a reason to change an allocated ID.

<a id="presentation-and-current-software-behavior"></a>

## 9. Presentation and current software behavior

Keep `Piece - `, `Assembly - `, `SCP`, menu badges, and current review warnings outside the canonical name stored in `name` or `title`. Each owning presentation adds its required prefix exactly once. View purpose, such as `Clean view` or `Connection overview`, camera direction, coordinate grid, and software-preview identification belong in the other caption rows defined by [documentation generation](WORKFLOW_DOCUMENTATION_GENERATION.md#6-reusable-names-and-standalone-type-pictures). Game-test status stays in the generated matrix and testing records.

Use the same canonical descriptive words across current guides, inventories, component lists, and pictures. Height normalization and required context prefixes are presentation transformations. They must not become independent editorial names for the same type. When a current assembly placement stores a copied `name` or `menu_name`, update that copy alongside a deliberate source-name change; the assembly renderer checks explicit menu names against the registered piece name.

Current software has narrower behavior than this authoring policy. [The shared picture-title helper](../framework/scp/render_headers.py) normalizes level shorthand and measured-height annotations, and contains special title wording for the tight Level 4/custom corner and modular crossing. Assembly menu titles are separately stored. Existing registration tools generally preserve registered manifests, while their recipe names and presentation functions supply names for newly created entries. Adopting the convention requires coordinating those actual producers when their subjects are intentionally migrated; a documentation update alone does not remove the exceptions or generate all names from one new naming engine.

The 64-character rule applies to IDs, not readable names. Do not invent an equivalent display-name limit. Prefer names that stay legible at the actual delivered picture and menu size. Shared picture headers shrink to fit and fail if the text still exceeds the available width; inspect the resulting image rather than treating a successful text edit as a layout check. Menu text encoding accepts Unicode, but visible support for arrows, degree signs, and em dashes requires checking the intended game environment. If a target needs text equivalents, format `→` as `to`, `↔` as `between … and …`, `°` as `degrees`, and `—` as ` | ` in that presentation, while preserving the canonical source name and recording the rendering choice.

<a id="choosing-and-changing-names"></a>

## 10. Choosing and changing names

For a new subject:

1. Decide whether it is one reusable piece or an assembly using the [piece-versus-assembly decision](WORKFLOW_PIECE_CREATION.md#1-decide-between-a-piece-and-an-assembly). Choose its owning domain.
2. Open that domain's `domain.jsonc`, piece inventory, assembly inventory, and network specification where implemented. Look for an existing reusable type before reserving another ID. Check candidate IDs and readable names across every domain, including names that differ only in capitalization.
3. Establish the facts listed above, choose the folder slug using the appropriate pattern, and count its complete 2–64-character length. Choose its canonical readable name independently using the same factual vocabulary.
4. For a piece, use the [scaffold and allocation workflow](WORKFLOW_PIECE_CREATION.md#3-create-a-draft-and-allocate-its-local-identifiers), keeping folder and `id` identical. For an assembly, follow [assembly registration](WORKFLOW_ASSEMBLY_CREATION.md#12-start-a-small-hsr-assembly-from-existing-pieces), using the folder basename as ID and `title` as the readable name. A scaffold's placeholder name must be completed before presenting a finished subject.
5. Follow [documentation generation](WORKFLOW_DOCUMENTATION_GENERATION.md) for source-backed names, cards, guides, artwork, and exports. Inspect the exact rendered headings and menu title within the supported verification scope.

For a deliberate readable-name change, record an old-name → new-name mapping keyed by the unchanged ID in the change description. Edit the owning definition and every current copied label or name-producing source that applies. Refresh the selected generated views through their documented workflow. A source-name edit can require a fresh build because menu text changes and preview generation compares the current definition with the build manifest, even when geometry is unchanged. Preserve original frozen artifacts and their recorded names and hashes; inspect a newly generated artifact under its actual source version.

A folder or ID change is a separate migration, not an ordinary display-name edit. It requires an explicit scope that includes that identity change. Before moving anything, enumerate the registry paths, allocation-ledger keys, collections, recipe dispatch references where relevant, assembly placements, menu-layout references, build selections, subject links, generated exports, resource filenames, and observation dependencies that use the old identity. Keep permanent numeric game IDs, construction coordinates, and accepted geometry unchanged unless a separately authorized functional change requires new allocation. Confirm how saved resources and tooling references will continue to resolve. Do not leave a half-renamed subject or create a replacement type merely to improve an old folder's wording.

Only explicit matching human observations can establish game-test results. Preserve observation records and their original evidence when changing names. If changed source fingerprints make a result stale, retain that state and use the existing [observation workflow](TESTING.md#5-data-ownership-and-stale-evidence); never edit old fingerprints to manufacture a current pass. Frozen evidence, imported materials, and original backup snapshots retain their recorded names.

Run these commands from the repository root after changing the maintained naming rules or applying an authorized migration:

```sh
python3 -B custom-pieces/scp.py docs-check
python3 -B tools/run_tests.py
git diff --check
```

Review the documentation errors, explicit test skips, and complete diff. `docs-check` checks current document structure and local links; it does not enforce this complete naming vocabulary. The test runner checks the framework, registered domains, and registered assemblies, and does not supply a new game observation. Building, installing, publishing, and human pull-request merging remain separate operations under the [repository workflow](https://github.com/KomodorDev/sc4-simons-custom-pieces/blob/dev/docs/GITHUB.md).
