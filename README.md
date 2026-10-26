---
title: "SimCity 4 project"
summary: "Find the custom-piece library, Planner, local setup history, and GitHub development workflow."
audience: "Project owner, developers, and coding agents"
document_type: "entry-point"
---

# SimCity 4 project

This repository contains Simon's Custom Pieces, a SimCity 4 network-piece authoring library, and SCP Planner, its separate placement and compatibility consumer. It also preserves project guides, plans, research, authored setup helpers, and canonical artwork. High Speed Rail (HSR) is the implemented network family.

| I want to… | Open |
| --- | --- |
| Browse pieces, assemblies, or authoring workflows | [Custom-piece library](custom-pieces/README.md) |
| Build, inspect, or install a plugin locally | [Build and install](custom-pieces/docs/BUILD_AND_INSTALL.md) |
| Work on placement and connection discovery | [SCP Planner](scp-planner/README.md) |
| Understand source ownership and documentation rules | [Library structure](custom-pieces/STRUCTURE.md) and [agent instructions](AGENTS.md) |
| Use Git, publish the initial copy, or require passing merge tests | [Git and GitHub workflow](docs/GITHUB.md) |
| Read the existing game setup history | [Setup summary](SimCity%204%20-%20Setup%20Summary.md) |

## Run the automated tests

Use Python 3.11 or newer. From the repository's root folder, install the test dependencies and run the shared test command:

```sh
python3 -m pip install -r requirements-ci.txt
python3 -B tools/run_tests.py
```

The command runs the library's framework, registered domain, and assembly suites, followed by all Planner tests. Pillow supplies image handling, and NumPy supports numerical rendering tests; both are included in the test dependencies. Tests requiring unavailable game resources or saved development builds report explicit skips. Automated checks do not establish observed game behavior or update manual game observations.

GitHub Actions, GitHub's automated job service, uses this same test command for pull requests, pushes to `main`, and merge-queue candidates. The check is named `Tests`. The workflow takes effect after the files reach GitHub; enforcing that check before merging also requires the repository setting described in the [GitHub guide](docs/GITHUB.md#require-passing-tests-before-merging).

## Keep working locally

Continue editing and running this project in its existing folder. Private game paths remain in `custom-pieces/local/settings.json`; built plugins remain in `custom-pieces/dist/`. Git tracks maintained source, documentation, canonical images, and evidence. Backups, downloaded installers, third-party source checkouts, copied trial workspaces, generated binaries, and caches remain on the workstation and are excluded by the project's `.gitignore` files. Excluding a file from Git does not delete it or back it up elsewhere.

See the [GitHub guide](docs/GITHUB.md) for exact first-upload steps, daily branch and pull-request commands, and fresh-clone setup. Building, installing into the game, publishing source to GitHub, and distributing a public plugin are separate operations.
