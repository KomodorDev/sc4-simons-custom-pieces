---
title: "Simon's Custom Pieces"
summary: "Explore custom SimCity 4 network pieces, modular assemblies, and their authoring tools."
audience: "Players, contributors, and maintainers"
document_type: "entry-point"
---

# Simon's Custom Pieces

Simon's Custom Pieces is an experimental SimCity 4 network-piece library. It provides reusable High Speed Rail (HSR) and Ground High Speed Rail (GHSR) pieces, modular interchange blueprints, source definitions, and build tools.

A **piece** is one reusable construction type. An **assembly** is a layout made from several placed pieces. The library owns the piece definitions, generated connector data, canonical artwork, and recorded evidence.

| I want to… | Start here |
| --- | --- |
| Browse available pieces and assemblies | [Library guide](custom-pieces/README.md) and [illustrated piece inventory](custom-pieces/domains/high-speed-rail/00_pieces/INVENTORY.md) |
| Build or install a plugin from source | [Build and install](custom-pieces/docs/BUILD_AND_INSTALL.md) |
| Understand connector declarations and generated exports | [Connector reference](custom-pieces/docs/CONNECTOR_METADATA.md) |
| Create pieces, assemblies, or documentation | [Authoring workflows](custom-pieces/README.md) |
| Understand source ownership and file formats | [Project structure](custom-pieces/STRUCTURE.md) |
| Contribute changes and understand automated checks | [Contributor workflow](docs/GITHUB.md) |

## Get the source

A **clone** is a local copy of the repository and its Git history. Install [Git](https://git-scm.com/downloads/) if needed, then open a terminal and type `git --version` to confirm that it is available. Clone the project into any directory where you keep source code:

```sh
git clone https://github.com/KomodorDev/sc4-simons-custom-pieces.git
cd sc4-simons-custom-pieces
```

The folder containing `custom-pieces/` and this README is the **repository root**. Run the following commands from that root.

## Prepare Python and run the tests

Use Python 3.11 or newer; [official Python downloads](https://www.python.org/downloads/) are available if it is not installed. CI uses Python 3.11. A **virtual environment** keeps the project's Python dependencies separate from other projects. Create and activate one using the commands for your operating system.

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

The test command runs the library's framework, registered domain, and assembly suites. Pillow handles images, and NumPy supports numerical rendering tests. These portable checks do not require a game installation. Tests that need unavailable NAM resources or saved development builds report explicit skips. NAM means Network Addon Mod, an external game dependency. Automated checks do not establish observed game behavior or update manual observations.

## Build and use the mod

Building the game plugin requires the exact supported NAM inputs described in the [build guide](custom-pieces/docs/BUILD_AND_INSTALL.md#prepare-local-development-inputs). The repository provides a [workstation-settings example](custom-pieces/config/local.example.json) and an [audited NAM profile](custom-pieces/config/profiles/nam50-rhd.json). Each contributor supplies their own local game resources and ignored settings; existing build folders are optional and can be regenerated. Build outputs are written under `custom-pieces/dist/`. Neither the installed game resources nor personal settings belong in Git.

The project remains experimental. Read each piece's documented limits and recorded tests before using it. Software previews and passing automated checks do not prove placement, traffic, or rendering inside the game. Public binary distribution has separate [release requirements](custom-pieces/docs/RELEASE.md).

## Contribute

The repository contains `custom-pieces/` and its repository support. Canonical images and evidence are tracked with their owning subjects; private settings, native test inputs, caches, and disposable builds are ignored. See [the contributor workflow](docs/GITHUB.md) for the exact file boundary and branch procedure.

`dev` is the default development branch. Create ordinary work branches from `dev`, and submit their pull requests to `dev`. Reserve `main` for release pull requests from this repository's `dev` branch. GitHub Actions runs `Tests` for pull requests, pushes to `dev` and `main`, and merge-queue candidates. Both branches require passing tests; `main` also requires `Release policy`, which rejects other release sources. Agents may create pull requests; human maintainers perform merges. See [the contributor workflow](docs/GITHUB.md#submit-a-release) for the release steps.
