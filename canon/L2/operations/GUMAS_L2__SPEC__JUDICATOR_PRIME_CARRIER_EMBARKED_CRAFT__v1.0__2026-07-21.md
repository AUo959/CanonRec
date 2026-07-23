# G.U.S. Judicator Prime — Carrier Wing and Embarked-Craft Architecture

**Domain:** GUMAS L2 / Galactic Union  
**Artifact:** Carrier operations and embarked-craft specification  
**Architecture ID:** `JUDICATOR-CARRIER-001`  
**Version:** v1.0  
**Date:** 2026-07-21  
**Certainty:** STAGING  
**Parent asset:** `canon/L2/entities/mobile_assets/vessel_gu_001.json`  
**Parent architecture:** `JUDICATOR-ARCH-001 v1.1`  
**Power dependency:** `JUDICATOR-POWER-001 v1.0`  
**Combat dependency:** `JUDICATOR-COMBAT-001 v1.0`  
**Command doctrine:** `JUDICATOR-HOST-001`  
**Authority:** Owner-authorized Judicator Prime architecture build

## 1. Purpose and certainty boundary

This specification defines a working organization for the Judicator Prime's naval aerospace wing, launch and recovery system, utility and mission craft, Sentinel deployment interfaces, and independent hosted vessels.

### 1.1 CANON anchors

The following are binding:

- the Judicator is a supercarrier and Galactic Union flagship;
- the ship carries tactical interceptors;
- the ship hosts a full Sentinel deployment wing / strike unit;
- the ship is a command platform for Marshal-led strike forces;
- Captain Alric Tann commands vessel defense, launch, recovery, flight safety, and emergency movement;
- hosted Ranger, Marshal, Sentinel, diplomatic, intelligence, and specialist assets retain their parent chains under `JUDICATOR-HOST-001`;
- the Judicator possesses an encrypted battle network, AI-resistant command systems, AI-coordinated point defense, long-range plasma lances, layered shields, and emergency-jump capability.

### 1.2 STAGING implementation

The following remain provisional:

- exact craft counts and squadron organization;
- craft manufacturers, class names, crew sizes, performance, and armament;
- readiness percentages and sortie rates;
- launch-lane and recovery-corridor counts;
- Sentinel insertion craft and deployment methods;
- berth allocation and compartment identifiers;
- pilot-command titles below the established senior command roster;
- maintenance staffing and flight-personnel totals.

## 2. Governing principles

### 2.1 Naval aviation and hosted craft are distinct

The Judicator's naval aerospace wing is ship's company. Its squadrons, maintenance personnel, flight controllers, and standing missions belong to Captain Tann's naval chain.

Independent hosted craft use the ship's bays, services, flight corridors, and battle-network interfaces without becoming naval squadrons. Hosting does not transfer personnel, discipline, mission authority, or investigative control.

### 2.2 Flight safety is vessel authority

Every craft operating from the Judicator is subject to:

- launch and recovery clearance;
- shield-corridor timing;
- point-defense deconfliction;
- traffic control;
- bay safety and ordnance handling;
- quarantine and contamination controls;
- emergency recall, diversion, or launch suspension when vessel survival requires it.

These safety authorities do not become a pretext for taking control of a hosted unit's mission.

### 2.3 Sortie capacity is finite

The Judicator cannot launch, recover, refuel, rearm, repair, and coordinate every craft simultaneously. Carrier tempo is constrained by:

- lane and corridor availability;
- shield geometry;
- point-defense activity;
- power and heat allocation;
- maintenance capacity;
- crew fatigue;
- ordnance and fuel handling;
- battle damage;
- navigation and maneuver state.

### 2.4 Recovery is not guaranteed

A craft's parent command may authorize its mission, but the Judicator may be unable to recover it during shield breach, lane damage, emergency jump, severe point-defense activity, contamination, or unsafe approach geometry.

### 2.5 Human command remains attributable

AI may coordinate traffic, predict conflicts, optimize sequencing, and assist defensive vectoring. It may not independently create missions, change institutional command relationships, conceal flight records, or authorize strategic weapons.

## 3. Carrier spaces

### 3.1 Port Flight Spine — `JP-Z03`

The port spine provisionally contains:

- four rapid-launch lanes;
- two recovery corridors;
- armored marshalling hangars;
- interceptor and multirole maintenance lines;
- ordnance and power-cell handling;
- pilot ready rooms;
- flight-control stations;
- emergency craft shelters;
- local point-defense and shield-corridor coordination.

### 3.2 Starboard Flight Spine — `JP-Z04`

The starboard spine mirrors the port spine sufficiently to continue carrier operations after loss or isolation of one side.

The two spines may carry unequal mission loads. One may emphasize interceptors while the other concentrates strike, rescue, or utility craft.

### 3.3 Heavy Mission Bays — `JP-Z05`

The ventral Heavy Mission Bays support craft that are too large, too specialized, politically sensitive, or institutionally independent for ordinary squadron handling.

The staged berth plan remains:

- 12 independent gunboat or cutter berths;
- 6 modular special-mission berths;
- 4 diplomatic or command-shuttle berths;
- 8 heavy transport positions;
- 4 external docking collars;
- 12 hardened rapid-response cells shared among interceptors, rescue craft, Sentinel deployments, and mission-loaded shuttles.

### 3.4 Flight Operations Control

Flight Operations Control is a distributed function with primary stations in the Command Crown and both flight spines.

It maintains:

- traffic separation;
- launch and recovery sequencing;
- shield-corridor requests;
- point-defense deconfliction;
- approach validation;
- craft status and fuel state;
- diversion and alternate-recovery plans;
- bay damage and obstruction status;
- emergency-jump exposure lists.

Loss of one control station does not end flight operations if another station and sufficient local systems remain available.

## 4. Naval Aerospace Group

### 4.1 Command relationship

The staged organization creates a **Naval Aerospace Group** as a standing component of the Judicator's ship's company.

Its unnamed senior billet is provisionally:

- **Aerospace Group Commander** — responsible for naval aerospace readiness, training, squadron employment, and tactical recommendations.

Command flow:

1. Captain Tann sets vessel mission, defensive posture, and weapons authority.
2. Tactical Operations and Gunnery integrates aerospace action with ship combat and fleet operations.
3. The Aerospace Group Commander translates tasking into wing-level employment.
4. Squadron commanders control assigned personnel, craft readiness, and execution.
5. Flight Operations Control governs safe launch, recovery, and local traffic.

The Aerospace Group Commander does not command hosted Rangers, Sentinel missions, or diplomatic craft unless a mission order grants temporary coordinating authority.

### 4.2 Staged combat-craft envelope

The working model retains **144 naval combat aerospace craft**:

| Formation | Staged organization | Craft |
|---|---:|---:|
| Tactical interceptor squadrons | 6 squadrons × 16 | 96 |
| Multirole / strike squadrons | 3 squadrons × 16 | 48 |
| **Total** | **9 squadrons** | **144** |

Each 16-craft squadron is provisionally divided into four flights of four craft.

This structure defines planning units, not a claim that every airframe is operational, crewed, armed, or launch-ready at once.

### 4.3 Tactical interceptor mission

Tactical interceptors primarily provide:

- fleet and carrier defense;
- hostile strike-craft interception;
- missile and drone screening beyond point-defense range;
- escort of shuttles, cutters, and hosted craft;
- rapid identification of uncertain contacts;
- patrol and exclusion-zone enforcement;
- combat search and rescue cover;
- route clearance for Sentinel or Marshal deployments.

### 4.4 Multirole and strike mission

Multirole or strike craft primarily provide:

- attacks against hostile vessels and installations;
- suppression of hostile sensors and defensive systems;
- anti-ship and anti-surface missions within lawful rules of engagement;
- armed reconnaissance;
- escort and close support;
- electronic or sensor-support packages;
- response to threats too dispersed or mobile for plasma-lance employment.

Exact weapon types and atmospheric capability remain open.

### 4.5 Squadron readiness states

Each squadron reports craft through the following staged states:

| State | Meaning |
|---|---|
| `STOWED` | secured or in deep maintenance |
| `TURNAROUND` | inspection, recharge, refuel, repair, or rearm underway |
| `READY` | mission-configured and available for assignment |
| `ALERT` | crewed or immediately crewable for rapid launch |
| `AIRBORNE` | operating away from the ship |
| `DIVERTED` | assigned to alternate recovery or independent continuation |
| `GROUNDED` | unavailable by safety, damage, legal, quarantine, or command restriction |

Readiness is tracked at individual-craft level. Squadron totals are planning aggregates rather than all-or-nothing states.

## 5. Support and utility craft

The staged noncombat and mission-support envelope is:

| Category | Staged quantity |
|---|---:|
| Shuttles, medevac, and utility craft | 36 |
| Boarding and rescue cutters | 12 |
| Heavy transports | 8 |
| Command and diplomatic shuttles | 4 |

### 5.1 Utility craft

Utility craft support:

- personnel and cargo transfer;
- medical evacuation;
- maintenance access;
- inspection and repair;
- local transport;
- search and rescue;
- liaison and courier missions;
- controlled detainee or witness movement.

### 5.2 Boarding and rescue cutters

Cutters are designed for:

- boarding support;
- rescue and recovery;
- damaged-craft assistance;
- controlled evacuation;
- hazardous-scene access;
- security transport;
- emergency towing or stabilization within their eventual technical limits.

They remain naval craft unless specifically assigned to a hosted mission package.

### 5.3 Heavy transports

Heavy transports move:

- large cargo loads;
- replacement armor and ship components;
- ground vehicles or mission modules;
- humanitarian supplies;
- large personnel detachments;
- damaged equipment requiring internal recovery.

### 5.4 Command and diplomatic shuttles

These craft provide secure, politically controlled transport for:

- Union senior officials;
- diplomatic delegations;
- Judicial Council personnel;
- protected witnesses;
- Sentinel-Diplomat missions;
- command liaison and ceremonial arrival.

Their flight path, communications, and reception routes are separated from ordinary combat launch traffic when security permits.

## 6. Independent hosted craft

### 6.1 Berth categories

The twelve independent berths are provisionally allocated as:

- 8 long-duration Ranger / Marshal gunboat berths;
- 2 intelligence or special-operations berths;
- 2 flexible cutter, allied, or specialist-craft berths.

These are capacity categories, not permanently occupied slots.

Surge operations may temporarily accommodate additional crews through modular bays, external collars, transfer berths, or compressed maintenance cycles, but surge capacity reduces safety margin and routine efficiency.

### 6.2 Hosted-craft support package

Hosted craft may receive:

- protected berth and environmental services;
- recharge, fuel, and consumables;
- repair and fabrication;
- mission-specific equipment;
- secure communications;
- sensor and intelligence feeds;
- evidence-transfer support;
- medical and casualty access;
- drone servicing and replacement;
- launch, recovery, traffic, and navigation support.

Support does not transfer ownership or mission command.

### 6.3 *Third Measure* stable locations

The following recurring locations are created at `STAGING`:

- `JP-HMB-R07` — **Ranger Berth Seven**, assigned to the Ranger-class gunboat *Third Measure* during the sector special-service deployment;
- `JP-ENC-R03` — **Ranger Ready Suite Three**, assigned as the crew's planning, equipment, and secure briefing space in the Enclave;
- `JP-ENC-EV04` — **Evidence Transfer Lock Four**, the crew's normal controlled interface for moving sealed evidence from the gunboat into Marshal custody systems.

These identifiers create stable narrative geography without promoting the entire zone topology.

### 6.4 Ranger launch relationship

For a Ranger mission:

1. Marshal command authorizes the investigation or deployment.
2. The Ranger crew confirms craft, crew, evidence, weapons, and mission readiness.
3. Flight Operations Control assigns a launch sequence and safe corridor.
4. Point defense and shield control deconflict the departure.
5. The Ranger mission lead retains investigative command after launch.
6. The Judicator may provide intelligence, escort, relay, rescue, or escalation support through separate authorization.

The Aerospace Group Commander does not become the Ranger crew's mission commander merely because naval interceptors escort the gunboat.

## 7. Sentinel deployment wing

### 7.1 Institutional position

The full Sentinel deployment wing is canonically present but remains institutionally distinct from naval aviation.

Sentinel mission authority remains with the applicable Sentinel and Marshal command structure. The Judicator controls:

- safe embarkation and launch;
- bay and corridor access;
- shipboard weapons posture;
- traffic deconfliction;
- recovery and casualty transfer;
- quarantine, decontamination, and emergency restrictions.

### 7.2 Deployment methods

The staged architecture supports several mission-dependent methods without fixing a single universal system:

- armored shuttle or cutter deployment;
- covert low-observability insertion craft;
- rapid-response launch cells;
- suit-capable deployment interfaces;
- external transfer to another vessel;
- diplomatic-shuttle movement for Sentinel-Diplomat pairs;
- emergency rescue or extraction craft.

Exact craft classes, pod designs, launch physics, and headcount remain open.

### 7.3 Sentinel rapid-response cells

The twelve hardened rapid-response cells may be configured for:

- interceptor alert craft;
- Sentinel-loaded shuttles;
- rescue craft;
- medical extraction craft;
- mission-loaded utility vehicles.

Configuration changes require time, maintenance labor, safety checks, and mission planning. A cell is not simultaneously available for every role.

### 7.4 Diplomatic Sentinels

Sentinel-Diplomat pairs normally deploy as separate task-force assets.

They may use:

- secure diplomatic shuttles;
- low-profile protected transport;
- ordinary delegation movement under concealed security posture;
- independent protective routes through the Forum and Enclave.

They are not routinely attached to Ranger missions. Joint deployment requires a specific protective, political, investigative, or emergency basis.

A recurring preparation space is staged as:

- `JP-ENC-DIP02` — **Diplomatic Sentinel Preparation Suite Two**.

This does not establish the identities or total number of embarked Sentinel-Diplomats.

## 8. Launch and recovery doctrine

### 8.1 Separate authorizations

Every departure requires two distinct approvals:

- **mission authorization** from the craft's parent chain;
- **flight clearance** from the Judicator.

A craft with mission authorization may still be held for unsafe traffic, shield, damage, quarantine, or point-defense conditions. Flight clearance does not authorize the mission itself.

### 8.2 Launch sequence

A normal launch sequence includes:

1. craft and crew readiness confirmation;
2. mission and identification-code validation;
3. ordnance and hazardous-system confirmation;
4. assigned lane and departure vector;
5. shield-corridor synchronization;
6. point-defense deconfliction;
7. battle-network handoff;
8. physical launch;
9. corridor closure and local-defense restoration.

Experienced crews experience most of this as routine background procedure rather than repeated verbal exposition.

### 8.3 Recovery sequence

A normal recovery includes:

1. identity and approach validation;
2. damage, contamination, fuel, and casualty report;
3. assigned corridor and recovery queue;
4. point-defense and shield coordination;
5. capture, deceleration, or docking;
6. safing of weapons and hazardous systems;
7. medical, evidence, security, or maintenance transfer as required;
8. readiness-state update.

### 8.4 Recovery priority

Provisional priority is based on immediate risk rather than institutional prestige:

1. craft facing imminent loss, collision, or critical life-support failure;
2. medical evacuation and mass-casualty craft;
3. craft carrying uncontrolled hazardous damage or contamination requiring isolation;
4. ship-defense craft required for immediate survival;
5. time-critical rescue, Sentinel, Marshal, or command missions;
6. routine mission recovery;
7. training, administrative, and nonurgent traffic.

Captain Tann or delegated flight authority may alter priority for vessel survival, but deviations are logged.

### 8.5 Wave-off and diversion

Flight Operations Control may wave off or divert any craft when:

- the corridor cannot be protected;
- point defense cannot safely deconflict the approach;
- a shield sector is breached or isolated;
- the recovery spine is damaged;
- contamination threatens the ship;
- emergency jump preparation removes the recovery window;
- traffic density exceeds safe control.

Hosted craft retain their parent command after diversion.

## 9. Carrier interaction with combat systems

### 9.1 Plasma-lance firing

High-output lance fire may:

- close or delay launch corridors near the firing sector;
- require craft repositioning;
- produce thermal and power restrictions;
- expose a local shield adjustment;
- temporarily reduce recovery capacity.

Carrier and lance operations therefore require coordinated sequencing.

### 9.2 Shield corridors

Launch and recovery corridors are localized shield exceptions. They do not remove the whole defensive envelope, but they may create an exploitable local condition.

Point defense concentrates around an open corridor while preserving a safe channel for friendly craft.

### 9.3 Point-defense deconfliction

Every airborne friendly craft carries continuously updated identification, vector, and corridor data where communications permit.

If the battle network is compromised, point defense may shift to local defensive rules with narrower safe corridors, higher wave-off rates, and reduced carrier tempo.

### 9.4 Emergency jump

Before emergency jump, flight control classifies every deployed craft as:

- `RECOVERING`;
- `DIVERTING`;
- `INDEPENDENT`;
- `ESCORT-TRANSFER`;
- `UNRESOLVED`.

The ship does not erase missing or stranded personnel from the record merely because it jumps.

## 10. Maintenance and turnaround

### 10.1 Maintenance tiers

- **Line turnaround:** inspection, recharge, refuel, rearm, minor repairs, and software validation between sorties.
- **Intermediate maintenance:** component replacement, structural work, drive or control servicing, and mission-system reconfiguration.
- **Heavy maintenance:** deep overhaul requiring major hangar occupation, fabrication, or external dock support.

### 10.2 Hosted-craft maintenance

Naval technicians may service a hosted craft under agreed access rules. The parent unit retains authority over:

- mission data;
- evidence systems;
- restricted equipment;
- classified software;
- weapons authorization settings;
- institutional records.

A hosted unit may place observers or technicians in the maintenance process when compartmentation requires it.

### 10.3 Readiness integrity

Flight command may not report a craft as ready merely to satisfy sortie targets. Readiness records preserve known faults, deferred maintenance, crew limits, and mission restrictions.

## 11. Personnel and culture

### 11.1 Naval aviation community

The carrier wing forms a distinct shipboard culture with its own:

- ready rooms;
- maintenance teams;
- launch crews;
- flight controllers;
- rescue personnel;
- training cycles;
- losses and reputations.

The wing is large enough to have internal competition and squadron identity, but it remains part of the Judicator rather than an independent institution.

### 11.2 Hosted-unit social boundary

Rangers and other hosted personnel may become familiar faces in the Wells and flight-control system without becoming members of the wing.

This creates recurring friction:

- naval crews may see hosted craft receiving unusual priority or resources;
- hosted crews may view carrier procedures as centralized obstruction;
- naval maintenance may distrust undocumented field modifications;
- Rangers may resist being treated like squadron pilots;
- both sides may develop genuine respect through repeated operations.

### 11.3 Visibility and scrutiny

Every launch from the flagship creates records, witnesses, and institutional attention. A Ranger crew accustomed to remote autonomy now operates within a dense system of flight logs, maintenance reports, surveillance data, and senior observers.

## 12. AI-resistant control

AI may assist with:

- traffic prediction;
- launch sequencing;
- approach correction;
- collision avoidance;
- maintenance forecasting;
- fuel and energy planning;
- threat-vector deconfliction;
- rescue search patterns;
- local defensive coordination.

AI may not:

- launch a crewed craft without lawful authority except to prevent immediate physical destruction under a preauthorized safety rule;
- create a combat mission;
- override a parent command's mission cancellation;
- conceal a launch, recovery, diversion, or loss;
- assign hosted personnel into the naval chain;
- independently authorize strategic attack.

## 13. Degraded carrier states

| State | Meaning |
|---|---|
| `AIR-GREEN` | both spines and normal control systems available |
| `AIR-AMBER` | one lane group, corridor, or major support function degraded |
| `AIR-RED` | one flight spine isolated or severe defensive restrictions active |
| `AIR-BLACK` | routine carrier operations suspended; emergency local movement only |
| `WELLS-RESTRICTED` | Heavy Mission Bays operating under damage, quarantine, or security limits |
| `HOSTED-DIVERT` | independent craft directed to alternate recovery plans |

These states describe capability, not automatic mission outcomes.

## 14. Narrative and simulation invariants

Future scenes should preserve the following:

- the Judicator's wing is powerful but cannot all launch at once without preparation and risk;
- not every listed craft is always operational;
- pilots, deck crews, maintainers, and controllers are part of the cost of every sortie;
- launch and recovery require shield and point-defense coordination;
- a Ranger mission remains a Marshal mission even when naval fighters provide escort;
- hosted craft may be delayed, diverted, stranded, or left behind;
- carrier procedures are often routine and fast for experienced crews, but never physically consequence-free;
- the *Third Measure* has a stable berth and ready suite aboard the Judicator without becoming naval property;
- Sentinel deployments remain separately authorized and are not a generic extension of the carrier wing;
- Diplomatic Sentinels and Rangers normally operate as separate assets;
- emergency-jump preparation can force morally and operationally difficult recovery decisions;
- the flagship's launch records create visibility that remote Ranger crews do not normally experience.

## 15. Promotion matrix

| Claim group | Disposition |
|---|---|
| Supercarrier, tactical interceptors, Sentinel deployment wing | CANON |
| Tann launch/recovery and vessel-safety authority | CANON |
| Hosted-asset institutional independence | CANON |
| 144 naval combat-craft envelope | STAGING |
| Six interceptor and three multirole squadrons | STAGING |
| Four-flight squadron organization | STAGING |
| Support-craft quantities | STAGING |
| Dual flight-spine lane and corridor counts | STAGING |
| Independent berth allocation | STAGING |
| Ranger Seven / Ranger Ready Suite Three / Evidence Lock Four | STAGING |
| Sentinel deployment methods and rapid-response-cell use | STAGING |
| Diplomatic Sentinel Preparation Suite Two | STAGING |
| Aerospace Group Commander billet and subordinate command model | STAGING |
| Readiness states, recovery priorities, and degraded states | STAGING |

## 16. Open decisions

1. Ratify or revise the 144-combat-craft envelope.
2. Ratify or revise the 96-interceptor / 48-multirole split.
3. Decide whether the nine-squadron structure becomes canonical.
4. Define interceptor and multirole craft classes, crews, performance, and armament.
5. Define the Aerospace Group Commander as a formal billet and eventually mint its incumbent.
6. Resolve the exact naval relationship between Tactical Operations, Flight Operations Control, and the Aerospace Group Commander.
7. Define Sentinel deployment craft and methods without inferring Sentinel headcount.
8. Ratify the independent berth allocation and recurring location IDs.
9. Define normal readiness and sortie-tempo expectations.
10. Define escort and alternate-recovery doctrine for the current sector deployment.
11. Promote only after CanonRec review confirms consistency with the vessel record, hosted-asset doctrine, power architecture, and combat architecture.
