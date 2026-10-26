# HSR circle and south-park tram

Current proposal, 16 September 2026. This replaces the earlier proposal to remove the HSR circle. **Keep the HSR loop**, build the business district inside it, and develop lower north/south waterfront parks connected by an eastern promenade. Extend the existing central tram into the southern park.

![Detailed district concept](/Users/simonhinterreiter/Documents/ChatGPT/Project_Sim_City/plans/hsr-loop-south-park-tram.png)

This is an illustrated design concept generated from your screenshot, not an implemented city or a tile-exact construction blueprint. Top of the image is called north for this plan. Exact terrain heights and placement need checking in the game. **17 September crossing correction:** a direct ground-level tram crossing under the existing HSR-style span was not found in the installed NAM 50 construction rules. Use the installed legacy tram FLUP tunnel crossing described in the [detailed crossing guide](</Users/simonhinterreiter/Documents/ChatGPT/Project_Sim_City/research/tram-under-hsr-2026-09-17/Findings and building guide.md>), or test the guide's Monorail-span workaround. The illustration does not show the required tram tunnel portals. Move the crossing to a straight HSR span; the line's smooth drawn bends represent a route corridor, and actual bends must use supported SimCity/NAM geometry.

## The route shown by A–E

- **A — Existing centre stop:** continue the existing tram south from the roundabout along the median (the strip between the two sides of the road).
- **B — Leave the avenue:** separate the tram from the road near the southern end of the central corridor. Let the road turn aside. Separate tram tracks keep a broad avenue from cutting through the park.
- **C — Pass under HSR:** use a short legacy tram FLUP tunnel beneath a straight HSR stretch. The installed crossing preserves HSR above and tram paths underground. Reserve a straight corridor for two three-tile tram ramps and the one-tile crossing. Keep the railway ring intact; confirm placement and traffic in-game.
- **D — Descend outside the circle:** use a long, gradual slope to reach the lower park terrace. A terrace is a flat shelf of land. Curve the route east/right of the visible southern tunnel entrance and leave the entrance's terrain untouched.
- **E — Park stop and plaza:** put the tram stop on flat, straight track beside a small arrival plaza and a few functioning commercial lots. Connect this area to the eastern promenade and the park paths. Keep the stop inland of the stone seawall.

As a design allowance, reserve approximately **8–12 map squares for the descent**, plus flat sections at its top and bottom. This is not a tested minimum: the required slope depends on the actual height difference. Do not automatically lower the park by 15 m. Fit a short shoreline/seawall sample first, then choose its final height.

## How to build the connection

The median in the screenshot appears to be **Tram-in-Avenue**. The transition instructions below assume that network. Ground Light Rail, shortened to **GLR**, is the NAM name for a tram on its own ground-level tracks.

1. Pause the city. Reserve the complete A–E corridor before placing buildings, trees or park lots within it.
2. Check **C first**, before shaping the descent. Find a flat location beneath a straight HSR span, crossing at a right angle on the map grid. Reserve at least the seven tiles occupied by the tram underpass components, plus approach space. Follow the detailed crossing guide linked above; simply drawing surface GLR beneath HSR is not a verified solution. Avoid the tightly curved part of the ring.
3. Open **Transportation → Miscellaneous Transportation**. Your setup includes a submenu named **Ground Lightrail**; look there if the tram tools are grouped rather than listed directly.
4. Select **Tram-Avenue (GroundLightRail / Avenue) - Dual Network Pieces**. Press **Tab** to cycle pieces, or **Shift+Tab** to cycle backward. Look for the description **Tram-Avenue transition to straight Tram and Avenue curve**. This piece lets the road curve away while the tram continues straight.
5. Rotate the transition with **fn + left arrow / fn + right arrow** on your Mac keyboard, and fit it at B on flat land. Its tram end must align with the existing tram tracks, not merely with the pavement. Leave sufficient space to use the piece's actual footprint. If the current endpoint does not fit, move B farther back within the business district instead of forcing the transition onto a bend.
6. Select **Draggable Ground Light Rail (Tram)** and place its starter on a clear part of the intended separate-track route. A starter is a small piece that tells the game which NAM network to draw.
7. Select the ordinary **Elevated Rail** drawing tool and draw through the GLR starter. The resulting line should convert to ground-level tram tracks. The tool name refers to the base game network; the GLR starter changes the resulting track to ground level.
8. Join this GLR line to the separated tram end at B. At C, place **Straight underground route under HSR (no pillar)** from the HSR puzzle-piece sequence and connect it to two inward-facing **Ramp for underground tram** pieces from **Tram-FLUPs - Flexible UnderPasses**. Join the surface GLR to the outside ramp ends. Fill any underground gaps with compatible legacy FLUP pieces; do not use the Subway tool for this version. The installed paths are verified, but placement and traffic in this city still need checking before shaping the long descent.
9. Beyond C, form the gentle terrain descent at D, staying clear of the road-tunnel entrance and its surrounding slope. Draw the GLR along it. Keep the crossing itself flat, and provide a flat area at E for the station.
10. Press **O → Buildings & Lots → Clear filters** and search **Orthogonal Tram Station by NOB**. This station is installed and occupies **2 × 1 map squares**. Orthogonal means aligned to the map grid rather than diagonal.
11. Select that building, select its lot below, and click **Plop**. Place it on a flat straight section at E, between GLR track sections. Do not select the similarly named **Orthogonal Tram-in-Avenue (TIA) Station by NOB**, which is for tracks remaining inside an avenue.
12. Draw the **Elevated Rail** tool through the separate GLR station to activate its track connections. Provide ordinary road/street access or a properly connected pedestrian network beside the stop. A decorative plaza is not a substitute for functional access.
13. Leave room for a short straight track section beyond the platforms. NAM offers optional loop starters for the visual finish; a second large loop is unnecessary for this plan.
14. After the track and station are connected, add the plaza, commercial lots, lawns and trees. Keep landscaping out of the reserved slope and crossing spaces.

The transition and station names above were checked in your installed NAM50 English text and O-menu catalogue. Their placement in this particular city has not been tested. Both separate GLR and Tram-in-Avenue can follow slopes; the separated route is a design choice, not a claim that avenue trams cannot descend.

## What to build around the tram

- **Inside the HSR ring:** concentrate the taller offices around the central streets. Keep some smaller buildings, plazas and trees next to the railway. Leave the route from A to B clear.
- **North park:** lawns, tree groves, paths and the installed Riprap Seawall. Protect the tunnel entrances and their immediate terrain.
- **South park:** a large lawn, shaded walking paths and a paved arrival area around E. Put the stop inland so the waterfront remains a continuous public walk.
- **East edge:** a promenade joining both parks, with a green buffer between it and the HSR. Use straight, diagonal and corner seawall pieces to follow the shore.

The small buildings, path patterns and lookout structures in the image illustrate the intended character; they are not a verified list of installed models. Useful installed building/lot search names include **Riprap Seawall**, **Small Plaza**, **Small Park Green**, **Medium Park Green** and **Large Park Green**.

Do not expect a decorative park alone to produce busy tram service. The traffic simulation primarily routes commuters to and from jobs; functioning commercial buildings near E give the line additional destinations. The extension can still be worthwhile as a scenic part of the city.

## References

- [NAM tram construction, crossings and station activation](https://www.sc4nam.com/docs/feature-guides/light-rail-tram/)
- [NAM HSR construction and crossing guidance](https://www.sc4nam.com/docs/feature-guides/high-speed-rail/)
- [NAM network additions and transitions](https://www.sc4nam.com/docs/feature-guides/base-network-additions/)
- [NAM slope specifications](https://www.sc4nam.com/docs/tech-specs/tunnel-and-slope-mod/)
- [NAM traffic simulator](https://www.sc4nam.com/docs/feature-guides/traffic-simulator/)
- [Installed stone seawall guide](/Users/simonhinterreiter/Documents/ChatGPT/Project_Sim_City/SimCity%204%20-%20Riprap%20Seawalls.md)

## Image generation

Made with the built-in image-generation tool using the original screenshot. The full prompt is saved in `hsr-loop-south-park-tram-prompt.md` beside this guide. No game files were changed.
