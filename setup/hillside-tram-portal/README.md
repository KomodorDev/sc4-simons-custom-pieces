# Morifari hillside tram portal installation

Installed on 20 September 2026 in the active Windows game profile.

- Source: [Hillside GLR to subway transition by morifari, version 1.0](https://community.simtropolis.com/files/file/14932-hillside-glr-to-subway-transition-by-morifari/), published by Andreas Roth.
- Original archive: `downloads/morifari_GLR_to_subway.zip`, preserved unchanged.
- Installation folder: `/Users/simonhinterreiter/Documents/SimCity 4 Windows/Plugins/700-transportation/Morifari - Hillside GLR to Subway`.
- Installed files: both original SC4Lot files and their shared prop DAT. NAM is the only author-listed prerequisite and is already installed.
- This is a manual installation in a separate folder. It is not registered as a sc4pac package. The sc4pac profile was not changed.
- The Plop and Paint catalogue was rebuilt successfully. Both portal entries and the existing avenue ramp were verified in the resulting catalogue. Original catalogue files are preserved in the timestamped `before-` folder.
- No city save was edited. Actual terrain placement and commuter routes have not been tested in the running game.

Press **O**, open **Buildings & Lots**, and search **GLR-to-Subway tunnel entrance**:

| Catalogue entry | Appearance | Lot footprint |
|---|---|---|
| GLR-to-Subway tunnel entrance | Concrete | 1 × 1 |
| GLR-to-Subway tunnel entrance, rural version | Grass | 1 × 1 |

The visible model extends beyond its one-tile lot; leave space beside it.

The upper entrance was already installed. Search **Tram in Ave** and choose **Tram in Ave to Subway/U-GLR Transition**. It occupies two tiles across and three along the avenue.

See [the construction guide](../../research/hillside-tram-portal/Upper%20avenue%20and%20lower%20hillside%20connection.md) for placement, surface activation, and the required underground connections.

`installation-verification.json` records the source, hashes, installed files and verified catalogue entries. The author's unmodified instructions are in `Hillside_GLR_to_subway_readme.txt`.

If removing this download later, first bulldoze its placed portals in any cities that use them, as the author instructs; then remove only the dedicated installation folder and refresh the catalogue.
