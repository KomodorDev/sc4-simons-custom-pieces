---
title: "Git and GitHub workflow"
summary: "Preserve the existing local workspace, publish maintained project files, and run automated tests before and after merges."
audience: "Project owner, developers, and coding agents"
document_type: "procedure"
---

# Git and GitHub workflow

## What this setup does

**Git** records versions of selected project files on your computer. A **repository** is the folder whose versions Git manages. A **commit** is one saved version with a descriptive message. **GitHub** stores a remote copy of those commits. A **push** uploads local commits; a **pull** downloads and incorporates remote commits. A **branch** is a named line of work; `main` holds the accepted version. A **pull request**, or **PR**, proposes merging a branch into another branch on GitHub.

The intended GitHub destination is the existing public repository [KomodorDev/sc4-simons-custom-pieces](https://github.com/KomodorDev/sc4-simons-custom-pieces). Public means uploaded files can be read by anyone. The repository contains this entire maintained project, including `custom-pieces/`, `scp-planner/`, guides, plans, research, and authored setup helpers.

The working folder on this Mac remains `/Users/simonhinterreiter/Documents/ChatGPT/Project_Sim_City`. Existing local paths, launchers, game settings, and build outputs continue to use that folder. An older empty checkout exists in `/Users/simonhinterreiter/Library/CloudStorage/Dropbox/06 - Coding/01 - Local Git Repos/02 - Mac/sc4-simons-custom-pieces`; it is not the working folder prepared here. Open the `Project_Sim_City` folder when editing or running commands. Use one working copy consistently to avoid editing two different versions by accident.

The local Git remote is named `origin`, which is Git's conventional name for the GitHub destination. It points to `https://github.com/KomodorDev/sc4-simons-custom-pieces.git`. A configured remote does not upload files. Use `git log -1 --oneline` to see the latest local commit, `git status --short --branch` to see unsaved changes and synchronization status, and the GitHub page to verify what has actually been uploaded.

## Which files belong in Git

| Stored in Git | Kept only on this workstation |
| --- | --- |
| Library implementation, schemas, registries, piece definitions, assembly definitions, and tests | `custom-pieces/local/`, including personal Plugins paths, native validation inputs, and copied trial workspaces |
| Planner source, configuration examples, tools, and tests | `scp-planner/local/`, including private working reports |
| Canonical piece images, connector exports, current evidence, manual observation records, and assembly previews | `custom-pieces/dist/`, Planner build output, and caches |
| Project guides, plans, research references, setup scripts, patches, manifests, and provenance records | Root `backups/` and `tmp/`, setup backup snapshots, downloaded installers, staged game assets, and compiled helper binaries |
| Notes and recorded patches explaining third-party build dependencies | Downloaded NAM, Plop and Paint, fast_float, and tool checkouts under `setup/` |

The root [`.gitignore`](../.gitignore), [library ignore rules](../custom-pieces/.gitignore), and [Planner ignore rules](../scp-planner/.gitignore) implement this boundary. An **ignored file** stays on disk but is excluded from ordinary `git add` commands. GitHub does not back up ignored files. Keep the existing separate backup process for city saves, private inputs, and original snapshots. Canonical artwork stays in Git even when a tool generated it, because the library owns those reviewed files and their evidence.

To find out why a particular file is excluded, run, for example:

```sh
git check-ignore -v custom-pieces/local/settings.json
```

The output identifies the ignore file, matching rule, and excluded path. Do not use `git add -f` to bypass these rules for local game inputs or downloaded archives. Preserve existing imported documents and frozen evidence rather than rewriting them during migration. Downloaded third-party source checkouts retain their own upstream history; the project's authored patches and build notes remain tracked beside them.

## Check the local preparation

1. Open Terminal, then enter the exact command below. `cd` changes the folder in which subsequent commands run; the quotes preserve spaces in paths.

   ```sh
   cd "/Users/simonhinterreiter/Documents/ChatGPT/Project_Sim_City"
   ```

2. Inspect the local branch, pending changes, and remote destination:

   ```sh
   git status --short --branch
   git remote -v
   git log -1 --oneline
   ```

   The branch should be `main`, and both remote lines should name the existing `KomodorDev/sc4-simons-custom-pieces` repository. A clean status means the maintained files match the latest commit; ignored local files still exist.

3. Check the Python version and run the same test command GitHub will use:

   ```sh
   python3 --version
   python3 -m pip install -r requirements-ci.txt
   python3 -B tools/run_tests.py
   ```

   Use Python 3.11 or newer. If Python requires a virtual environment, create an isolated dependency folder with `python3 -m venv .venv`, run `source .venv/bin/activate`, and repeat the two install/test commands. A **virtual environment** keeps this project's installed Python packages separate from other projects. Existing working Python installations can continue to be used.

## Upload the initial version

Perform this step when the initial public upload has been approved. It publishes every tracked file in the initial commit to the existing public repository. It does not upload ignored local files or install anything into the game.

1. From the working folder, confirm that `git status --short --branch` reports the intended commit and no unexpected pending changes.
2. Upload `main` and remember its remote branch:

   ```sh
   git push -u origin main
   ```

   The `-u` option records `origin/main` as the branch to compare and synchronize with. Later pushes from that branch can use `git push`. If Git reports that remote work already exists, stop and inspect it with `git fetch origin` and `git log --oneline --all --graph`; preserve that work rather than forcing the push.

3. Open the [repository](https://github.com/KomodorDev/sc4-simons-custom-pieces). Confirm that the root README, `custom-pieces/`, `scp-planner/`, and `.github/workflows/ci.yml` appear.
4. Click **Actions**, click the **CI** run for the uploaded commit, and click the **Tests** job. Wait for it to finish, then inspect its test output. A green result means every test that ran passed; explicit skipped tests remain outside that result's coverage.
5. Enable the merge requirement below. Uploading a workflow runs tests but does not, by itself, prevent merging after a failure.

The initial upload establishes the repository's first branch. Subsequent accepted changes should use pull requests and the required test check.

## Require passing tests before merging

**Continuous integration**, or **CI**, means running automated checks whenever proposed code changes arrive. A **status check** is GitHub's reported outcome for one such job. A **branch protection rule** makes selected conditions mandatory before changes enter `main`.

After `Tests` has run successfully on GitHub, apply the prepared [branch protection settings](../.github/branch-protection.json) from the working folder using GitHub CLI, the `gh` command-line tool:

```sh
gh api --method PUT repos/KomodorDev/sc4-simons-custom-pieces/branches/main/protection --input .github/branch-protection.json
```

This requires repository administration permission. The settings require a pull request, the successful `Tests` check, a branch that includes current `main`, and resolved review conversations. They apply to administrators too, prohibit force pushes and deletion of `main`, and require zero approving reviews so the project owner can merge their own tested PRs. The JSON file is a reviewable settings template; GitHub does not automatically apply it when it is committed.

To apply the same settings through the GitHub website:

1. Open the repository, click **Settings**, click **Branches** in the left sidebar, and click **Add classic branch protection rule** under **Branch protection rules**. If a rule for `main` already exists, edit that rule instead of creating a competing one.
2. In **Branch name pattern**, type `main`.
3. Select **Require a pull request before merging**. Leave **Require approvals** unchecked unless another person will review every change; GitHub does not let you approve your own pull request.
4. Select **Require status checks to pass before merging**. In its search field, type `Tests`, and select the `Tests` job reported by GitHub Actions. A successful run must have appeared recently for GitHub to offer it.
5. Select **Require branches to be up to date before merging**. This ensures the proposed changes are tested together with the latest accepted version.
6. Select **Require conversation resolution before merging** and **Do not allow bypassing the above settings**. Keep **Allow force pushes** and **Allow deletions** unchecked.
7. Click **Create** or **Save changes**. On future PRs targeting `main`, inspect the checks area and confirm `Tests` is marked **Required**. An unsuccessful required check should prevent the normal merge action.

These steps follow GitHub's [branch protection instructions](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/managing-a-branch-protection-rule) and [required status check guidance](https://docs.github.com/en/pull-requests/how-tos/merge-and-close-pull-requests/troubleshooting-required-status-checks). Keep the job's `Tests` name stable, or update the protection rule when deliberately renaming it.

## Daily local work and pull requests

1. Start from an up-to-date accepted version. Commit or otherwise preserve any current edits before switching branches:

   ```sh
   git status --short --branch
   git switch main
   git pull --ff-only
   ```

   `--ff-only` allows an update only when it can advance directly to the remote version; it stops if the histories have diverged instead of creating an unexpected merge.

2. Create a branch for one task. Choose a descriptive name; this example creates `work/update-piece-docs` and switches to it:

   ```sh
   git switch -c work/update-piece-docs
   ```

3. Edit files with the same local tools as before. Existing build and game installation commands still work; follow the [build guide](../custom-pieces/docs/BUILD_AND_INSTALL.md). Run the relevant focused checks while editing, then run the full shared command before proposing the merge:

   ```sh
   python3 -B tools/run_tests.py
   git status --short
   git diff --stat
   git diff
   ```

4. Select the completed files for the commit. This **staging** step identifies exactly which changes the next commit saves. For example, if you edited only the library README:

   ```sh
   git add custom-pieces/README.md
   git diff --cached --stat
   git diff --cached
   git commit -m "Clarify piece documentation workflow"
   git push -u origin work/update-piece-docs
   ```

   Replace the path, commit message, and branch name with your actual task. `git diff --cached` shows the selected changes before you save them. A commit is local until pushed.

5. Open the repository on GitHub. Click **Pull requests**, then **New pull request**. Select `main` as **base** and your work branch as **compare**. Click **Create pull request**, enter a descriptive title and the change's purpose, and click **Create pull request** again.
6. Wait for `Tests` to pass, then review the **Files changed** tab and any skipped-test limits. If `main` changed during your work, use GitHub's **Update branch** action when offered, or incorporate `main` into the work branch locally, push, and wait for the new test run. Fix a failed automated check before merging; do not change manual game observations to make software checks appear successful.
7. Click **Merge pull request**, then **Confirm merge**, when all required checks and conversations are satisfied. GitHub runs `Tests` again on the resulting `main` commit.
8. Update your local accepted branch:

   ```sh
   git switch main
   git pull --ff-only
   ```

   Your working files now include the accepted changes. Local ignored settings, backups, and build directories stay on disk throughout this workflow. Build outputs are generated from a particular source version; rebuild deliberately before installing a plugin from a newer version.

## What the automated checks cover

The [workflow](../.github/workflows/ci.yml) runs on GitHub's hosted Ubuntu runner using Python 3.11, with the dependencies listed through [requirements-ci.txt](../requirements-ci.txt). A **runner** is the computer GitHub assigns to execute a job. The workflow uses the same [test runner script](../tools/run_tests.py) that is available locally; it returns a failure if either the library or Planner suite fails, and runs both suites so their results are visible.

| GitHub event | Revision tested |
| --- | --- |
| Pull request opened, reopened, or updated | GitHub's proposed merge of the PR into its target branch |
| Push to `main`, including a completed merge | The actual new `main` commit |
| Merge queue requests checks | The proposed combined merge-group commit |
| **Actions → CI → Run workflow** | The selected branch or revision supported by GitHub's manual run form |

The workflow has no file-path filters, so documentation-only PRs still report the required check. Its `merge_group` event supports a future merge queue; it does not enable that feature, which depends on GitHub availability and repository settings. See GitHub's [workflow event reference](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows).

The library command discovers framework tests, each registered domain's tests, and each registered assembly's tests. Planner runs its complete test directory against the adjacent library checkout. Pillow and NumPy are installed so portable rendering coverage can run. Real NAM integration tests and compiled-build fixture tests require external native archives or local staged builds and can explicitly skip when those inputs are absent. NAM means Network Addon Mod, the external game dependency. Those skips are printed in the logs; a green hosted run does not prove successful native builds, macOS helper execution, installation, rendering inside the game, traffic behavior, or public plugin release readiness.

For local native integration checks, keep the existing private Plugins settings or set the existing `SCP_TEST_NAM_PLUGINS` environment variable to the directory containing the exact audited NAM inputs. Follow the library's [build and install guide](../custom-pieces/docs/BUILD_AND_INSTALL.md) for input verification. This GitHub preparation does not change the source profiles, dependency fingerprints, approved geometry, game IDs, or manual observations. Existing public-release blockers remain separate work.

## Start from a fresh clone on another computer

After the initial upload, a **clone** downloads the repository's tracked files and Git history into a new folder. It does not recreate ignored files from this workstation.

```sh
git clone https://github.com/KomodorDev/sc4-simons-custom-pieces.git
cd sc4-simons-custom-pieces
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements-ci.txt
python3 -m pip install -e custom-pieces
python3 -B tools/run_tests.py
```

These commands assume a macOS or Linux terminal with Git and Python 3.11 or newer installed. The editable `-e` installation registers the cloned source packages, so later edits are visible to the library's module commands. Existing game installations, NAM archives, downloaded setup tools, and city saves must be restored or installed separately. For game-building operations, copy `custom-pieces/config/local.example.json` to `custom-pieces/local/settings.json`, fill in this computer's actual Plugins paths, and follow the linked build guide. Restore exact recorded third-party versions and patches from their owning setup notes when those older helpers are needed; they are not prerequisites for portable CI.
