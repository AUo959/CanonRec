# G.U.S. Judicator Prime — Propulsion and Power Architecture

**Domain:** GUMAS L2 / Galactic Union  
**Artifact:** Propulsion and power specification  
**Architecture ID:** `JUDICATOR-POWER-001`  
**Version:** v1.0  
**Date:** 2026-07-21  
**Certainty:** STAGING  
**Parent asset:** `canon/L2/entities/mobile_assets/vessel_gu_001.json`  
**Parent architecture:** `JUDICATOR-ARCH-001 v1.1`  
**Authority:** Owner-authorized Judicator Prime architecture build

## 1. Purpose and certainty boundary

This specification converts the Judicator Prime's canonical propulsion and power anchors into a coherent working architecture without inventing a final drive physics model.

### 1.1 CANON anchors

The following are binding:

- the Judicator has **dual FTL cores**;
- the ship possesses an **emergency jump capability**;
- the ship operates long-range plasma lances, multi-layered energy shields, AI-coordinated point defense, tactical interceptors, a full Sentinel deployment wing, AI-resistant command systems, AI-Vanguard countermeasures, and an encrypted battle network;
- the vessel has an approximate normal complement of 12,000;
- Captain Alric Tann commands the vessel and its movement;
- hosted assets remain institutionally intact under `JUDICATOR-HOST-001`.

### 1.2 STAGING implementation

Everything below is provisional unless identified as a CANON anchor. In particular, this document does not establish the underlying physical mechanism of FTL travel, reactor type, fuel type, absolute power output, maximum jump range, or exact acceleration.

## 2. Governing design principles

### 2.1 Drive redundancy without fictional invulnerability

Two FTL cores provide isolation, maintenance flexibility, and emergency survivability. They do not make the ship immune to propulsion failure, navigation error, structural damage, or power depletion.

### 2.2 FTL and ship power are coupled but not identical

The FTL cores are not treated as ordinary ship-service reactors. Normal lighting, life support, medical systems, gravity, data systems, and most combat functions do not fail merely because one FTL core is isolated.

### 2.3 Strategic power requires visible tradeoffs

Plasma-lance firing, shield regeneration, emergency-jump charging, heavy sublight maneuver, and maximum carrier sortie activity compete for finite generation, storage, cooling, and distribution capacity.

### 2.4 Survival loads remain distributed

No single reactor, bus, capacitor bank, coolant loop, or control room is the sole source of continued life support, navigation, medical care, or internal communications.

### 2.5 Emergency jump is an extraction measure

Emergency jump exists to remove the Judicator from imminent catastrophic danger. It is not routine transportation, a consequence-free tactical dodge, or a substitute for navigation planning.

## 3. Dual-FTL topology

### 3.1 Core identities

The staged architecture assigns two operational identifiers:

- `JP-FTL-A` — Port FTL Core
- `JP-FTL-B` — Starboard FTL Core

These are functional identifiers, not manufacturer or technology names.

### 3.2 Physical separation

The cores occupy separate protected volumes within `JP-Z07`, divided by armored structural depth, independent access control, and isolation voids.

Each core provisionally receives:

- independent containment and shutdown systems;
- independent coolant loops and thermal isolation;
- independent local control rooms;
- independent navigation-solution validation channels;
- independent power-conditioning and charge interfaces;
- blast, radiation, field, and cascade isolation appropriate to the eventual drive physics;
- manual local shutdown capability;
- hardened links to the bridge, engineering control, emergency battle bridge, and encrypted battle network.

A casualty in one core compartment must not automatically propagate into the other.

### 3.3 Normal operating model

The preferred full-envelope jump model uses both cores in synchronized operation.

Provisional advantages of paired operation:

- lower load concentration on either core;
- better field symmetry across a supercarrier-scale hull;
- wider navigation and mass envelope;
- reduced structural stress during entry and exit;
- shorter recovery time than repeated single-core operation;
- improved tolerance for small calibration errors.

The cores may alternate lead duty between planned jumps to equalize wear and maintenance burden.

### 3.4 Single-core capability

Either core may provisionally execute a **degraded single-core jump** after the other core is safely isolated.

A single-core jump has staged limitations:

- reduced range or narrower route selection;
- longer charge and navigation-solution time;
- lower permissible ship mass asymmetry;
- stricter structural and shield-readiness requirements;
- greater thermal and maintenance burden on the active core;
- mandatory engineering inspection before another FTL event.

This capability preserves escape and mobility after serious damage without asserting that one core offers the full performance of two.

### 3.5 Core states

Each core may occupy one of five operational states:

| State | Meaning |
|---|---|
| `OFFLINE` | shut down, maintenance, or unavailable |
| `STANDBY` | contained and monitored; not jump-ready |
| `WARM` | active support systems; calibration underway |
| `READY` | validated for planned FTL use |
| `ISOLATED` | physically and logically separated after damage or anomaly |

`ISOLATED` is not equivalent to repaired or safe for reactivation.

## 4. Emergency-jump doctrine

### 4.1 Emergency-jump modes

#### `EJ-1` — Controlled emergency extraction

Both cores are available and a valid but compressed navigation solution can be produced. This is the preferred emergency mode.

Expected consequences:

- accelerated charge cycle;
- elevated structural and thermal stress;
- reduced destination precision relative to a planned jump;
- temporary reduction in shield recharge and strategic-weapon availability;
- mandatory post-jump drive, hull, navigation, and medical inspection.

#### `EJ-2` — Single-core emergency extraction

One core is unavailable or isolated. The remaining core performs a degraded emergency jump.

Expected consequences:

- materially shorter range or fewer valid destinations;
- greater stress on the active core;
- higher risk of inaccurate emergence;
- probable loss of immediate follow-on FTL capability;
- possible automatic isolation of the surviving core after arrival pending inspection.

#### `EJ-3` — Catastrophic-threat departure

A last-resort dual- or single-core departure undertaken when remaining in place presents an immediate likelihood of destruction.

`EJ-3` does **not** authorize a blind jump. A minimally valid navigation solution and collision-exclusion check are still required. The reduced process concerns precision, optimization, and system preservation—not the abandonment of causal navigation safety.

### 4.2 Authorization

Normal and emergency FTL movement remains a vessel-command function.

Provisional authorization chain:

1. Captain Tann, or the lawful acting commanding officer, orders the jump.
2. Navigation certifies a minimally valid route and emergence volume.
3. Chief Engineer Rhen Kailo, or the acting engineering authority, reports core state and known consequences.
4. Tactical Operations confirms the combat window and weapons posture.
5. Flight control reports recovery, securing, or disposition of exposed craft where time permits.

During an immediate catastrophic threat, the captain may order departure before every ordinary readiness condition is satisfied. Bypassed conditions are logged and reviewed.

### 4.3 Operational exclusions

The ship may not perform the following at full strategic output simultaneously:

- maximum-rate plasma-lance fire;
- maximum shield regeneration;
- full emergency-jump charge;
- maximum carrier launch tempo.

Command may maintain reduced levels of several functions, but an emergency-jump charge forces an explicit power and heat-allocation decision.

### 4.4 Craft and hosted assets

Emergency departure does not automatically grant the Judicator authority over the missions of hosted units, but Captain Tann may order immediate recovery, diversion, or abandonment of a launch window when vessel survival requires it under `JUDICATOR-HOST-001`.

Craft that cannot recover before an emergency jump may be:

- directed to an escort or alternate recovery platform;
- ordered to a prebriefed rendezvous;
- left operating independently under their own command;
- recovered only if the delay does not unreasonably endanger the Judicator.

The operational and human consequences of leaving personnel behind are documented rather than erased by the jump.

## 5. Primary power architecture

### 5.1 Generation model

The staged model uses **four primary generation plants** arranged as two separated pairs:

- `JP-PWR-1P` — Port Forward Primary Plant
- `JP-PWR-2P` — Port Aft Primary Plant
- `JP-PWR-1S` — Starboard Forward Primary Plant
- `JP-PWR-2S` — Starboard Aft Primary Plant

The technology and absolute output remain open.

The four-plant model allows:

- maintenance without shipwide shutdown;
- continued survival loads after loss of one plant;
- combat capability after loss of one side's generation pair;
- localized isolation after battle damage;
- separate conditioning for drives, shields, weapons, aviation, and ship services.

### 5.2 Auxiliary generation

Eight provisional auxiliary generator islands are distributed among command, engineering, flight, medical, logistics, and habitation zones.

Auxiliary systems are intended to sustain:

- life support and atmosphere control;
- medical and casualty systems;
- emergency lighting and internal communications;
- local gravity and compartment control;
- damage-control equipment;
- limited navigation, sensors, and maneuvering;
- safe FTL-core shutdown and containment;
- minimum launch or recovery support where physically possible.

Auxiliary generation does not support full plasma-lance fire, full shield regeneration, or normal FTL operation.

## 6. Power-distribution domains

### 6.1 Strategic Pulse Grid

High-energy domain for:

- FTL-core charging and field formation;
- plasma-lance charging and firing;
- rapid shield regeneration;
- emergency-jump preparation;
- major sublight acceleration events.

The Strategic Pulse Grid is heavily compartmented and normally disconnected from direct ship-service loads.

### 6.2 Combat Grid

Supports:

- point defense;
- sensors and tactical computation;
- AI-Vanguard countermeasures;
- encrypted battle-network infrastructure;
- sublight maneuvering;
- flight-spine launch and recovery;
- Sentinel deployment systems;
- weapons cooling and fire control.

### 6.3 Sustaining Grid

Supports:

- life support;
- medical systems;
- gravity and environmental control;
- habitation and food systems;
- internal transit;
- routine communications and data;
- evidence storage and legal systems;
- noncombat laboratories and administration.

### 6.4 Local emergency buses

Every major zone has at least one isolated emergency bus capable of receiving local auxiliary generation or limited cross-feed from another zone.

Cross-feed is controlled because unrestricted power sharing can propagate damage, cyber compromise, overload, or fire.

## 7. Energy storage and pulse management

Six provisional strategic energy-storage vaults are distributed away from both FTL cores and from one another.

They buffer short-duration demand for:

- plasma-lance firing;
- shield reinforcement;
- emergency maneuver;
- rapid interceptor launch;
- emergency-jump initiation.

The exact storage technology remains open.

A vault may be isolated after damage. Loss of one vault reduces surge performance rather than blacking out the ship.

Storage reserves are not unlimited ammunition. Repeated lance fire or shield recovery creates recharge time and heat debt even when generation plants remain intact.

## 8. Power priority doctrine

### 8.1 Default survival priority

Unless Captain Tann orders otherwise under immediate combat necessity, automatic load shedding protects:

1. FTL containment and safe shutdown
2. Life support and atmosphere integrity
3. Medical and casualty systems
4. Navigation, collision avoidance, and internal communications
5. Damage control and compartment isolation
6. Point defense and immediate ship protection
7. Shield continuity
8. Sublight maneuver and flight recovery
9. Battle network and strategic sensors
10. Plasma-lance charging and offensive sortie generation
11. Nonessential transit, habitation, laboratory, and administrative loads

This list governs automatic protection logic, not every tactical decision. Tann may reorder combat allocations while remaining accountable for consequences.

### 8.2 Lance–shield tradeoff

Full-power plasma-lance firing reduces the energy and cooling available for shield regeneration.

The ship may fire while shielded, but repeated full-power lance use creates a measurable defensive recovery penalty. This makes offensive commitment a command decision rather than a free background action.

### 8.3 Jump–combat tradeoff

Emergency-jump charging suppresses or limits:

- plasma-lance firing;
- maximum-rate shield recharge;
- high-energy electronic countermeasures;
- nonessential carrier launches;
- heavy industrial and fabrication loads.

Point defense, collision avoidance, life support, and core containment remain protected.

## 9. Sublight propulsion and maneuver

The staged sublight model includes:

- primary axial drive systems in the aft Engineering and Drive Spine;
- distributed maneuvering clusters across the hull;
- independent station-keeping and docking thrusters;
- protected low-output maneuver capability from auxiliary power;
- separate control and power paths sufficient to prevent one local failure from removing all attitude control.

Exact thrust technology, acceleration, inertial management, and fuel model remain open.

A two-kilometer supercarrier does not pivot or stop without consequence. Narrative and simulation must respect mass, clearance, escort geometry, and launch-recovery safety.

## 10. Thermal architecture

FTL charging, plasma-lance operation, shield regeneration, heavy acceleration, and carrier activity produce a shared thermal burden.

The staged system includes:

- multiple isolated coolant loops;
- distributed heat sinks;
- deployable or hull-integrated rejection systems appropriate to the eventual technology;
- emergency heat-storage capacity;
- sacrificial thermal isolation around damaged systems;
- independent medical and life-support cooling reserves;
- thermal forecasting integrated into tactical and engineering command.

The ship accumulates **heat debt** during high-output operations. Heat debt may force reduced lance rate, lower acceleration, slower shield recharge, or delayed FTL use even when power remains available.

## 11. Damage and degraded states

### `PWR-GREEN`

All primary plants, both FTL cores, and normal distribution paths available.

### `PWR-AMBER`

One primary plant or major bus unavailable. Full mission capability remains possible with reduced reserve.

### `PWR-RED`

At least one generation pair, strategic storage region, or FTL core unavailable. Offensive, carrier, shield, and jump capabilities require strict allocation.

### `PWR-BLACK`

Primary strategic generation is lost or unsafe. The ship survives on auxiliary islands and isolated sustaining buses. FTL, plasma lances, full shields, and normal carrier operations are unavailable.

### `CORE-SPLIT`

One FTL core is isolated; single-core degraded jump may remain possible.

### `CORE-LOCK`

Both FTL cores are unavailable or prohibited from activation. The ship remains sublight-mobile if other systems permit.

These states describe capability, not automatic mission outcomes.

## 12. AI-resistant control and human authority

Power and propulsion control must remain compatible with the canonical AI-resistant command architecture.

The staged model requires:

- independent human authentication for FTL activation;
- separate navigation and engineering concurrence channels;
- local manual isolation controls at each core and generation plant;
- non-AI degraded procedures for safe shutdown, basic maneuver, and survival power;
- physically and cryptographically segmented control domains;
- immutable logging of emergency overrides;
- no single autonomous system with unilateral authority to jump the vessel or fire a plasma lance.

AI may assist with forecasting, synchronization, fault detection, routing, and defensive coordination. Human command retains strategic movement and weapons authority.

## 13. Narrative and simulation invariants

Future scenes should preserve these constraints:

- the Judicator cannot jump instantly without charge, navigation, and readiness consequences;
- emergency jump is dangerous, logged, and operationally disruptive;
- one core may preserve degraded FTL mobility, but not full undamaged performance;
- loss of one FTL core does not automatically remove life support or ordinary ship power;
- loss of primary generation does not automatically destroy the FTL cores, but may prevent charging them;
- plasma-lance fire, shield regeneration, carrier tempo, and jump charging compete for resources;
- heat can constrain the ship even when power is technically available;
- hosted craft may be stranded or diverted by emergency movement;
- power damage creates regional and institutional consequences across a ship of 12,000 people;
- AI assistance does not erase accountable human command.

## 14. Promotion matrix

| Claim group | Disposition |
|---|---|
| Dual FTL cores | CANON |
| Emergency jump capability | CANON |
| Tann command authority over vessel movement | CANON |
| Paired normal operation | STAGING |
| Single-core degraded jump | STAGING |
| Emergency-jump mode taxonomy | STAGING |
| Four primary generation plants | STAGING |
| Eight auxiliary generator islands | STAGING |
| Strategic, combat, and sustaining grids | STAGING |
| Six strategic storage vaults | STAGING |
| Power-priority ordering | STAGING |
| Lance–shield and jump–combat tradeoffs | STAGING |
| Thermal heat-debt model | STAGING |
| Damage-state taxonomy | STAGING |
| Human-authentication and manual-control implementation | STAGING, CANON-compatible |

## 15. Open decisions

1. Ratify or revise paired-core normal operation.
2. Ratify whether either core can execute a degraded single-core jump.
3. Define the FTL mechanism, route model, range, and navigation requirements.
4. Define emergency-jump destination precision and recovery burden.
5. Ratify or revise the four-primary / eight-auxiliary generation model.
6. Define primary generation technology and fuel or energy source.
7. Define strategic storage technology and capacity.
8. Quantify the plasma-lance, shield, carrier, and jump power tradeoffs.
9. Define sublight drive and inertial-management technology.
10. Define thermal rejection technology and vulnerability.
11. Define the exact Radek, Drayen, flight-control, and hosted-asset procedures during an emergency jump.
12. Promote only after CanonRec review confirms consistency with `JUDICATOR-ARCH-001`, the vessel record, the ship registry, and `JUDICATOR-HOST-001`.
