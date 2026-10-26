---
title: "Simon's Custom Pieces and SCP Planner"
summary: "Explore custom SimCity 4 network pieces, modular assemblies, and the companion placement tools."
audience: "Players, contributors, and maintainers"
document_type: "entry-point"
---

# Simon's Custom Pieces and SCP Planner

Simon's Custom Pieces is an experimental SimCity 4 network-piece library. It provides reusable High Speed Rail (HSR) and Ground High Speed Rail (GHSR) pieces, modular interchange blueprints, source definitions, and build tools. SCP Planner is the companion project for comparing connections and experimenting with piece placement; its Python tools are available, while the full browser interface remains unfinished.

A **piece** is one reusable construction type. An **assembly** is a layout made from several placed pieces. The library owns the piece definitions, generated connector data, canonical artwork, and recorded evidence; Planner consumes that data without changing the library's definitions.

| I want to… | Start here |
| --- | --- |
| Browse available pieces and assemblies | [Library guide](custom-pieces/README.md) and [illustrated piece inventory](custom-pieces/domains/high-speed-rail/00_pieces/INVENTORY.md) |
| Build or install a plugin from source | [Build and install](custom-pieces/docs/BUILD_AND_INSTALL.md) |
| Explore connection matching and placement tools | [SCP Planner](scp-planner/README.md) |
| Create pieces, assemblies, or documentation | [Authoring workflows](custom-pieces/README.md) |
| Understand source ownership and file formats | [Project structure](custom-pieces/STRUCTURE.md) |
| Contribute changes and understand automated checks | [Contributor workflow](docs/GITHUB.md) |

## Get the source

A **clone** is a local copy of the repository and its Git history. Clone the project into any directory where you keep source code:

```sh
git clone https://github.com/KomodorDev/sc4-simons-custom-pieces.git
cd sc4-simons-custom-pieces
```

The folder containing `custom-pieces/`, `scp-planner/`, and this README is the **repository root**. Keep the two project folders beside each other, and run the following commands from that root.

## Prepare Python and run the tests

Use Python 3.11 or newer. A **virtual environment** keeps the project's Python dependencies separate from other projects. Create and activate one using the commands for your operating system.

On macOS or Linux:

```sh
python3 -m venv .venv
source .venv/bin/activate
```

On Windows, in PowerShell:

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

With the environment active, install the dependencies, register the library's source packages, and run the shared test command:

```sh
python -m pip install -r requirements-ci.txt
python -m pip install -e custom-pieces
python -B tools/run_tests.py
```

The test command runs the library's framework, registered domain, and assembly suites, followed by the Planner tests. Pillow handles images, and NumPy supports numerical rendering tests. Tests that need unavailable NAM resources or saved development builds report explicit skips. NAM means Network Addon Mod, an external game dependency. Automated checks do not establish observed game behavior or update manual observations.

## Build and use the mod

Building the game plugin requires the exact supported NAM inputs described in the [build guide](custom-pieces/docs/BUILD_AND_INSTALL.md). Copy the provided configuration example to `custom-pieces/local/settings.json` and enter the actual Plugins paths for your installation, following that guide. Build outputs are written under `custom-pieces/dist/`. Neither the installed game resources nor personal settings belong in Git.

The project remains experimental. Read each piece's documented limits and recorded tests before using it. Software previews and passing automated checks do not prove placement, traffic, or rendering inside the game. Public binary distribution has separate [release requirements](custom-pieces/docs/RELEASE.md).

## Contribute

The repository contains `custom-pieces/`, `scp-planner/`, and their shared repository support. Canonical images and evidence are tracked with their owning subjects; private settings, native test inputs, caches, and disposable builds are ignored. See [the contributor workflow](docs/GITHUB.md) for the exact file boundary and branch procedure.

`dev` is the default development branch. Create ordinary work branches from `dev`, and submit their pull requests to `dev`. Reserve `main` for release pull requests from this repository's `dev` branch. GitHub Actions runs `Tests` for pull requests, pushes to `dev` and `main`, and merge-queue candidates. Both branches require passing tests; `main` also requires `Release policy`, which rejects other release sources. Agents may create pull requests; human maintainers perform merges. See [the contributor workflow](docs/GITHUB.md#submit-a-release) for the release steps.
