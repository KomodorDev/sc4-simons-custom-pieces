---
title: "Public release requirements and controller maintenance"
summary: "Explain the evidence, permissions and identifier requirements for a publishable release."
audience: "Maintainers and release authors"
document_type: "reference"
---

# Public release requirements and controller maintenance

Research checked on **18 October 2026**. This document distinguishes statements found in the sources from release practices recommended for this project. It does not grant permission, reserve identifiers, or claim that a prototype has passed an in-game test.

## Current release status

The existing pieces are **private experimental builds**. A public binary release is not cleared by the permission evidence currently recorded here. Local development, reproducible builds, and preparation of a review package can continue while those release questions remain open.

Current compiled piece DATs contain copied or adapted NAM models, paths, and effects. A selected build has one separate controller DAT containing the complete **RUL0 resource** and the **NetworkINI resource**, with additions, plus one separate menu DAT. It does not copy every resource from the original `NetworkAddonMod_Controller.dat` archive. An old staged ZIP is not a prerequisite for preparing or assessing a fresh candidate.

Definitions:

- **DAT / DBPF:** the archive format used to package SimCity 4 resources.
- **Resource:** one item inside that archive, such as a model or rule file.
- **TGI:** the Type, Group, and Instance numbers identifying a resource.
- **IID:** its Instance ID. Reusing an IID can be intentional for related models, paths, and exemplars, but unrelated resources with the same complete TGI conflict.
- **RUL0:** the shared construction rules that define selectable puzzle pieces.
- **NetworkINI:** shared network settings, including selection of shadow images.
- **Overlay:** a replacement resource with the same TGI as an existing one.

## Permission evidence: what was actually found

| Source inspected | Observation | Consequence for this project |
| --- | --- | --- |
| NAM's [installer `license.txt`](https://github.com/NAMTeam/Network-Addon-Mod/blob/staging/src/scripts/installer-resources/license.txt), also present in the local source checkout | Contains compatibility requirements, installation directions, and a liability disclaimer. No general redistribution or derivative-work grant was found in this file. | Do not treat accepting the installer disclaimer as recorded permission to publish retained NAM assets. |
| [NAM source repository](https://github.com/NAMTeam/Network-Addon-Mod) | On the checked `staging` tree, the installer file above was the only license-named file found. GitHub's repository metadata reported `license: null`. | Public source availability is not sufficient evidence for the release gate defined below. The precise observation is that no applicable grant has been recorded, not a legal conclusion that all reuse is forbidden. |
| [Official NAM FAQ](https://www.sc4nam.com/docs/getting-started/frequently-asked-questions/#i-want-to-use-an-older-version-of-the-nam-where-can-i-download-previous-versions) | The team states that users and sites may not redistribute old NAM versions. | A binary containing old controller resources needs an update/withdrawal policy and clarification of the permission covering those resources. The FAQ does not specifically decide the status of this custom derivative. |
| [NAM DLL guide](https://www.sc4nam.com/docs/feature-guides/nam-dll/#overview) | Specifies LGPL-3 for the NAM DLL. | This statement concerns the DLL; it does not establish the license for the NAM models, paths, effects, or controller data used by these pieces. |
| [STEX Code of Conduct, staff posts](https://community.simtropolis.com/forums/topic/66427-stex-code-of-conduct/) | Requires original or explicitly permission-given uploads. | Retained donor content requires an applicable permission record or a documented exception from the site's staff before a STEX binary release. Credit alone does not satisfy the stated rule. |

**Recommended permission record:** for every externally authored component, record the original author/team, source URL, source version, resource TGIs, the modification made, the permission or license relied on, the evidence location, its scope, and any attribution or distribution conditions. Cover models, textures, paths, effects, copied rule templates, and complete overlaid resources separately where the scope differs. An unanswered request is not an approval. No message has been sent and no permission is claimed by this audit.

One possible future distribution is a builder that reads the user's own NAM installation and produces an overlay locally. This avoids shipping the copied binary resources themselves. It does not automatically resolve permission questions for any copied source text or templates included with the builder. Another route is an accepted NAM contribution; the [official FAQ invites prospective contributors to show a prototype](https://www.sc4nam.com/docs/getting-started/frequently-asked-questions/#id-like-to-contribute-to-the-nam-how-do-i-do-so).

## Identifier reservation before public release

The [original puzzle-piece tutorial](https://community.simtropolis.com/omnibus/simcity-4/modding-information/how-to-create-puzzle-pieces-part-1-r199/) describes reserving resource IIDs and construction identifiers project by project. It also identifies preview effect names as a separate uniqueness concern. This is historical primary guidance, not confirmation that its linked reservation contacts or all numerical ranges are current.

Recommended steps:

1. Inventory the complete set needed by the release: tile IIDs, all five model zoom IIDs where present, preview IIDs, path/exemplar/label IIDs, and shadow IIDs if new shadow images are supplied.
2. List every **H3ID**, meaning the identifier of a `HighwayIntersectionInfo` construction-rule section, including rotation and mirror variants and any menu-slot clones.
3. List every new preview effect name as well as its resource TGI.
4. Obtain a documented allocation or confirmation from the relevant current NAM identifier maintainer. A general lot-texture allocation is not evidence of allocation inside an HSR network range.
5. Scan the installed resources and the complete intended combined build for duplicate TGIs, H3IDs, and effect names. Record the inspected folders and any folders that could not be inspected.
6. Mark the allocation as **confirmed** only after its evidence is recorded. A successful local scan means only that the inspected installation has no detected collision. It does not reserve the numbers globally.

The experimental `5DD0F1xx`, `5DD0F2xx`, `F7A0`, and `F7A1` identifiers must remain marked **unreserved** unless later evidence changes that status. Assign final identifiers before public release. After release, keep published tile identifiers stable or provide a documented migration/compatibility plan: existing cities can still refer to them.

The [NAM technical-information page](https://www.sc4nam.com/docs/reference/technical-information/#7-nam-id-conventions) describes network and path-ID conventions but explicitly labels itself out of date. Its left-hand-drive discussion is a reason to audit the installed INI's actual conversion rules and test each supported drive side, rather than assume that a right-hand-drive build supports both sides.

## Combined-controller evidence for release

A public package must contain the single combined controller required by the [controller composition and verification contract](FRAMEWORK_ENGINEERING.md#controller-composition-and-verification). Its release evidence must identify the clean base and final controller hashes, scanned loading roots, competing-overlay checks, exact native-byte restoration, and saved-rule verification for the complete selected set. Keep observed rotation and traffic results separate from those static checks. Controller implementation and integration rules live in that engineering contract; the release gates below assess their evidence.

## Gates for a public package

These are **recommended project gates**, except where a site requirement is explicitly identified. A private experimental build can be prepared without claiming that the public-release gates have passed.

| Gate | Evidence needed to mark it passed |
| --- | --- |
| Permission | Applicable license or explicit permission evidence covering every retained external component and any redistributed complete controller resources. |
| Allocation | Confirmed network/resource and construction-ID allocation, plus collision results and preview-name checks. |
| Compatibility | Exact supported NAM/controller fingerprints, game edition, DLL requirements, drive side, and any required optional NAM asset packages. Unsupported variants are named. |
| Static verification | Results tied to the exact release DAT hash, including all combined-controller checks. |
| In-game verification | Actual game build, loaded add-ons, tester/date, and evidence of menu selection, all distinct rotations/mirrors, all connection ends, both directions on both lines, no unintended transfers, shadows, zooms, save/reopen, and removal. Test actual passenger demand when checking route query. |
| Installation and removal | Instructions tested on a clean supported profile, competing overlays handled, upgrades tested, and removal instructions explain how to remove placed pieces before their resources disappear. |
| Packaging | Final archive tested, members listed, DAT/archive hashes recorded, dependencies and credits included, and no private filesystem paths or private correspondence accidentally included. |
| Publication description | Accurate behavior, menu location, footprint, compatibility, dependencies, limitations, installation, removal, and support route. Do not label an experimental piece as game-tested without the evidence above. |

The [STEX staff rules](https://community.simtropolis.com/forums/topic/66427-stex-code-of-conduct/) specifically call for an archive, a meaningful description, and an in-game picture where applicable. A software model render is useful supplemental material, but is not an in-game screenshot. The located rules post dates from 2015 and includes a 25 MB limit; recheck the active upload form and current site requirements at publication time rather than treating that historical number as a guaranteed current limit.

Suggested metadata, regardless of the final file format:

```text
package_id; version; release_status; authors; credits; source_commit
selected_pieces; published_resource_ids; puzzle_ids; preview_effect_names
supported_game_builds; supported_nam_versions; supported_drive_sides
base_controller_sha256; base_resource_hashes; donor_resource_hashes
dependency_identifiers_and_versions; inventory_roots; unscanned_roots
permissions_status; permission_evidence_reference
identifier_allocation_status; allocation_evidence_reference
static_check_result_and_dat_hash; in_game_test_evidence_reference
known_issues; install_instructions; uninstall_instructions; upgrade_policy
archive_members; dat_sha256; archive_sha256; support_url
```

Publication approval and permission evidence are separate facts. A permission record does not publish anything. This workflow must not upload a file, send a message, or publish a listing merely because it can build a release archive.

## When NAM changes

1. Preserve the old build's manifest and test evidence. Remove its active shared overlay before using a replacement NAM controller; retaining the models and paths alone does not establish compatibility.
2. Read and fingerprint the new clean controller and donors. Inspect the new menu anchors, construction definitions, relevant path/conversion rules, and shadow mappings.
3. Reapply reviewed source additions to that new base. Do not edit the old generated RUL0 or only replace the accepted fingerprint in code.
4. Repeat the combined static checks and the supported in-game test matrix. Keep final published resource IDs stable unless a migration is provided.
5. Publish a new compatibility record only after the evidence passes. If an older public binary would continue shipping an obsolete NAM resource, follow its permission terms and the NAM distribution policy; obtain a clarification where those do not explicitly address the derivative.
6. Retain reproducible source additions and manifests for maintenance. Do not infer permission to host an old NAM release from the fact that a local backup exists.

## Build-specific game evidence

Each selected piece can reference a project-relative evidence JSON file with `"game_evidence": "evidence/hsr-diagonal-ghsr.json"` in its piece manifest. The release assessor requires the fields below. This is a **template with placeholders**, not test evidence:

```json
{
  "piece_id": "<exact piece id>",
  "asset_sha256": "<tested piece asset DAT hash from manifest.files>",
  "package_fingerprints": {
    "<every manifest.files path>": "<its exact sha256>"
  },
  "donor_fingerprints": {
    "<every manifest.profile.donors filename>": "<its exact sha256>"
  },
  "case_results": {
    "placement": "<recorded result>",
    "traffic_both_directions": "<recorded result>",
    "no_unwanted_transfers": "<recorded result>",
    "rotations_and_mirrors": "<recorded result>",
    "shadows": "<recorded result>",
    "demolition": "<recorded result>",
    "save_reload": "<recorded result>"
  },
  "tester": "<tester name>",
  "date": "<YYYY-MM-DD>",
  "screenshots": ["evidence/screenshots/<actual game screenshot>.png"]
}
```

Replace the placeholders with records of tests actually performed on the verified build. All declared cases must match the piece's `game_tests` and be `passed` for release readiness. The date must be a real calendar date in `YYYY-MM-DD` format. Evidence and screenshot paths must stay inside the project; absolute paths, parent traversal, and symbolic links are rejected. At least one referenced screenshot file must exist.

`package_fingerprints` must include **every** `manifest.files` entry, including the shared controller and menu DATs and the other selected pieces. Changing those files or any donor makes the old evidence inapplicable. Recheck the affected behavior rather than copying a new hash into an old passing record. The caller must verify the actual DAT files against the manifest before the evidence assessment. Matching hashes establish file identity, not that the reported game tests happened. Human permission/evidence flags likewise remain recorded assertions and do not provide automatic legal proof.

