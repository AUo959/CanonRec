# G.U.S. Judicator Prime — Functional Architecture

**Domain:** GUMAS L2 / Galactic Union  
**Artifact:** Functional architecture specification  
**Version:** v1.1  
**Date:** 2026-07-21  
**Certainty:** STAGING  
**Parent asset:** `canon/L2/entities/mobile_assets/vessel_gu_001.json`  
**Parent class:** `canon/L2/entities/ship_classes/cls_judicator.json`  
**Parent doctrine:** `JUDICATOR-HOST-001`  
**Supersedes:** `GUMAS_L2__SPEC__JUDICATOR_PRIME_FUNCTIONAL_ARCHITECTURE__v1.0__2026-07-21.md`  
**Authority:** Owner-authorized Judicator Prime architecture pass, revised after the Judicator Prime Promotion Pass

## 1. Purpose and certainty boundary

This document defines the working functional architecture of the **G.U.S. Judicator Prime** as a Galactic Union flagship, supercarrier, Marshal strike-force command platform, Sentinel deployment vessel, cyberwarfare center, diplomatic platform, and long-duration campaign headquarters.

It distinguishes two evidence layers:

### 1.1 CANON system anchors

The following facts are binding and must be expressed by every later design:

- canonical vessel identity: `VESSEL-GU-001` / `CLASS-JUDICATOR-01` / `cls_judicator`;
- hull type: supercarrier;
- commanding officer: Captain Alric Tann;
- active flagship status;
- approximate complement: 12,000;
- command ship for Marshal-led strike forces;
- host to a full Sentinel deployment wing / strike unit;
- tactical interceptors;
- long-range plasma lances;
- AI-coordinated point defense;
- multi-layered energy shields;
- ablative armor plating;
- dual FTL cores with emergency jump capability;
- AI-resistant command systems;
- AI-Vanguard countermeasures;
- encrypted battle network;
- hosted assets remain institutionally intact under `JUDICATOR-HOST-001`.

### 1.2 STAGING implementation layer

The following remain provisional:

- hull dimensions and deck count;
- internal zone topology and crew shorthand;
- weapon count, mount type, firing arcs, range, cooling, and recharge;
- shield geometry, emitter count, recharge, and failure behavior;
- armor thickness, material composition, and replacement doctrine;
- FTL-core placement, operating physics, synchronization, fuel or power requirements, and emergency-jump limits;
- reactor and sublight-propulsion architecture;
- exact craft quantities and squadron organization;
- Sentinel strength and variant mix;
- facility capacities;
- detailed network segmentation and AI permissions.

Narrative and simulation may use the staged layer provisionally. CanonRec promotion is required before it becomes binding.

## 2. Design principles

### 2.1 Concentration without institutional collapse

The Judicator concentrates naval, Marshal, Sentinel, diplomatic, intelligence, scientific, medical, and logistical power without merging their chains of command or security domains.

### 2.2 Campaign endurance

The vessel supports sector-scale operations without constant planetary access: combat, investigation, detention, diplomacy, repair, medical care, intelligence analysis, personnel recovery, and fleet sustainment.

### 2.3 Distributed resilience

No single bridge, hangar, FTL core, data center, shield node, transit spine, or engineering compartment is the sole path to continued operation.

### 2.4 Human-scale navigation

Personnel experience the ship as linked functional districts, not an undifferentiated two-kilometer maze. Stable zone identifiers, express transit, compartment markers, and local service hubs are required.

### 2.5 Hosted-asset independence

Independent units receive secure facilities and protected routes to launch, medical, briefing, evidence, and support services without routine access to naval command compartments.

### 2.6 Attributable force

The Judicator's mass, cyberwarfare capability, aerospace wing, Sentinels, and long-range weapons create overwhelming potential force. Command architecture must preserve lawful authorization, human responsibility, evidence integrity, and reviewable escalation.

## 3. Staged scale envelope

| Field | STAGING value |
|---|---|
| Nominal length | approximately 2.1 km |
| Acceptable design range | 1.9–2.3 km |
| Maximum beam | approximately 760 m |
| Maximum hull depth | approximately 340 m |
| Principal pressurized decks | approximately 84, excluding interstitial service volumes |
| Normal complement | approximately 12,000, consistent with CANON vessel record |
| Short-duration surge capacity | approximately 15,000–16,000 |
| End-to-end express transit | approximately 8–12 minutes under normal conditions |
| End-to-end pedestrian transit | approximately 30–45 minutes, route dependent |

The 12,000 figure governs this vessel. Whether it is defined administratively as ship's company alone or as the normal campaign complement including routinely embarked assets remains open; functional planning treats it as the normal populated state of the ship.

## 4. Primary internal zones

Formal zone IDs and topology remain STAGING.

### `JP-Z01` — Command Crown

**Location:** dorsal-forward, behind the forward defensive and sensor envelope.  
**Working shorthand:** the Crown.

Contains:

- primary bridge;
- Combat Information Center;
- Flag Operations Center;
- Joint Operations Coordination Center;
- strategic communications and fleet-control rooms;
- command intelligence watch floor;
- secure command conference spaces;
- captain's and executive officer's working suites;
- protected access to the emergency battle bridge;
- hardened interfaces to the encrypted battle network.

The bridge commands the vessel. The CIC executes immediate combat. Flag Operations coordinates fleet and sector activity. Joint Operations supports temporary multi-institution missions without merging chains of command.

### `JP-Z02` — Defensive and Weapons Belt

**Location:** forward and distributed outer-hull armored volumes.  
**Working shorthand:** the Belt.

Contains or supports:

- long-range plasma-lance installations and power interfaces;
- AI-coordinated point-defense control;
- primary sensor arrays and sensor-processing rooms;
- multi-layer shield-distribution and control nodes;
- countermeasure and AI-Vanguard defense systems;
- ablative-armor inspection, isolation, and replacement access;
- hardened ammunition, energy, coolant, and power-routing trunks;
- forward damage-control stations;
- redundant tactical communications relays.

The plasma-lance count, mounting arrangement, arcs, and performance remain STAGING. The architecture assumes distributed point-defense and shield nodes so damage to one region does not remove the ship's entire defensive envelope.

### `JP-Z03` — Port Flight Spine

**Location:** port longitudinal carrier volume.  
**Working shorthand:** Port Wing.

Contains:

- armored internal hangars;
- tactical-interceptor marshalling and maintenance;
- rapid-launch lanes;
- recovery and deceleration corridors;
- aviation maintenance shops;
- fuel, power-cell, and ordnance handling;
- ready rooms and flight-control stations;
- emergency craft shelters.

### `JP-Z04` — Starboard Flight Spine

**Location:** starboard longitudinal carrier volume.  
**Working shorthand:** Starboard Wing.

Mirrors the Port Flight Spine sufficiently to preserve tactical-interceptor and support-craft operations after major damage, while allowing unequal mission loading.

### `JP-Z05` — Heavy Mission Bays

**Location:** ventral-midships.  
**Working shorthand:** the Wells.

Contains:

- heavy shuttle and cutter docks;
- independent Ranger, Marshal, intelligence, and specialist-craft berths;
- boarding and rescue-craft staging;
- modular mission bays;
- cargo transfer locks;
- diplomatic and command-shuttle docking;
- external docking collars;
- protected routes to the Marshal and Sentinel Operations Enclave.

The *Third Measure* and comparable hosted craft berth here without entering an ordinary naval squadron.

### `JP-Z06` — Marshal and Sentinel Operations Enclave

**Location:** protected midships mission complex adjacent to the Heavy Mission Bays.  
**Working shorthand:** the Enclave.

Contains:

- independent Marshal Operations Center;
- Ranger ready rooms and planning suites;
- secure evidence intake and custody vaults;
- forensic processing rooms;
- witness-protection and interview spaces;
- short-duration detention and protective-custody facilities;
- Judicial Council and Marshal-command secure links;
- Sentinel mission planning and command suites;
- Sentinel deployment-wing ready spaces;
- suit storage, maintenance, arming, decontamination, and medical interfaces;
- Sentinel-Diplomat preparation rooms;
- compartmented intelligence and special-operations cells;
- independent armories and mission-equipment stores.

The Enclave is not under ordinary naval mission command. Vessel command governs safety, access, shipboard weapons posture, launch conditions, and immediate emergency restrictions under `JUDICATOR-HOST-001`.

### `JP-Z07` — Engineering and Drive Spine

**Location:** axial-aft protected core.  
**Working shorthand:** the Forge.

Contains or supports:

- **two canonical FTL cores** in physically and operationally separated protected volumes;
- emergency-jump control and isolation architecture;
- primary and auxiliary power-generation nodes;
- sublight propulsion systems;
- weapons and shield power conditioning;
- engineering control rooms;
- fabrication and heavy-repair shops;
- coolant, atmosphere, and thermal-management plants;
- redundant life-support machinery;
- manual and degraded-mode control stations.

Dual FTL cores and emergency jump capability are CANON. Core location, independence, synchronization, performance, fuel or energy model, and emergency-jump consequences remain STAGING.

The architecture assumes distributed generation and control rather than one vulnerable reactor room. It does not yet assert that either FTL core can independently move the full vessel.

### `JP-Z08` — Logistics Keel

**Location:** ventral-aft and deep-midships cargo volumes.  
**Working shorthand:** the Keel.

Contains:

- long-duration stores;
- spare parts and fabrication feedstock;
- aviation and mission ordnance magazines;
- shipwide drone depots;
- ablative-armor replacement stock and handling capacity;
- cargo sorting and automated distribution;
- refrigerated, medical, and hazardous-material storage;
- large-component workshops;
- waste reclamation and recycling;
- damage-control reserves;
- fleet resupply interfaces.

The Keel enables campaign endurance and supports hosted assets without absorbing them administratively into the naval establishment.

### `JP-Z09` — Medical and Science Complex

**Location:** protected central volumes with direct access from mission bays, habitation, and express transit.  
**Working shorthand:** the Lantern.

Contains:

- main hospital and surgical center;
- trauma intake linked to carrier and mission bays;
- Sentinel medicine and powered-suit casualty interfaces;
- quarantine and contamination isolation;
- rehabilitation and cybernetic medicine;
- forensic medicine;
- modular research laboratories;
- captured-technology examination rooms;
- anomaly and materials laboratories;
- science operations control;
- medical surge wards.

STAGING planning capacity:

- approximately 250 acute-care beds under normal configuration;
- approximately 600 mass-casualty capacity through converted spaces;
- separated medical custody for detainees and protected witnesses.

### `JP-Z10` — Habitation, Civic, and Diplomatic Districts

**Location:** distributed central and dorsal-midships residential volumes.  
**Working shorthand:** the Hearth and the Forum.

Contains:

- crew quarters and messes;
- recreation, exercise, reflection, and social spaces;
- long-deployment counseling and morale services;
- administrative offices;
- delegation suites;
- formal conference chambers;
- neutral negotiation rooms;
- legal and political liaison offices;
- media and public-information spaces;
- secure diplomatic communications;
- protected diplomatic arrival routes separated from combat flight operations.

The district supports the Judicator-Class canonical role in high-level diplomacy without converting the bridge or Flag Operations Center into ceremonial space.

## 5. Command-space separation

### 5.1 Primary bridge

Navigation, maneuver, shipwide readiness, defensive posture, and execution of Captain Tann's vessel orders.

### 5.2 Combat Information Center

Immediate tactical picture, plasma-lance and point-defense employment, shield coordination, sensor fusion, countermeasures, and ship-combat execution under Tann and Tactical Operations.

### 5.3 Flag Operations Center

Fleet movement, escort operations, sector surveillance, strategic logistics, and naval campaign planning.

### 5.4 Joint Operations Coordination Center

Shared planning and real-time coordination for missions involving independent institutions. It creates no permanent authority; every joint operation requires a named lead and reserved-authority statement.

### 5.5 Marshal Operations Center

Marshal investigations, warrants, evidence, enforcement priorities, Ranger tasking, and Judicial Council liaison.

### 5.6 Sentinel Mission Control

Sentinel readiness, deployment-wing operations, suit deployment, mission-specific tactical planning, and Sentinel High Command coordination. The Radek/Drayen boundary remains mission-order dependent.

### 5.7 Cyberwarfare and network-defense command

A dedicated command function coordinates the encrypted battle network, AI-Vanguard countermeasures, intrusion response, cross-domain security, and degraded-mode continuity. Its exact physical placement and reporting structure remain STAGING; it may be distributed across the Crown, Belt, and specialist compartments rather than located in one room.

### 5.8 Emergency battle bridge

A physically isolated command node capable of navigation, defense, internal communications, emergency-jump initiation under lawful authority, and minimum launch/recovery control if the Crown is disabled.

## 6. Launch and recovery architecture

### 6.1 Flight spines

The Port and Starboard Flight Spines operate as independent carrier systems supporting the canonical tactical-interceptor role.

Each spine provisionally contains:

- four rapid-launch lanes;
- two primary recovery corridors;
- armored internal marshalling hangars;
- distributed ready rooms and flight-control stations;
- independent damage-control and emergency-seal capability.

Loss of one spine reduces sortie rate without ending carrier operations.

### 6.2 Heavy mission bays

STAGING berth plan:

- 12 independent gunboat/cutter berths;
- 6 modular special-mission berths;
- 4 diplomatic or command-shuttle berths;
- 8 heavy shuttle/transport positions;
- 4 external docking collars.

### 6.3 Sentinel deployment interfaces

The canonical Sentinel deployment wing requires:

- overt rapid-deployment routes;
- protected or low-observability mission routes;
- suit-safe launch and recovery interfaces;
- decontamination and casualty transfer;
- secure armament and mission-loading spaces;
- direct connection to Sentinel Mission Control.

Exact bay count and deployment method remain STAGING.

### 6.4 Rapid-response cells

Twelve provisional hardened cells permit interceptors, rescue craft, or mission-loaded shuttles to launch without clearing a complete hangar sequence.

### 6.5 Launch authority

Mission authorization and flight clearance remain separate:

- the parent command authorizes a hosted unit's mission;
- Judicator flight control authorizes safe launch and recovery;
- Captain Tann may delay, divert, recover, or suspend flight operations for lawful vessel-safety reasons;
- flight clearance may not be used as a pretext to assume investigative or Sentinel mission authority.

## 7. Staged embarked craft envelope

Canonical support-craft anchors are **tactical interceptors** and a **full Sentinel deployment wing**. Exact quantities remain STAGING.

| Category | STAGING nominal capacity |
|---|---:|
| Fighters / tactical interceptors | 96 |
| Multirole / strike craft | 48 |
| Shuttles, medevac, and utility craft | 36 |
| Boarding / rescue cutters | 12 |
| Independent Ranger, Marshal, intelligence, or specialist gunboats | 12 berths |
| Command / diplomatic shuttles | 4 |
| Heavy transports | 8 |
| Shipboard drones | Variable; mission and maintenance dependent |

The provisional 144-combat-craft total reflects supercarrier function but does not establish squadron names, manufacturers, readiness rates, or combat doctrine.

## 8. Embarked operational complements

### 8.1 Naval establishment

Bridge, combat systems, engineering, aviation, logistics, medical, science, administration, security, and ship services under Captain Tann's chain.

### 8.2 Sentinel deployment wing

A full Sentinel deployment wing / strike unit is CANON. Strength, squad distribution, and variant mix remain unresolved and must not be inferred from facility capacity.

The architecture supports:

- multiple squad-ready rooms;
- segregated suit-maintenance lines;
- covert and overt deployment routes;
- medical and decontamination support;
- one or more Sentinel-Diplomat pairs;
- mission-specific attachments from Sentinel High Command.

### 8.3 Marshal and Ranger presence

STAGING long-duration capacity:

- up to 8 Ranger crews in dedicated berths;
- up to 8 additional Ranger or specialist crews in surge configuration;
- one embarked Marshal command and liaison element;
- evidence, witness, interview, and temporary detention support for a sector campaign.

These berths primarily serve rotation, repair, staging, transfer, and exceptional assignments. Long-term supercarrier service remains unusual for Ranger crews.

### 8.4 Diplomatic and specialist detachments

The ship can host diplomatic missions, Sentinel-Diplomat pairs, Union Intelligence teams, scientific and technical detachments, Judicial Council personnel, medical or humanitarian teams, and allied delegations. They are normally employed separately unless a mission order establishes joint use.

## 9. Detention, evidence, and legal facilities

The Judicator is not a prison ship.

STAGING short-duration capacity:

- 96 standard secure detention positions;
- 16 high-security isolation positions;
- 24 protective-custody or witness positions;
- 12 medical-custody rooms;
- expandable emergency holding during mass boarding operations.

Detention requires lawful authority. Evidence and detainees retain separate chains of custody. Planetary transfer is preferred when lawful and secure. Medical access and Judicial Council review remain available.

## 10. Networks, cyberwarfare, and information boundaries

### 10.1 Canonical network anchors

The ship possesses:

- AI-resistant command systems;
- AI-Vanguard countermeasures;
- an encrypted battle network.

These are CANON capabilities, not legacy suggestions.

### 10.2 STAGING segmented-domain model

Provisional physically and cryptographically separated domains include:

- navigation and engineering;
- tactical systems and weapons;
- aviation and flight control;
- fleet command;
- Marshal evidence and operations;
- Sentinel operations;
- intelligence compartments;
- medical and scientific systems;
- diplomatic communications;
- public and crew services.

Cross-domain exchange passes through audited gateways. Hosted assets provide the minimum information required for safe launch, recovery, medical response, access control, and ship defense while preserving lawful compartmentation.

### 10.3 AI-resistant operation

The architecture reserves hardened manual controls, isolated command paths, independent authentication, degraded-mode procedures, and human-authorized weapons release. Exact AI permissions, model architecture, autonomy boundaries, and counter-intrusion procedures remain STAGING.

AI-coordinated point defense does not imply unrestricted autonomous strategic-weapons employment.

## 11. Propulsion, power, weapons, and defense integration

### 11.1 FTL

CANON:

- two FTL cores;
- emergency jump capability.

STAGING:

- core placement and separation distance;
- whether one core can move the entire vessel;
- synchronization and redundancy model;
- normal and emergency jump envelope;
- cooldown, navigation, and structural constraints;
- energy or fuel requirements;
- emergency-jump damage and review thresholds.

### 11.2 Power

The functional model assumes distributed primary and auxiliary generation, hardened power trunks, sectional isolation, and separate conditioning for shields, plasma lances, propulsion, flight operations, and life support. Reactor technology and output remain open.

### 11.3 Long-range plasma lances

Plasma lances are the canonical primary weapon family. Count, mounts, arcs, effective range, pulse or sustained behavior, power draw, thermal load, and planetary-employment rules remain STAGING.

Their architecture must support long-range fleet combat without turning every local Marshal operation into an implicit threat of strategic fire.

### 11.4 Point defense and countermeasures

AI-coordinated point defense and AI-Vanguard countermeasures are CANON. The design assumes distributed sensors, local fire-control continuity, human-governed engagement policy, and degraded operation if the battle network is compromised.

### 11.5 Shields and armor

Multi-layer energy shields and ablative armor are CANON. The functional design assumes overlapping shield regions, sectional isolation, replaceable sacrificial armor zones, and protected access for battle-damage assessment. Performance figures remain open.

## 12. Transit and internal movement

Three provisional movement layers:

1. **Axial express trunk:** high-speed end-to-end personnel and light cargo.
2. **District loops:** local transit among habitation, command, medical, flight, and mission zones.
3. **Service trunks:** restricted logistics, maintenance, ordnance, armor-replacement, and damage-control routes.

Hosted-asset routes connect the Heavy Mission Bays, Enclave, Medical and Science Complex, and diplomatic district without routine passage through the Crown.

Every major zone can be divided into independently pressurized compartments. No single transit line is the only path among command, engineering, medical, and launch functions.

## 13. Approximate population planning model

This is a functional planning model, not a full roster claim.

| Population group | STAGING planning figure |
|---|---:|
| Naval command, combat systems, security, and administration | 3,200 |
| Engineering, maintenance, and ship services | 2,600 |
| Aviation, flight deck, and aerospace support | 2,300 |
| Logistics, cargo, fabrication, and supply | 1,300 |
| Medical, science, intelligence, communications, and diplomatic staff | 1,000 |
| Embarked Marshal, Sentinel, specialist, and transient personnel | 1,600 |
| **Total** | **12,000** |

Operational deployments may alter the proportions without changing the governing approximate total.

## 14. Damage-control and continuity architecture

The continuity model includes:

- separation among bridge, CIC, Flag Operations, and emergency battle bridge;
- two independently operable flight spines;
- separated dual-FTL-core volumes and emergency isolation;
- distributed power generation and routing;
- distributed shield and point-defense control;
- multiple life-support and atmosphere-processing zones;
- decentralized damage-control stations;
- protected medical facilities near but not inside carrier and mission bays;
- separated ordnance, plasma-lance support, and hazardous stores;
- ablative-armor inspection and replacement routes;
- compartment-level isolation;
- manual and degraded controls for navigation, propulsion, defense, launch, recovery, and communications.

## 15. Narrative-use constraints

Future scenes should treat the Judicator as a large institution rather than a single room with a ship around it.

- Travel takes time unless express transit is used.
- Departments have separate priorities and access rules.
- Hosted units remain socially and operationally distinct from naval personnel.
- The ship's size creates resources, bureaucracy, visibility, and political audiences.
- A Ranger crew may stand close to overwhelming power while still waiting for lawful authorization, launch clearance, evidence review, or specialist availability.
- Damage to one bay, command room, shield node, FTL core, or network does not automatically disable the vessel.
- Emergency jump is a consequential capability, not routine scene transport.
- Plasma-lance availability does not erase proportionality, political consequence, or command review.
- The ship can dominate a battlespace but cannot manufacture legitimacy or lawful government through mass alone.

## 16. Promotion matrix

| Claim group | Current disposition |
|---|---|
| Flagship, supercarrier, Tann command, approximately 12,000 | CANON |
| Marshal strike-force role and hosted-asset doctrine | CANON |
| Senior command roster and Drayen embarked distinction | CANON |
| Long-range plasma lances | CANON |
| AI-coordinated point defense | CANON |
| Multi-layer energy shields and ablative armor | CANON |
| Dual FTL cores and emergency jump | CANON |
| Tactical interceptors and Sentinel deployment wing | CANON |
| AI-resistant command, AI-Vanguard countermeasures, encrypted battle network | CANON |
| 2.1 km scale and 84-deck model | STAGING |
| Ten-zone topology and crew shorthand | STAGING |
| Dual flight-spine and heavy-bay layout | STAGING |
| Craft quantities and rapid-response cells | STAGING |
| Ranger berth, detention, medical, and surge capacities | STAGING |
| Population planning breakdown | STAGING |
| Weapon mounts and performance | STAGING |
| Shield and armor performance | STAGING |
| FTL implementation and power architecture | STAGING |
| Network segmentation and AI permissions | STAGING |

## 17. Open decisions

1. Ratify or revise the staged scale envelope.
2. Clarify whether 12,000 is administratively ship's company or the normal total campaign complement.
3. Resolve the permanently embarked Sentinel command boundary between Major Elias Radek and Marshal-Captain Elias Drayen.
4. Define the dual-FTL-core topology, synchronization, and emergency-jump limits.
5. Define primary and auxiliary power generation.
6. Define plasma-lance count, mounts, firing arcs, and thermal cycle.
7. Define point-defense distribution and human/autonomous engagement boundaries.
8. Define shield layers, armor zones, and battle-damage replacement doctrine.
9. Ratify or revise the 144-combat-craft planning envelope.
10. Define the current sector-deployment event and escort group.
11. Decide which internal zone names become canonical crew language.
12. Create stable berth and compartment IDs for the *Third Measure*, Diplomatic Sentinels, and recurring narrative locations.
13. Promote only after CanonRec review confirms consistency with the vessel record, class record, Ship Registry, and hosted-asset doctrine.
