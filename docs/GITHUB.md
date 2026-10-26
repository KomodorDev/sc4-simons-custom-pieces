---
title: "Contributor workflow"
summary: "Clone the project anywhere, keep local game inputs private, and submit changes with automated checks."
audience: "Contributors, maintainers, and coding agents"
document_type: "procedure"
---

# Contributor workflow

## Repository scope

This repository contains the custom-piece library in `custom-pieces/`, SCP Planner in `scp-planner/`, and the shared instructions, documentation, Git rules, and automated-test support required by those projects. A **repository root** is the directory containing those two project folders and the root README. Its parent directory and name on your computer are your choice.

| Tracked content | Local content excluded from Git |
| --- | --- |
| Source code, schemas, registries, piece definitions, assembly definitions, and tests | Personal settings and native game inputs under `custom-pieces/local/` |
| Library and Planner guides, canonical images, connector exports, and current evidence | Private Planner reports under `scp-planner/local/` |
| `README.md`, `AGENTS.md`, `.gitignore`, `docs/GITHUB.md`, `requirements-ci.txt`, and `tools/run_tests.py` | Build output under each project's `dist/`, virtual environments, and caches |
| `.github/workflows/ci.yml` and `.github/branch-protection.json` | Additional top-level files that are not explicitly allowed by the root ignore rules |

The root [ignore rules](../.gitignore), [library rules](../custom-pieces/.gitignore), and [Planner rules](../scp-planner/.gitignore) keep this boundary explicit. An **ignored file** remains on disk but is omitted from ordinary `git add` commands. GitHub does not back up ignored files. Keep separate backups of game saves, local inputs, and private configuration. Do not force-add personal paths, credentials, downloaded game archives, or disposable outputs.

To see which rule excludes a file, run this example from the repository root:

```sh
git check-ignore -v custom-pieces/local/settings.json
```

## Clone and prepare the project

**Git** records file versions locally. A **commit** is one saved version. **GitHub** hosts a remote copy. A **clone** downloads the tracked files and history into a directory on your computer.

1. Open a terminal in the parent directory where you want to keep the project, then clone it:

   ```sh
   git clone https://github.com/KomodorDev/sc4-simons-custom-pieces.git
   cd sc4-simons-custom-pieces
   ```

2. Follow the [Python environment instructions](../README.md#prepare-python-and-run-the-tests). They cover macOS, Linux, and Windows, and install both normal and rendering test dependencies.
3. Run the tests from the repository root, with that environment active:

   ```sh
   python -B tools/run_tests.py
   ```

4. For game builds or native integration checks, prepare the supported NAM inputs and private `custom-pieces/local/settings.json` using the [build guide](../custom-pieces/docs/BUILD_AND_INSTALL.md). A clone does not contain installed game resources, personal Plugins paths, or existing development builds. Keep those inputs outside version control.

An **editable installation**, created by `python -m pip install -e custom-pieces`, imports the source files directly. If you move the repository or switch to another clone, reinstall that editable package in the active virtual environment so module commands use the intended source tree. Keep `custom-pieces/` and `scp-planner/` beside each other; Planner's default configuration uses their relative locations.

## Submit a change

A **branch** is a named line of work. `main` holds the accepted project version. A **push** uploads commits, and a **pull** downloads and incorporates remote commits. A **pull request**, or **PR**, proposes merging one branch into another on GitHub. Agents may create PRs, but only human maintainers may merge them. Agents must not enable automatic merging or treat successful tests as merge authorization.

The following example assumes that you can push branches to the canonical repository. If you cannot, fork the repository on GitHub, clone your fork, and create a pull request targeting the canonical repository's `main` branch. A **fork** is a repository copy under your own GitHub account. In a fork, `origin` usually refers to that copy rather than the canonical repository.

1. From the repository root, inspect current work before switching branches. Commit or otherwise preserve any unfinished edits first:

   ```sh
   git status --short --branch
   git switch main
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

5. On GitHub, open the repository receiving the change, select **Pull requests → New pull request**, choose `main` as the base, and choose your work branch as the comparison. Review **Files changed**, enter a descriptive title and explanation, and select **Create pull request**. For a fork, choose the option to compare across forks and select your fork's branch.
6. Wait for `Tests` to finish. Inspect failures and explicit skips. If the base branch changed, update the work branch with the accepted changes and wait for the new check. A previous commit's green result does not approve a newer commit.
7. A human maintainer reviews and merges the PR when required checks and conversations are satisfied. GitHub then runs the tests again on the resulting `main` commit.
8. After the merge, update your local accepted branch:

   ```sh
   git switch main
   git pull --ff-only
   ```

Local settings and ignored files stay outside Git throughout this workflow. A generated build belongs to the source version from which it was created; rebuild deliberately before installing outputs from a newer version. Build, install, source publication, and public plugin distribution remain separate operations.

## Automated checks and coverage

**Continuous integration**, or **CI**, runs checks automatically when changes reach GitHub. A **runner** is the computer that executes a job, and a **status check** is GitHub's reported result. The [workflow](../.github/workflows/ci.yml) runs on a hosted Ubuntu runner with Python 3.11 and the dependencies in [requirements-ci.txt](../requirements-ci.txt). It calls the same [test script](../tools/run_tests.py) used locally.

| Event | Revision tested |
| --- | --- |
| A pull request is opened, reopened, or updated | GitHub's proposed merge into the target branch |
| A commit is pushed or merged into `main` | The resulting `main` commit |
| A merge queue requests checks | The proposed combined merge-group commit |
| **Actions → CI → Run workflow** | The branch selected in GitHub's manual-run form |

The workflow has no file-path filters, so documentation-only changes also report the required check. The `merge_group` event supports repositories using a merge queue; the workflow does not enable that feature itself.

The library discovers its framework, registered domain, and registered assembly suites; Planner runs its complete test directory against the adjacent library source. Pillow and NumPy enable portable rendering checks. Tests requiring supported NAM archives or staged compiled builds report explicit skips when those inputs are absent. A successful hosted run does not establish game placement, traffic behavior, installation, or public binary release readiness, and it does not modify manual game observations.

For local native integration checks, use private Plugins settings or set `SCP_TEST_NAM_PLUGINS` to the directory containing the exact audited inputs. Follow the [build guide](../custom-pieces/docs/BUILD_AND_INSTALL.md) for input verification and saved-build requirements.

## Required checks for maintainers

The canonical repository protects `main` with the `Tests` status check. A work branch must include the current base version, required conversations must be resolved, and the rule applies to administrators. No approving review is required by the saved template, so a human maintainer can merge a tested PR without a second reviewer. Fork owners manage their own repository settings; cloning or committing the template does not apply branch protection.

Maintainers with repository administration permission can deliberately apply the [saved protection template](../.github/branch-protection.json) to the canonical repository after `Tests` has run:

```sh
gh api --method PUT repos/KomodorDev/sc4-simons-custom-pieces/branches/main/protection --input .github/branch-protection.json
```

Here, `gh` is GitHub's command-line tool. For a different repository, replace `KomodorDev/sc4-simons-custom-pieces` with that repository's owner and name. Keep the `Tests` job name stable, or update the protection rule when deliberately renaming it. GitHub documents the available settings in its [branch protection guide](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/managing-a-branch-protection-rule) and [required-check troubleshooting guide](https://docs.github.com/en/pull-requests/how-tos/merge-and-close-pull-requests/troubleshooting-required-status-checks).
