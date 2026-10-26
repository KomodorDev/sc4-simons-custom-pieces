# Regional agent research: NAM transport and high-speed rail

Research date: 7 September 2026. Read-only research; no game settings, plugins, or saves changed.

## 1. Scope and terminology

**HSR** means high-speed rail. **RRW** means RealRailway, NAM's conventional railway system. **HRW** means Hybrid Railway, which carries conventional railway and high-speed/monorail traffic on a combined network. A **recipe** below means a tested sequence of construction actions, with exact pieces, orientation, terrain requirements, and checks of the resulting paths. It is a proposed component of our agent, not a currently installed automation feature.

Local setup records confirm NAM 50, right-hand traffic, Low traffic capacity, original Maxis highways, RRW, HRW, HSR, and Ground Light Rail. The recorded NAM DLL is 1.3.1. The fresh startup log confirms the Eternal Commute Loop patch is active. Sources: `SimCity 4 - Setup Summary.md`, `setup/cam-install/startup-logs/NAM.log` lines 9–11.

## 2. Existing railway choices and real restrictions

| System | Documented behavior | Proposed role |
|---|---|---|
| RRW | The Rail tool constructs basic double track. Advanced geometry uses drag patterns and FLEX pieces. Single track is an override. | Conventional commuter service and freight; simpler initial construction library. |
| Legacy HSR / Ground HSR | Monorail overrides, started by placing a starter and dragging Monorail through it. | Dedicated express passenger corridors when the documented geometry is suitable. |
| HRW | Dual Rail + Monorail paths, mainly constructed from FLEX pieces. | Shared conventional/express approach tracks and station districts, after recipe validation. |

RRW is a replacement for the game's railway network, with advanced curves, turnouts, and elevated sections. A general instruction to draw Rail does not select every advanced shape. [NAM RRW guide](https://www.sc4nam.com/docs/feature-guides/real-railway/).

HSR is still described by the NAM team as legacy content; the successor, Real High Speed Rail, remains described as under development. HSR runs at Monorail's simulated 225 km/h, with capacity 10,000 per tile under the user's Low variant. Elevated HSR sits at 15.5 m and Ground HSR at approximately 1 m. Same-height road crossings are unsupported. Supported bridges exist, but functioning Monorail/HSR tunnels do not. Station lots require a Monorail drag through their track area. Ordinary Monorail train graphics appear unless a suitable replacement is installed. Therefore a tunnel shown on a proposed HSR plan must have a separately verified solution. [NAM HSR guide](https://www.sc4nam.com/docs/feature-guides/high-speed-rail/).

HRW supports both passenger railway and Monorail/HSR traffic. Most construction requires FLEX pieces; the guide additionally documents converting straight RRW tiles by clicking them with Monorail. Crossings usually require constructing network stubs from both sides. Appropriate HRW stations generally need Monorail dragged through them for both traffic types; using Rail alone gives only conventional rail service. The existing RRW on-slope transition is not interchangeable with the HRW version. [NAM HRW guide](https://www.sc4nam.com/docs/feature-guides/hybrid-railway/).

The HRW technical table explicitly lists **no HRW bridges and no HRW tunnels**. Elevated HRW is limited to straight orthogonal/diagonal segments at Level 1; elevated curves are unsupported. Crossing support depends on the other network, elevation, and geometry. Several tables contain unknown entries, which must stay unverified in our catalogue. [NAM HRW specifications](https://www.sc4nam.com/docs/tech-specs/hybrid-railway/).

**Recommendation/inference:** choose the railway family per corridor segment after considering its actual crossings. Avoid committing the entire region to HRW before proving how its rivers, mountains, borders, and stations will work. A subway conversion can provide an underground passenger connection, but should be represented as a change of simulated transport mode, with its own speed and transfer behavior. It should not be reported as an uninterrupted 225 km/h HSR tunnel.

## 3. A current NAM 50 restriction that changes regional route planning

The official DLL guide describes the Eternal Commuter Loop fix: through-commutes between a city's **North and West** neighboring edges are blocked; other directional combinations remain available. This is about traffic entering from one neighboring city and leaving for another, not physically preventing a North or West connection. [NAM DLL explanation](https://www.sc4nam.com/docs/feature-guides/nam-dll/#eternal-commuter-loop-fix).

I corroborated this in the released source. For a West-origin route the code excludes the Northern edge from standard destinations, and vice versa. Its final destination test rejects that neighbor-to-neighbor completion while preserving the local-lot branch. The small source comment states: “these patches only affect path searches involving neighbor connections”. The configuration defaults `EnableCommuteLoopPatch` to true. [DLL 1.3.1 source](https://github.com/NAMTeam/nam-dll/blob/1.3.1/src/CommuteLoop.cpp), [configuration](https://github.com/NAMTeam/nam-dll/blob/1.3.1/src/NAM.ini).

**Planning consequence/inference:** model allowed transitions between border connections, alongside their positions and transport type. Do not treat every pair of connections on an otherwise continuous track as an available regional through-route. A city can still receive workers at local jobs from either edge; that is a different trip from traversing the city. Tests should cover North–West through traffic, North–South through traffic, and commuters whose destination is inside the test city. Keep the installed fix enabled; plan around it.

## 4. Public transport requires useful journeys, not just track mileage

NAM's traffic simulator chooses faster journeys and uses the same defined speeds across capacity variants. The Low variant gives Rail, Monorail/HSR, and Subway/El-Rail/GLR capacity 10,000 per tile. Their documented speeds differ: passenger Rail 140 km/h, Monorail 225, El-Rail 115, Subway 105. These are simulation parameters, not timetable promises. NAM recommends a robust network with stations to encourage transit use. The former Traffic Simulator Configuration Tool was discontinued with NAM 45; the team explains that many former adjustments harm the redesigned Simulator Z 3.0. [Traffic simulator documentation](https://www.sc4nam.com/docs/feature-guides/traffic-simulator/).

Ground Light Rail uses starter overrides. Its station paths are activated by dragging Elevated Rail through the station. A bridge does not carry the override to the far side, which needs another starter. For tram/street combined networks, the recommended sequence is base street/road construction, zoning, then tram conversion. Border connections require the corresponding components on both cities' edges. [Light Rail/Tram guide](https://www.sc4nam.com/docs/feature-guides/light-rail-tram/).

**Proposed agent objective:** connect housing to actual jobs with a continuous walk–feeder–rail–feeder–walk journey. Reserve city-center station land first. Add walking connections, bus or tram feeders, conventional regional stops, express hubs, and only then grow the surrounding districts. Check passenger paths, station utilization, congestion, abandoned buildings, operating costs, and regional data freshness. Track kilometers alone cannot prove success.

## 5. Terrain and geometric routing

Slope-mod variants affect acceptable grades and how slopes change along a route. NAM documents separate maximum steepness and vertical curvature: a track may need more approach distance even if the average slope looks acceptable. Network construction can reshape terrain and may affect nearby development. [NAM Tunnel and Slope Mod](https://www.sc4nam.com/docs/feature-guides/tunnel-and-slope-mod/).

**Proposed solver:** find routes over a state that includes position, heading, height, and railway family. Each available recipe has a real footprint and entry/exit geometry. Reject unsupported curves/crossings before execution. Compare construction cost, travel time, excavation/fill, bridge requirements, demolition, protected land, and future expansion space. These are our proposed engineering choices; no existing NAM tool performs this complete regional optimization.

Use the installed exemplars and game tests to establish actual slope limits. Do not silently assume the separate NAM Tunnel and Slope Mod is installed because NAM itself is installed; the current setup summary does not establish that additional selection.

## 6. Construction recipe validation and live visibility

The first transport library should cover: straight RRW, basic curve, switch, station plus access; HSR starter and straight, HSR station, valid grade-separated crossing, bridge; paired city-border connection; GLR starter/station; then HRW straights, switches, stations, crossings, and transitions.

For every recipe, proposed verification is:

1. Read terrain, occupied cells, relevant network types, and installed asset identifiers.
2. Check the complete footprint and reserve it in the regional plan.
3. Show the game camera at the work site and label the current operation in the dashboard.
4. Execute the smallest useful construction batch, then allow a rendered frame.
5. Read the resulting network and paths; confirm the intended override and all needed traffic types.
6. For a station, verify boarding/alighting and onward pedestrian connections.
7. Run a controlled commute test and inspect route usage.
8. Save, reopen, and verify persistence before declaring the recipe reliable.

**Open technical question:** the built-in `PlaceNetwork` command exposes base network construction, but this does not establish a stable API for every NAM FLEX piece, starter, or bridge selector. A custom helper DLL or tested GUI/tool invocation may be needed for those operations. Avoid assuming lot placement and NAM puzzle-piece placement are interchangeable.

**Regional acceptance test:** a corridor crossing at least two city borders, joining populated housing and jobs, with a working express station and feeder connections in each major center. Validate both sides of every boundary after simulating the affected cities, verify the allowed border-to-border directions, show actual passenger routes, and preserve saves through reload. The user should see the active city, exact work area, planned/built/verified corridor status, and the latest measured result throughout execution.
