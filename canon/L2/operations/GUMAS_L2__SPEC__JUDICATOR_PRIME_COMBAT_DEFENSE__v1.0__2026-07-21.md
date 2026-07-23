# G.U.S. Judicator Prime — Combat and Defense Architecture

**Domain:** GUMAS L2 / Galactic Union  
**Artifact:** Combat systems and defensive architecture specification  
**Architecture ID:** `JUDICATOR-COMBAT-001`  
**Version:** v1.0  
**Date:** 2026-07-21  
**Certainty:** STAGING  
**Parent asset:** `canon/L2/entities/mobile_assets/vessel_gu_001.json`  
**Parent architecture:** `JUDICATOR-ARCH-001 v1.1`  
**Power dependency:** `JUDICATOR-POWER-001 v1.0`  
**Authority:** Owner-authorized Judicator Prime architecture build

## 1. Purpose and certainty boundary

This specification converts the Judicator Prime's canonical combat-system anchors into a coherent working architecture while preserving a strict distinction between established capability and generated implementation.

### 1.1 CANON anchors

The following are binding:

- long-range plasma lances;
- AI-coordinated point defense;
- multi-layered energy shields;
- ablative armor plating;
- AI-Vanguard countermeasures;
- an encrypted battle network;
- AI-resistant command systems;
- tactical interceptors and a full Sentinel deployment wing;
- dual FTL cores with emergency jump capability;
- Captain Alric Tann commands vessel movement, defensive posture, and shipboard weapons employment;
- hosted assets remain institutionally intact under `JUDICATOR-HOST-001`.

### 1.2 STAGING implementation

Everything below is provisional unless identified as a CANON anchor. In particular, this document does not canonize weapon counts, mount geometry, exact range, shield strength, armor composition, point-defense weapon types, repair rates, or numerical performance.

## 2. Governing combat principles

### 2.1 Command platform first

The Judicator is a flagship, supercarrier, and campaign headquarters. Its combat design prioritizes survival, fleet coordination, aerospace control, and lawful power projection over reckless line-of-battle attrition.

### 2.2 Long-range control

Plasma lances, tactical interceptors, sensors, countermeasures, and fleet coordination are used to shape the battlespace before hostile forces reach close engagement range.

### 2.3 Layered survival

Defense is sequential and overlapping:

1. detection and classification;
2. countermeasure and interception;
3. point defense;
4. multi-layer shields;
5. ablative armor;
6. compartmentation and damage control.

No single layer is treated as invulnerable.

### 2.4 Distributed continuity

Weapons, sensors, shield control, countermeasures, and local defense must continue in degraded regional modes if the encrypted battle network or Combat Information Center is damaged.

### 2.5 Attributable force

Strategic weapons release, shield sacrifice, populated-world fire, and other consequential actions remain accountable human command decisions. AI may coordinate, predict, route, and defend; it may not independently redefine the mission or authorize strategic attack.

## 3. Long-range plasma-lance architecture

### 3.1 Staged installation plan

The working design uses **six primary plasma-lance installations**:

- `JP-LANCE-F1` — Forward Axial Lance One;
- `JP-LANCE-F2` — Forward Axial Lance Two;
- `JP-LANCE-DP` — Dorsal-Port Arc Lance;
- `JP-LANCE-DS` — Dorsal-Starboard Arc Lance;
- `JP-LANCE-VP` — Ventral-Port Arc Lance;
- `JP-LANCE-VS` — Ventral-Starboard Arc Lance.

These identifiers describe functional placement, not manufacturers or final weapon names.

### 3.2 Forward axial lances

The two forward lances are staged as the ship's highest-output chase weapons.

They are:

- deeply embedded along reinforced forward structural lines;
- limited in traverse relative to the ship's orientation;
- optimized for long-range fleet targets, hardened installations, and major hostile vessels;
- dependent on deliberate maneuver and validated firing geometry;
- protected by armored shutters, isolation volumes, and independent cooling paths.

A maximum-output forward salvo requires the Judicator to present a constrained bow-on or oblique attack geometry. The ship cannot project maximum lance power equally in every direction.

### 3.3 Arc lances

Four lower-output but more flexible arc installations provide dorsal, ventral, port, and starboard engagement coverage.

They are staged to:

- engage targets outside the axial firing cone;
- maintain pressure during carrier maneuver or withdrawal;
- support layered fleet defense;
- combine in pairs or asymmetric salvos;
- remain independently isolatable after damage.

Their exact traverse, elevation, output relative to the axial lances, and mounting technology remain open.

### 3.4 Fire profiles

Three provisional firing profiles are defined:

| Profile | Function |
|---|---|
| `LANCE-PRECISION` | Reduced-output, tightly controlled shot against a validated point target; still a lethal strategic weapon |
| `LANCE-STRIKE` | Standard fleet-combat discharge balancing effect, recovery, and heat |
| `LANCE-OVERDRIVE` | Maximum authorized output with major power, thermal, structural, and recovery consequences |

`LANCE-PRECISION` is not a warning shot or a nonlethal setting.

### 3.5 Lance operating states

| State | Meaning |
|---|---|
| `COLD` | secured, maintenance, or unavailable |
| `WARM` | power conditioning and thermal preparation underway |
| `READY` | firing solution and system readiness validated |
| `COMMITTED` | charge allocated and firing sequence active |
| `LOCKED` | isolated after damage, anomaly, authorization hold, or safety failure |

A committed lance sequence may be aborted, but doing so may waste stored energy, add heat debt, or require inspection.

### 3.6 Power and heat constraints

Plasma lances draw from the Strategic Pulse Grid and distributed strategic-storage vaults established by `JUDICATOR-POWER-001`.

Repeated fire competes with:

- shield regeneration;
- emergency-jump charging;
- heavy sublight maneuver;
- high-tempo carrier operations;
- thermal recovery.

The ship may fire while shielded, but repeated maximum-output lance fire reduces defensive recovery and raises heat debt.

### 3.7 Shield interaction

A plasma-lance discharge requires a controlled local adjustment of shield geometry around the firing path.

This does not drop the entire shield envelope, but it may:

- temporarily reduce protection in the firing sector;
- create a detectable prefire signature;
- limit simultaneous local shield reinforcement;
- require precise coordination between weapons and shield control.

Enemy forces may attempt to exploit the firing window.

### 3.8 Weapons authorization

Normal plasma-lance release requires:

1. lawful target designation and positive identification;
2. a validated firing solution and exclusion check;
3. Tactical Operations readiness confirmation;
4. engineering confirmation of available power, cooling, and structural condition;
5. Captain Tann's order or lawful delegated weapons authority;
6. immutable battle-network logging.

No autonomous system may independently fire a plasma lance.

### 3.9 Planetary and civilian-space employment

Plasma-lance fire near inhabited worlds, civilian stations, protected infrastructure, or dense traffic requires extraordinary legal and command review unless an immediate catastrophic threat makes delay impossible.

The architecture rejects casual warning shots with strategic weapons. A lance discharge is an act of committed force with political, legal, and humanitarian consequences.

## 4. Multi-layer shield architecture

### 4.1 Three defensive layers

The working shield model uses three overlapping functions:

1. **Outer dispersal layer** — reduces debris, radiation, sensor, and low-energy impact burden before it reaches the main barrier.
2. **Main combat barrier** — absorbs, redirects, or disperses weapons effects across segmented combat sectors.
3. **Citadel hardening layer** — provides localized protection to critical command, drive, medical, magazine, and mission volumes when the outer envelope is degraded.

The exact field physics remain open.

### 4.2 Shield sectors

The main combat barrier is staged as **twelve independently managed sectors** distributed around the hull.

Each sector has:

- local emitter and control nodes;
- independent condition reporting;
- limited cross-feed from adjacent sectors;
- local isolation after damage or intrusion;
- access to strategic reserve power;
- a mapped relationship to armor districts and point-defense coverage.

A failed sector does not automatically collapse the entire shield envelope.

### 4.3 Shield rebalancing

Shield strength may be shifted toward a threatened sector, but rebalancing:

- takes finite time;
- consumes reserve energy and cooling;
- weakens one or more other sectors;
- may affect launch, recovery, sensor, or lance geometry;
- is logged as a tactical command decision.

The ship cannot maintain maximum reinforcement everywhere simultaneously.

### 4.4 Flight and docking corridors

Carrier launches, recoveries, docking, and Sentinel deployment require controlled shield corridors.

A corridor:

- remains open only as long as operationally necessary;
- is synchronized with flight control, point defense, and local shield stations;
- creates a localized defensive complication rather than a total shield failure;
- may be closed immediately if an inbound threat exceeds the recovery threshold.

Exposed craft do not gain guaranteed recovery merely because the ship is present.

### 4.5 Shield states

| State | Meaning |
|---|---|
| `SHIELD-NORMAL` | standard navigational and readiness envelope |
| `SHIELD-COMBAT` | full combat segmentation and active reserve allocation |
| `SHIELD-HARDENED` | one or more sectors receive extraordinary reinforcement |
| `SHIELD-DEGRADED` | reserve, emitter, cooling, or control losses reduce coverage |
| `SHIELD-BREACH` | one or more sectors cannot prevent direct armor exposure |
| `SHIELD-ISOLATED` | affected sector disconnected to prevent cascade or cyber propagation |

### 4.6 Regeneration and heat

Shield recovery requires both power and thermal capacity. A ship may possess sufficient generation yet remain unable to restore a sector rapidly because of emitter damage, coolant loss, field instability, or accumulated heat debt.

## 5. Ablative armor architecture

### 5.1 Armor purpose

Ablative armor is the physical survival layer beneath the shields. It is intended to absorb, redirect, vaporize, fragment, or carry away destructive energy while protecting the pressure hull and critical systems.

### 5.2 Layered armor model

The staged armor stack includes:

1. **Sacrificial exterior plates** — replaceable or repairable armor elements designed to be consumed under fire.
2. **Thermal and fragmentation layer** — limits heat transfer, spall, radiation, and secondary damage.
3. **Structural citadel armor** — protects pressure hull, magazines, command paths, drive compartments, medical spaces, and other critical volumes.

Materials and thickness remain open.

### 5.3 Armor districts

The exterior is staged as **twenty-four armor districts**, each mapped to:

- one or more shield sectors;
- local point-defense coverage;
- damage-control access;
- external inspection paths;
- Logistics Keel replacement stock;
- structural and pressure-hull boundaries.

Armor districts allow damage to be described and repaired regionally rather than through an undifferentiated hull-integrity percentage.

### 5.4 Replacement and repair

The Judicator carries replacement armor stock and handling capacity in `JP-Z08`.

Provisional repair levels:

- **combat patching:** drones, maintenance crawlers, sealants, and temporary plates restore pressure and limited protection under protected conditions;
- **campaign replacement:** damaged exterior sections are removed and replaced during reduced-threat operations;
- **dock-level reconstruction:** major structural armor and pressure-hull work requires a fleet yard, heavy tender, or equivalent infrastructure.

Combat patching does not reset a damaged district to factory condition.

### 5.5 Armor consequences

Loss of exterior armor may:

- increase thermal and radiation exposure;
- expose sensors, emitters, weapon interfaces, and service trunks;
- reduce safe acceleration or FTL readiness;
- force evacuation or isolation of adjacent compartments;
- alter the ship's sensor and emissions profile;
- increase the consequences of a second strike to the same district.

## 6. AI-coordinated point defense

### 6.1 Defensive mission

Point defense protects the Judicator and nearby assigned craft against:

- guided munitions;
- strike craft and attack drones;
- boarding pods and hostile shuttles;
- terminal-stage kinetic or energy threats;
- hazardous debris created during combat;
- coordinated saturation attacks.

Exact effector types remain open.

### 6.2 Distributed defense sectors

The working model uses **twenty-four independently controlled point-defense sectors**.

Each sector contains multiple sensor, tracking, fire-control, and effector nodes. Exact node count and weapon mix remain STAGING.

Each sector can operate in:

- battle-networked mode;
- local cooperative mode with adjacent sectors;
- isolated local-defense mode if central links fail;
- manual degraded mode under human control.

### 6.3 AI coordination boundary

AI may:

- fuse sensor tracks;
- predict intercept geometry;
- allocate nonconflicting effectors;
- deconflict friendly craft and shield corridors;
- prioritize terminal threats within approved rules;
- maintain local defense after network damage;
- detect saturation patterns and adversarial manipulation.

AI may not:

- redefine protected or hostile categories;
- authorize strategic attack;
- conceal engagement records;
- fire on a crewed craft outside approved defensive rules unless it presents an immediate terminal threat;
- override a lawful human weapons hold without a documented last-resort collision or impact condition.

### 6.4 Point-defense operating modes

| Mode | Function |
|---|---|
| `PD-GUARD` | tracking and passive readiness; no routine automatic engagement |
| `PD-INTERCEPT` | automatic engagement of validated inbound munitions within approved defensive rules |
| `PD-CLOSE` | maximum terminal defense with reduced safety margins and heightened friendly-fire risk |
| `PD-ISOLATED` | local sector defense after network or command separation |
| `PD-HOLD` | weapons held by command, safety, legal, or identification constraint |

`PD-CLOSE` requires explicit command authorization unless a preauthorized catastrophic-impact condition is met.

### 6.5 Friendly-craft protection

Carrier operations require constant deconfliction among interceptors, shuttles, Ranger craft, Sentinel deployments, shield corridors, and point-defense fire.

Flight control and point defense share a protected coordination layer but retain separate authority. Point defense may close a corridor or force a craft diversion when an inbound threat makes recovery unsafe.

## 7. AI-Vanguard countermeasures and electronic defense

### 7.1 Purpose

AI-Vanguard countermeasures defend the Judicator against adversarial autonomous systems, corrupted targeting logic, hostile machine coordination, deceptive sensor environments, and attempts to exploit Union battle-network dependence.

### 7.2 Staged capabilities

The working architecture includes:

- adversarial-pattern detection;
- independent track validation;
- false-target and signature-discrimination systems;
- controlled decoy and deception deployment;
- hostile-link disruption and spectrum denial;
- command-authentication verification;
- quarantined analysis environments for captured or suspect machine code;
- automatic network segmentation after anomaly detection;
- manual and non-AI fallback procedures.

### 7.3 Countermeasure distribution

Countermeasure systems are distributed across the Command Crown, Defensive and Weapons Belt, flight spines, intelligence compartments, and local defense sectors.

No single cyberwarfare room is the only source of AI resistance.

### 7.4 Deception and decoys

The Judicator may deploy remote decoys, false signatures, communication ghosts, and controlled emissions to complicate hostile targeting.

These systems:

- do not falsify the internal command record;
- require deconfliction with friendly forces and civilian traffic;
- may be locally controlled if the battle network is segmented;
- cannot substitute for legal target identification by the Judicator's own command.

## 8. Combat Information Center and distributed control

### 8.1 Central command

The Combat Information Center coordinates:

- plasma-lance employment;
- point-defense posture;
- shield allocation;
- countermeasures;
- tactical sensors;
- combat maneuver;
- flight and recovery conflict resolution;
- power and heat tradeoffs with Engineering;
- fleet-level data exchange with Flag Operations.

Captain Tann retains weapons and defensive-posture authority. The Tactical Operations and Gunnery Chief executes that authority within delegated limits.

### 8.2 Local control stations

Local control stations in the Defensive and Weapons Belt can:

- isolate damaged systems;
- maintain regional sensors and point defense;
- preserve shield-sector control;
- safe or lock a lance installation;
- continue manual defensive action if the CIC is unavailable.

Local stations do not acquire independent strategic-weapons authority merely because central command is damaged.

### 8.3 Emergency command continuity

The emergency battle bridge can command minimum defensive systems, authorize emergency jump, maintain local point defense, and preserve lawful weapons holds.

Loss of the Crown is a severe command casualty, not automatic loss of the ship.

## 9. Combat doctrine

### 9.1 Preferred engagement sequence

A normal fleet engagement favors:

1. long-range detection and identification;
2. countermeasure and deception shaping;
3. tactical-interceptor deployment;
4. fleet positioning and escort coordination;
5. selective plasma-lance fire;
6. layered point-defense and shield management;
7. withdrawal, emergency extraction, or close engagement only when required.

### 9.2 Orientation and fresh-sector doctrine

Because lance arcs, shield strength, armor condition, launch corridors, and damaged systems are not uniform, Tann may maneuver to:

- expose a stronger shield sector;
- rotate damaged armor away from hostile fire;
- bring axial or arc lances onto target;
- protect an active recovery corridor;
- place escorts between a breached sector and the threat;
- prepare an emergency-jump alignment.

The Judicator's size means such maneuvers require time, clearance, and fleet coordination.

### 9.3 Carrier and weapons coordination

Maximum lance output, shield reinforcement, and maximum launch tempo cannot all be sustained simultaneously.

The ship may choose among postures such as:

- **carrier dominance:** prioritize interceptors, recovery, sensors, and point defense;
- **lance engagement:** prioritize strategic fire and forward shield support;
- **defensive citadel:** prioritize shields, point defense, damage control, and protected recovery;
- **extraction preparation:** preserve point defense and survival systems while charging emergency jump.

These are planning postures, not rigid software presets.

### 9.4 Marshal campaign constraint

The presence of plasma lances and a supercarrier does not convert every Marshal operation into a military strike.

Weapons availability remains bounded by:

- jurisdiction;
- proportionality;
- civilian risk;
- evidentiary integrity;
- political consequence;
- Captain Tann's vessel authority;
- the independent mission authority of hosted Marshal assets.

## 10. Damage states

### 10.1 Overall defensive state

| State | Meaning |
|---|---|
| `DEF-GREEN` | full sensor, shield, armor, countermeasure, and point-defense availability |
| `DEF-AMBER` | one or more sectors degraded; full mission remains possible with reduced reserve |
| `DEF-RED` | shield breach, major armor loss, or regional defensive isolation materially constrains maneuver and mission |
| `DEF-BLACK` | strategic defense network unavailable; only local, manual, or isolated systems remain |

### 10.2 Regional state

Each shield, armor, and point-defense sector records:

- available;
- degraded;
- isolated;
- breached;
- destroyed or inaccessible;
- under repair;
- safe only for restricted operation.

### 10.3 Combat-system casualty rules

Future narrative and simulation should preserve:

- loss of one lance does not remove all strategic fire;
- loss of one shield sector does not collapse every shield;
- armor damage remains physically meaningful after shields recover;
- battle-network loss does not eliminate all local point defense;
- point-defense failure does not automatically imply shield failure;
- repeated strikes to a damaged district become increasingly dangerous;
- recovery and repair consume time, stores, personnel, and protected operating windows.

## 11. Human authority and audit

### 11.1 Plasma-lance release

Plasma-lance fire always requires accountable human authorization.

### 11.2 Defensive automation

AI-coordinated point defense may act automatically within a preauthorized defensive envelope against validated terminal threats. Engagement rules, exclusions, and overrides are logged and reviewable.

### 11.3 Shield sacrifice

Deliberately weakening one shield sector to protect another, open a launch corridor, fire a lance, or prepare a jump is a consequential command action when personnel or critical systems are exposed.

### 11.4 Record integrity

The encrypted battle network records:

- target identification;
- firing solutions;
- weapons-release authority;
- shield and power allocations;
- point-defense rules and engagements;
- countermeasure deployment;
- local overrides;
- damage and casualty reports;
- emergency departures and abandoned recovery windows.

No AI or officer may silently rewrite the combat record.

## 12. Narrative and simulation invariants

Future scenes should preserve these constraints:

- the Judicator has firing arcs and cannot apply maximum lance power equally in all directions;
- plasma-lance fire creates power, heat, signature, and local shield consequences;
- shields are segmented and can be strengthened, weakened, isolated, or breached regionally;
- armor damage survives shield recovery and affects later operations;
- point defense is distributed and may continue locally after network damage;
- AI coordinates defense but does not autonomously control strategic violence;
- launch and recovery corridors create local defensive complications;
- no single hit, corridor, turret, or shield node automatically determines the entire battle;
- the ship's size makes orientation, repair, and recovery consequential;
- strategic weapons do not solve legitimacy, jurisdiction, or civilian-risk problems.

## 13. Promotion matrix

| Claim group | Disposition |
|---|---|
| Long-range plasma-lance weapon family | CANON |
| AI-coordinated point defense | CANON |
| Multi-layered energy shields | CANON |
| Ablative armor plating | CANON |
| AI-Vanguard countermeasures and encrypted battle network | CANON |
| Six-lance installation plan | STAGING |
| Two axial and four arc-lance topology | STAGING |
| Lance fire profiles and operating states | STAGING |
| Twelve shield sectors and three-layer function | STAGING |
| Twenty-four armor districts | STAGING |
| Twenty-four distributed point-defense sectors | STAGING |
| Shield firing corridors and local lance windows | STAGING |
| Armor replacement and campaign-repair doctrine | STAGING |
| AI defensive permissions and point-defense modes | STAGING |
| Combat postures and damage-state vocabulary | STAGING |

## 14. Open decisions

1. Ratify or revise the six-lance installation plan.
2. Define final lance arcs, output relationships, range, and recharge behavior.
3. Decide whether the axial lances are fixed, minimally trainable, or mounted through another architecture.
4. Ratify or revise the twelve-sector shield model.
5. Define shield physics, recharge behavior, emitter topology, and citadel coverage.
6. Ratify or revise the twenty-four armor districts and repair levels.
7. Define armor materials, thickness, stock burden, and replacement time.
8. Ratify or revise the twenty-four point-defense sectors.
9. Define point-defense effector families and ammunition or energy logistics.
10. Define AI-Vanguard countermeasure permissions, offensive cyber limits, and civilian-spectrum rules.
11. Define populated-world plasma-lance employment doctrine in formal legal language.
12. Promote only after owner review and CanonRec conflict scan.
