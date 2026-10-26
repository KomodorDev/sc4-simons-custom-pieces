# Riprap stone seawalls

Installed and checked on **16 September 2026** in **SimCity 4 Windows**.

The angled rock shoreline in the [reference video](https://www.youtube.com/shorts/8dS-WP0sATI) visually matches **NBVC Riprap Seawall**. Riprap means a slope covered with separate rocks. Each game piece already contains its stones; place adjoining sections to build a longer shoreline.

Installed packages:

- [Riprap Seawall 1.0](https://community.simtropolis.com/files/file/26175-riprap-seawall/) — seven straight, corner and stair sections.
- [Riprap Seawall Addon 1.0](https://community.simtropolis.com/files/file/26255-riprap-seawall-addon/) — seven diagonal, uneven and small-stair sections.

Both authors' pages list no additional dependencies. The existing NBVC Marina concrete walls remain available.

## Find and place them

1. Start **SimCity 4 Windows** and open your city.
2. Press the letter **O** to open **Advanced Plopping & Painting**, your installed search panel.
3. Select **Buildings & Lots**. A **lot** is a complete placeable section occupying one or more map squares.
4. Click the search box and type **Riprap**. All 14 new pieces are present in the rebuilt search catalogue.
5. Start with **Riprap Seawall**. Its description is **Riprap Seawall 1x1**. Select its **Plop** action, which means place the item manually.
6. Move the preview to an empty shoreline. Rotate it with **fn / 🌐 + ←** or **fn / 🌐 + →** until its rock face points toward the water. Click to place when the game permits it.
7. Check that the top meets your land and that the rocks cover the bank before extending the wall. Terrain height affects the fit; the author does not specify a universal required elevation.
8. Place neighboring pieces to extend it. Search **Riprap Seawall Diagonal** for a diagonal shore and **Riprap Seawall Inner Corner** or **Riprap Seawall Outer Corner** for turns.
9. Press **Escape** to stop placing pieces.

The author also lists the **Seaport menu** as their normal location. Search-panel titles are verified in the generated catalogue; placement inside a running city remains untested.

## Management in sc4pac

These manually downloaded ZIPs were supplied through sc4pac's **Select a file from disk to use instead** fallback. sc4pac extracted the packages in a staging profile, and their files and manager records were then added to your active profile. The active manager's own `list` command confirms both packages as installed and explicitly selected:

- `nbvc:riprap-seawall` — version `1.0`
- `nbvc:riprap-seawall-addon` — version `1.0`

They can therefore be updated or removed through sc4pac. Manually downloading an archive does not prevent management. Simply copying extracted files into Plugins, without registering a package, does not make those copies managed. If a later download is blocked, sc4pac may need the updated ZIP supplied manually again. [Official local-file fallback release notes](https://github.com/memo33/sc4pac-gui/releases/tag/1.2.0) · [Official sc4pac documentation](https://github.com/memo33/sc4pac-tools)

Verification: 50 installed payload files match the original archives; all 169 previous package records and all existing non-catalogue files were preserved. There are now **171 managed packages**. Plop and Paint rebuilt successfully with **893 buildings, 2,363 lots and zero parsing errors**, including all 14 Riprap pieces.

Backups, original ZIPs and verification records are in [setup/riprap-seawall](</Users/simonhinterreiter/Documents/ChatGPT/Project_Sim_City/setup/riprap-seawall>).
