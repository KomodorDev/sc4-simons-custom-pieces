---
title: "Contributor workflow"
summary: "Develop through tested pull requests into dev, promote releases into main, and keep local game inputs private."
audience: "Contributors, maintainers, and coding agents"
document_type: "procedure"
---

# Contributor workflow

<!-- BEGIN DOCUMENT NAVIGATION -->
[1. Repository scope](#1-repository-scope) · [2. Clone and prepare the project](#2-clone-and-prepare-the-project) · [3. Submit a change](#3-submit-a-change) · [4. Submit a release](#4-submit-a-release) · [5. Automatic installer prereleases](#5-automatic-installer-prereleases) · [6. Automated checks and coverage](#6-automated-checks-and-coverage) · [7. Required checks for maintainers](#7-required-checks-for-maintainers)
<!-- END DOCUMENT NAVIGATION -->

<a id="repository-scope"></a>

## 1. Repository scope

This repository contains the custom-piece library in `custom-pieces/` and its instructions, documentation, Git rules, and automated-test support. A **repository root** is the directory containing `custom-pieces/` and the root README. Its parent directory and name on your computer are your choice.

| Tracked content | Local content excluded from Git |
| --- | --- |
| Source code, schemas, registries, piece definitions, assembly definitions, and tests | Personal settings and native game inputs under `custom-pieces/local/` |
| Library guides, canonical images, connector exports, and current evidence | Private reports, captured game inputs, and temporary review workspaces under `custom-pieces/local/` |
| `README.md`, `AGENTS.md`, `.gitignore`, `docs/GITHUB.md`, `requirements-ci.txt`, and `tools/run_tests.py` | Build output under `custom-pieces/dist/`, virtual environments, and caches |
| `.github/workflows/ci.yml`, `.github/workflows/release-policy.yml`, `.github/workflows/installer-release.yml`, `.github/branch-protection.jsonc`, and `.github/branch-protection-main.jsonc` | Additional top-level files that are not explicitly allowed by the root ignore rules |

The root [ignore rules](../.gitignore) and [library rules](../custom-pieces/.gitignore) keep this boundary explicit. An **ignored file** remains on disk but is omitted from ordinary `git add` commands. GitHub does not back up ignored files. Keep separate backups of game saves, local inputs, and private configuration. Do not force-add personal paths, credentials, downloaded game archives, or disposable outputs.

To see which rule excludes a file, run this example from the repository root:

```sh
git check-ignore -v custom-pieces/local/settings.jsonc
```

<a id="clone-and-prepare-the-project"></a>

## 2. Clone and prepare the project

**Git** records file versions locally. A **commit** is one saved version. **GitHub** hosts a remote copy. A **clone** downloads the tracked files and history into a directory on your computer.

1. Open a terminal in the parent directory where you want to keep the project, then clone it:

   ```sh
   git clone https://github.com/KomodorDev/sc4-simons-custom-pieces.git
   cd sc4-simons-custom-pieces
   ```

2. Follow the [Python environment instructions](../README.md#2-prepare-python-and-run-the-tests). They cover macOS, Linux, and Windows, and install both normal and rendering test dependencies.
3. Run the tests from the repository root, with that environment active:

   ```sh
   python -B tools/run_tests.py
   ```

4. For game builds or native integration checks, prepare the supported NAM inputs and private `custom-pieces/local/settings.jsonc` using the [build guide](../custom-pieces/docs/BUILD_AND_INSTALL.md). A clone does not contain installed game resources, personal Plugins paths, or existing development builds. Keep those inputs outside version control.

An **editable installation**, created by `python -m pip install -e custom-pieces`, imports the source files directly. If you move the repository or switch to another clone, create a fresh virtual environment and install that editable package there so module commands use the intended source tree. Existing build folders and caches are optional. The [local-input guide](../custom-pieces/docs/BUILD_AND_INSTALL.md#3-prepare-local-development-inputs) distinguishes the public settings example, private game inputs, and generated builds.

<a id="submit-a-change"></a>

## 3. Submit a change

A **branch** is a named line of work. `dev` is the default branch and holds accepted development changes; `main` holds deliberately promoted releases. A **push** uploads commits, and a **pull** downloads and incorporates remote commits. A **pull request**, or **PR**, proposes merging one branch into another on GitHub. Its **base** is the destination, and its **head** is the source. Agents may create PRs, but only human maintainers may merge them. Agents must not enable automatic merging or treat successful tests as merge authorization.

The following example assumes that you can push branches to the canonical repository. If you cannot, fork the repository on GitHub, clone your fork, and create a pull request targeting the canonical repository's `dev` branch. A **fork** is a repository copy under your own GitHub account. In a fork, `origin` usually refers to that copy rather than the canonical repository.

1. From the repository root, inspect current work before switching branches. Commit or otherwise preserve any unfinished edits first:

   ```sh
   git status --short --branch
   git fetch origin
   git switch dev
   git pull --ff-only
   ```

   `--ff-only` allows the branch to advance directly to its configured remote version and stops if the histories have diverged. It does not create an unexpected merge commit.

2. Create a descriptive work branch:

   ```sh
   git switch -c docs/clarify-piece-guide
   ```

3. Make the change, follow the applicable [agent instructions](../AGENTS.md), and run the relevant checks. Before submitting the complete change, run:

   ```sh
   python -B tools/run_tests.py
   git diff --stat
   git diff
   ```

4. Select the actual changed files for the next commit. For example, if you changed only the library README:

   ```sh
   git add custom-pieces/README.md
   git diff --cached
   git commit -m "Clarify the piece authoring guide"
   git push -u origin docs/clarify-piece-guide
   ```

   Replace the file path, commit message, and branch name with your actual change. `git diff --cached` shows the selected changes before the commit. The `-u` option remembers the branch's remote counterpart for later pushes.

5. On GitHub, open the repository receiving the change, select **Pull requests → New pull request**, choose `dev` as the base, and choose your work branch as the comparison. Review **Files changed**, enter a descriptive title and explanation, and select **Create pull request**. For a fork, choose the option to compare across forks and select your fork's branch.
6. Wait for `Tests` to finish. Inspect failures and explicit skips. If the base branch changed, update the work branch with the accepted changes and wait for the new check. A previous commit's green result does not approve a newer commit.
7. A human maintainer reviews and merges the PR when required checks and conversations are satisfied. GitHub then runs the tests again on the resulting `dev` commit.
8. After the merge, update your local accepted branch:

   ```sh
   git switch dev
   git pull --ff-only
   ```

Local settings and ignored files stay outside Git throughout this workflow. A generated build belongs to the source version from which it was created; rebuild deliberately before installing outputs from a newer version. Build, install, source publication, and public plugin distribution remain separate operations.

<a id="submit-a-release"></a>

## 4. Submit a release

A **release promotion** accepts the tested development version into `main`. Ordinary work branches must first pass through `dev`. Prepare the complete prebuilt catalogue on the Mac before promoting source. A successful promotion starts the [automatic installer workflow](#5-automatic-installer-prereleases) for the exact merged revision.

1. Confirm that the intended changes have been merged into the canonical repository's `dev` branch and that its `Tests` run has passed. Run the [Mac preparation command](../custom-pieces/docs/AUTOMATIC_RELEASES.md#4-what-do-i-click-to-publish-and-find-the-download) from the matching clean checkout. Wait for `payload-ready`, which confirms that Dropbox has the entire verified ZIP.
2. On the canonical GitHub repository, select **Pull requests → New pull request**. Select **base: main** and **compare: dev**, both in the canonical repository. A fork's branch named `dev` is not an accepted release source.
3. Review **Files changed**, enter the release title and explanation, and select **Create pull request**.
4. Wait for both `Tests` and `Release policy` to pass. `Tests` checks the proposed merge, and `Release policy` checks that its source is this repository's `dev` branch. Resolve conversations and update the source through reviewed PRs if the current base has changed.
5. A human maintainer reviews the release and selects **Create a merge commit**, then confirms the merge. Keep the long-lived `dev` and `main` branches. Agents must leave the merge to the human maintainer.
6. Open **Actions → Installer release**, and inspect the run for the resulting `main` commit. The release job checks the approved merge, the Dropbox handoff, the exact release evidence, the packaged self-test, GUI startup, and the installer archive. When it succeeds, inspect the prerelease, its checksum, and `release-record.json`. For a temporary runner failure, rerun the same revision. If the source differs from the prepared ZIP, prepare the required revision and repeat the release route.
7. If `dev` is now behind the release commit on `main`, open a synchronization PR with **base: dev** and **compare: main**. A human maintainer merges it after `Tests` passes. This brings the release history back into development without pushing directly to a protected branch.

<a id="automatic-installer-prereleases"></a>

## 5. Automatic installer prereleases

Start with [Automatic releases, explained simply](../custom-pieces/docs/AUTOMATIC_RELEASES.md) for the Mac command, the one-time Dropbox and GitHub setup, and the exact buttons to use.

The [installer workflow](../.github/workflows/installer-release.yml) uses GitHub's hosted `windows-2022` runner. The Mac prepares all compiled SCP archives, including the shared controller and assembly menus. It keeps original SimCity and NAM inputs on the Mac and places only the verified handoff ZIP into the dedicated Dropbox App Folder. A Git tree fingerprint identifies the tracked files. The hosted job looks up the ZIP by that fingerprint and checks that both the original prebuild commit and receiving commit contain the same tracked tree.

Before checkout, the Windows job enables [Git's long-path support](https://gitforwindows.org/faq.html) with `git config --global core.longpaths true`. Deep evidence paths can exceed Git for Windows' default path-length limit when combined with the runner's workspace path, causing `Filename too long` before any tests or build commands run. Keep this setting before `actions/checkout`, together with `core.autocrlf false` and `core.eol lf`, so the complete source and frozen evidence are checked out without line-ending conversion.

Pull-request runs still build source-builder review artifacts using no Dropbox secrets. They also use [synthetic placeholder DATs](../custom-pieces/installer/prepare_fixture.py) for all current piece IDs to check compact Windows packaging, Downloads extraction, and the extracted executable, uploading only **compact-player-fixture-checks** reports; these files contain no playable content or native game resources and do not replace protected review of the exact real payload. A manual `dev` run uses the protected review environment and the exact Dropbox ZIP to prove the hosted handoff. It keeps the compiled ZIP on the runner. The release environment is restricted to `main`. It requires the recorded successful review run, explicit publication enablement, the approved `dev` release PR, and the [tracked evidence for an experimental installer](../custom-pieces/docs/RELEASE.md#experimental-installer-distribution). Only its release step uploads files.

Preparing the executable uses [the installer dependencies](../custom-pieces/requirements-installer.txt). The PR source-builder job and publication job additionally install [the source and test dependencies](../requirements-ci.txt): the source builder needs them for compilation, and publication needs them for the original catalogue-based release-evidence checks. Private prebuilt review uses the installer dependencies alone. Compact packaging explicitly excludes geometry libraries from the player application even when those libraries are installed on the publication runner.

The tag is **`installer-<first 12 characters of the main commit>`**. Its assets include the Windows ZIP, its checksum, the exact member index, the archive check, the Downloads extraction check, the two executable checks, and `release-record.json`. The release record and ZIP both identify the prebuild commit, the merged commit, the shared source tree, and the payload fingerprints. Published assets are immutable. A new source revision gets a new tag.

These are **experimental installer prereleases**. [`config/release.jsonc`](../custom-pieces/config/release.jsonc) governs compiled-plugin readiness, including recorded permission for any bundled derived resources. The compact player installer contains the finished SCP assets, its application runtime, and generated installation data. It excludes repository documentation, previews, historical evidence, authoring tools, geometry libraries, and test suites. Those files remain in Git and in the contributor workflow. Players select their actual Plugins folder directly; the installer verifies the supported game and NAM installation and retains ownership receipts, backups, updates, and Undo. Its Windows executable is unsigned. [Player instructions](../custom-pieces/docs/INSTALLER.md)

After the one-time enablement, a human source promotion starts automatic publication. The hosted tests check the frozen executable's runtime, GUI startup, and prebuilt installation and Undo with disposable synthetic files. Prebuilt archive verification enforces an extraction-path budget with 100 characters reserved for the destination and 259 characters allowed for the complete file path. The Windows build extracts the entire ZIP beneath a realistic Downloads destination and reruns both executable checks there, recording `extraction-check-windows-x64.json`. This records an actual hosted extraction check in addition to the path calculation; skipped native or game checks remain separate. Native geometry verification runs on the Mac against the audited game inputs. Actual in-game evidence follows the [separate release requirements](../custom-pieces/docs/RELEASE.md#5-gates-for-a-public-package).

<a id="automated-checks-and-coverage"></a>

## 6. Automated checks and coverage

**Continuous integration**, or **CI**, runs checks automatically when changes reach GitHub. A **runner** is the computer that executes a job, and a **status check** is GitHub's reported result. The [workflow](../.github/workflows/ci.yml) runs on a hosted Ubuntu runner with Python 3.11 and the dependencies in [requirements-ci.txt](../requirements-ci.txt). It calls the same [test script](../tools/run_tests.py) used locally.

| Event | Revision tested |
| --- | --- |
| A pull request is opened, reopened, or updated | GitHub's proposed merge into the target branch |
| A commit is pushed or merged into `dev` or `main` | The resulting branch commit |
| A merge queue requests checks | The proposed combined merge-group commit |
| **Actions → CI → Run workflow** | The branch selected in GitHub's manual-run form |

The workflow has no file-path filters, so documentation-only changes also report the required check. The `merge_group` event supports tests for repositories using a merge queue; the workflow does not enable that feature itself. The separate release policy supports ordinary release PRs. Enabling a merge queue for `main` would also require a release-policy check for merge-group events.

The separate [release policy workflow](../.github/workflows/release-policy.yml) uses `pull_request_target` to inspect PR metadata from the trusted default-branch workflow. It runs when a PR into `main` is opened, updated, reopened, or edited, including a change of destination. It checks no source files out, executes no PR code, and receives no token permissions. Its only accepted source is the canonical repository's `dev` branch. Normal development PRs into `dev` do not require this release check. GitHub explains the event's execution context in its [workflow event reference](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#pull_request_target).

The library discovers its framework, registered domain, and registered assembly suites. Pillow and NumPy enable portable rendering checks. Tests requiring supported NAM archives or staged compiled builds report explicit skips when those inputs are absent. A successful hosted run does not establish game placement, traffic behavior, installation, or public binary release readiness, and it does not modify manual game observations.

For local native integration checks, use private Plugins settings or set `SCP_TEST_NAM_PLUGINS` to the directory containing the exact audited inputs. Follow the [build guide](../custom-pieces/docs/BUILD_AND_INSTALL.md) for input verification and saved-build requirements.

<a id="required-checks-for-maintainers"></a>

## 7. Required checks for maintainers

The canonical repository uses `dev` as its default branch and protects both `dev` and `main`. `dev` requires the `Tests` check; `main` requires both `Tests` and `Release policy`. A work branch must include the current base version, required conversations must be resolved, and the rules apply to administrators. Force pushes and branch deletion are blocked. No approving review is required by the saved templates, so a human maintainer can merge a tested PR without a second reviewer. Fork owners manage their own repository settings; cloning or committing these templates does not apply branch protection.

Maintainers with repository administration permission can deliberately apply the [development protection template](../.github/branch-protection.jsonc) and the [release protection template](../.github/branch-protection-main.jsonc). GitHub accepts strict JSON, so first convert the commented sources into disposable API payloads from the repository root:

```sh
mkdir -p custom-pieces/local/github-api
python3 -B custom-pieces/framework/scp/jsonc.py .github/branch-protection.jsonc --output custom-pieces/local/github-api/dev-protection.json
python3 -B custom-pieces/framework/scp/jsonc.py .github/branch-protection-main.jsonc --output custom-pieces/local/github-api/main-protection.json
```

Open both generated files, confirm that conversion succeeded and that the required checks match the intended policy, then apply those strict-JSON payloads:

```sh
gh api --method PUT repos/KomodorDev/sc4-simons-custom-pieces/branches/dev/protection --input custom-pieces/local/github-api/dev-protection.json
gh api --method PUT repos/KomodorDev/sc4-simons-custom-pieces/branches/main/protection --input custom-pieces/local/github-api/main-protection.json
```

The JSONC files remain the authoring sources. The ignored `local/github-api/` files are generated API inputs; converting them changes no GitHub setting until a maintainer deliberately runs the corresponding `gh api` command.

When introducing this setup, merge the workflow changes into the default `dev` branch through a tested PR before expecting release PRs to report `Release policy`. Requiring the check on `main` before that first human merge intentionally blocks release merges until the workflow is available. Do not bypass protection or merge the setup PR as an agent to install it.

After installation, confirm that a `dev` → `main` release PR reports both required checks for its current revision. If `Release policy` remains **Expected**, inspect its event and revision association instead of bypassing protection.

Here, `gh` is GitHub's command-line tool. For a different repository, replace `KomodorDev/sc4-simons-custom-pieces` with that repository's owner and name. The release template binds its checks to GitHub Actions. Keep the `Tests` and `Release policy` names stable, or update protection when deliberately renaming them. GitHub documents the available settings in its [branch protection guide](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/managing-a-branch-protection-rule) and [required-check troubleshooting guide](https://docs.github.com/en/pull-requests/how-tos/merge-and-close-pull-requests/troubleshooting-required-status-checks).
