# Upper avenue entrance and lower hillside tram exit

**Plan:** keep the tram in the avenue through the business district. Before the avenue reaches the HSR boundary, send the tram underground through the installed **Tram in Ave to Subway/U-GLR Transition**. Connect it with the **Subway** tool to a Morifari hillside portal beside the park. The avenue's car lanes continue across the upper entrance at ground level.

**Verification, 20 September 2026:** the upper entrance's catalogue name, 2 × 3 footprint, traffic switches and network paths were inspected in the active Windows Plugins folder. The downloaded Morifari archive was inspected directly: both lower portal variants have a 1 × 1 lot footprint, and their names are given below. The author's included readme was also checked. The exact arrangement has not been built or traffic-tested in your city. The three archive files have been installed in the dedicated Morifari folder, and the refreshed catalogue confirms both lower names and footprints as well as the upper transition. The installation record is `setup/hillside-tram-portal/installation-verification.json`.

## 1. Understand the three parts

- **Tram-in-Avenue** means tram tracks in the avenue's central strip, with car lanes beside them.
- A **transition lot** is a placeable object that transfers traffic between transport systems. The upper lot transfers tram passengers to the Subway network. It is not a passenger stop.
- **GLR**, or Ground Light Rail, is NAM's name for separate tram tracks on the ground. The lower hillside portal connects the Subway network back to these tracks.

The working route is:

`tram in upper avenue → avenue transition → Subway → hillside portal → separate tram tracks beside park`

The upper and lower entrances can be on different terrain heights. Your installed NAM Tunnel and Slope Mod includes **SubwayPipeDepthFix.dat**; NAM documents support for Subway construction across steep terrain changes. You do not have to make the upper district and park terrace the same height. Exact placement and track alignment still need an in-game check. [NAM slope guide](https://www.sc4nam.com/docs/feature-guides/tunnel-and-slope-mod/#slope-mod-characteristics)

This route uses ordinary **Subway connections between transition lots**. It does not use the older tram FLUP tunnel pieces. FLUP means Flexible Underpass; those pieces form a different construction system.

## 2. Reserve the upper entrance's space

Using your island screenshot as the reference:

1. Find the roundabout inside the HSR loop on the right-hand part of the island.
2. Follow the avenue arm from that roundabout toward the park at the bottom of the picture.
3. Choose a **straight section inside the HSR loop**, before the avenue reaches the elevated HSR and before the land slopes downward.
4. Reserve **two tiles across the avenue and three tiles along it**. A tile is one square of the game's map grid. This is six tiles in total.
5. Keep the complete rectangle clear of the HSR crossing, the roundabout and any bend. If the rectangle would overlap one of these, move the proposed entrance farther into the business district along the straight avenue.
6. Leave at least **one ordinary tram-in-avenue network tile along the route** between this entrance and a tram station. Traffic should not have to pass directly from one transit-enabled lot into another.

Choose locally level ground so the fixed ramp model and adjoining tracks align cleanly. This is a placement recommendation, not a measured maximum-slope rule. The installed lot permits steep terrain in its settings, but that does not guarantee a clean-looking result.

The screenshot does not establish an exact tile coordinate or prove that this entire footprint already fits. Position the placement preview before removing the existing avenue section.

## 3. Find and orient the upper entrance

1. Press **O** to open **Plop and Paint**.
2. Select **Buildings & Lots**.
3. Click the search field and type **Tram in Ave**.
4. Select the result named exactly **Tram in Ave to Subway/U-GLR Transition**.
5. Select its lot and choose **Plop** to display the placement preview.
6. Align its long, three-tile dimension with the avenue. Orient the visible surface-track end toward the roundabout, and the end where the tracks disappear toward the park.
7. Provide the required 2 × 3 gap in the avenue and place the transition there. Keep the adjoining tram-avenue and ordinary avenue connections aligned with its two ends.

The installed path records show that the two road carriageways remain at surface height through all three rows. Only the median tram tracks descend. You can therefore continue the ordinary avenue beyond the covered end toward its existing road tunnel.

## 4. Activate the upper surface connections

NAM's documented method for activating tram-in-avenue transit lots is to draw **One-Way Road through each of their two carriageways**. A carriageway is one half of the divided avenue, carrying traffic in one direction. [NAM tram guide](https://www.sc4nam.com/docs/feature-guides/light-rail-tram/#tram-in-network-dual-networking-options)

1. Select the game's **One-Way Road** drawing tool.
2. Draw a straight connection along one carriageway of the lot, following the same traffic direction as the adjoining avenue lanes.
3. Repeat along the other carriageway, in its opposite traffic direction.
4. Check that both ends join the adjoining avenue networks.

**Evidence limit:** these are NAM's general instructions for tram-in-avenue transit lots. The installed transition contains the corresponding avenue/one-way-road network-enabling records, but this precise drag sequence has not been tested on the lot in your running game. Its catalogue description does not supply a separate activation instruction. An Avenue drag or an Elevated Rail drag through this specific upper lot is not established here as a replacement procedure.

## 5. Connect both halves beneath the upper entrance

This is the important extra step for the avenue version. Its creator warns that an incomplete Subway connection can allow the morning commute while preventing the return journey.

1. Select the **Subway** drawing tool. This displays the underground network.
2. Locate the six tiles beneath the upper entrance: two columns across the avenue, each three tiles long.
3. Connect the three tiles under one carriageway lengthwise with Subway.
4. Do the same beneath the other carriageway.
5. Connect the two columns across **each of the three rows**. The result should resemble this small ladder:

```text
One side     Other side
   ●────────●
   │        │
   ●────────●
   │        │
   ●────────●
```

Every dot is a tile beneath the transition; none is an additional subway station. The lines represent Subway connections.

The creator specifies that the main outgoing tunnel should connect beneath the carriageway carrying incoming traffic. In the creator's illustrated orientation, this is the left-hand side for right-hand road traffic. **This does not mean the left side of your screen in every camera rotation.** The creator also allows tunnels from both halves, provided they connect to each other. Keep both halves linked to the same route to the park. [Creator's instructions for the NAM-integrated transition](https://community.simtropolis.com/forums/topic/4490-road-top-mass-transit-rtmt-development-and-support/?comment=1396966&do=findComment)

## 6. Place the lower hillside portal

Morifari's **Hillside GLR to Subway Transition** has two appearance variants: an urban version with a concrete base and a rural version with a grass base. Either serves the same type of connection. The concrete version suits the existing avenue-tunnel entrance; the grass version suits a softer park edge. [Publisher's description](https://community.simtropolis.com/files/file/14932-hillside-glr-to-subway-transition-by-morifari/)

The names stored in the downloaded archive are:

- **GLR-to-Subway tunnel entrance** — urban version; lot name **Hillside GLR to subway**.
- **GLR-to-Subway tunnel entrance, rural version** — grass version; lot name **Hillside GLR to subway (rural)**.

Both occupy **one map tile**, but the visible portal model extends beyond that tile. Check its full appearance in the placement preview rather than squeezing the one-tile footprint against the avenue tunnel or another object.

1. Locate the lower land beside the existing avenue-tunnel mouth, on the park side of the slope.
2. Choose a place where a separate tram track can leave the hillside and continue toward the park. The tram needs its own portal and surface track; it does not join the road tunnel.
3. Press **O**, choose **Buildings & Lots**, and search **GLR-to-Subway**. Select **GLR-to-Subway tunnel entrance** for the concrete version or **GLR-to-Subway tunnel entrance, rural version** for grass. Select its lot and choose **Plop**.
4. Orient the tunnel mouth toward the park and the rear of the portal into the hillside. Check the placement preview against the slope and adjacent avenue before placing it.
5. If the adjoining track end would sit above or below the lot's track, level the local approach enough to make the visual join clean. Do not assume a particular embankment height from this guide: the publisher does not prescribe one on the release page.
6. Connect the visible track end to separate GLR tracks leading into the park. The publisher notes that this lot automatically aligns to a nearby road, street or one-way road running **parallel** to those tracks; account for the existing avenue when checking its orientation.
7. With the **Subway** tool selected, connect the upper entrance's underground route to the lower portal's underground connection. The publisher explicitly instructs using Subway between tunnel entrances.

Place the park's tram stop farther along the visible track, with at least one ordinary track tile between it and the portal. The portal provides the tunnel connection; the stop provides a place for passengers to board and leave the tram.

## 7. Check the completed route

1. Confirm continuous surface connections into the upper entrance and out of the lower portal.
2. In Subway view, confirm that both halves of the upper lot are joined and that the underground route reaches the lower portal.
3. Supply power to the transition lots and stops, then let the simulation run long enough to calculate journeys.
4. Select **Route Query** and click an ordinary tram track or tram-avenue tile on the approach. Look for a commuter route that uses the tunnel connection and continues toward a real destination.
5. Check both the **morning** and **evening** journeys using the corresponding commute selection in the route/traffic view. Do not assume the evening direction works because the morning direction does.
6. Also query the avenue's road approaches to check that cars still pass through the upper entrance.

An unused route in an otherwise empty district does not prove a broken connection: passengers need homes and destinations that make this route useful. Conversely, watching a tram animation enter the ramp does not prove the entire route works. The tram-to-Subway conversion can make the visible tram disappear; use commuter routes to assess the transport connection.

## Evidence behind this guide

- Active catalogue: `/Users/simonhinterreiter/Documents/SimCity 4 Windows/Plugins/lots.cbor`.
- Upper lot: `RTMT_Tram_in_Avenue_to_Underground.SC4Lot.dat`, lot instance `7765b0f5`, footprint 2 × 3.
- Six installed support paths: `358695a6` through `358695ab`, in `GLR Dual-Networking-to-Subway LOTSupportPaths_RHD and LHD.dat`. These show surface road paths and the descending tram tracks.
- Lower-portal source: `/Users/simonhinterreiter/Downloads/morifari_GLR_to_subway.zip`. Urban lot instance `cf459904`; rural lot instance `ef45a073`; both have a 1 × 1 footprint. Their required custom GLR path `af1daca0` exists in the active NAM files. The shared prop and model are included in the archive.
- Archive properties and dependency checks, including the original capacity-field discrepancy, are recorded in `archive-and-dependency-audit.json`.
- [NAM tram construction and activation guide](https://www.sc4nam.com/docs/feature-guides/light-rail-tram/).
- [Transition creator's required Subway connection pattern](https://community.simtropolis.com/forums/topic/4490-road-top-mass-transit-rtmt-development-and-support/?comment=1396966&do=findComment).
- [Morifari hillside portal publisher's description](https://community.simtropolis.com/files/file/14932-hillside-glr-to-subway-transition-by-morifari/).

No city save, game plugin or profile setting was changed while preparing this guide.
