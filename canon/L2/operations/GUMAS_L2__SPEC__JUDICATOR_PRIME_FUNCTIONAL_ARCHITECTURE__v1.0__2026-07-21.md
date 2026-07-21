# G.U.S. Judicator Prime — Functional Architecture

**Domain:** GUMAS L2 / Galactic Union  
**Artifact:** Functional architecture specification  
**Version:** v1.0  
**Date:** 2026-07-21  
**Certainty:** STAGING  
**Parent asset:** `canon/L2/entities/mobile_assets/vessel_gu_001.json`  
**Parent doctrine:** `JUDICATOR-HOST-001`  
**Authority:** Owner-authorized Judicator Prime build pass  

## 1. Purpose and authority boundary

This document defines the working functional architecture of the **G.U.S. Judicator Prime** as a Galactic Union flagship, supercarrier, Marshal strike-force command platform, Sentinel deployment vessel, and long-duration campaign headquarters.

The following facts are already CANON and govern every staged design choice below:

- canonical vessel identity: `VESSEL-GU-001` / `CLASS-JUDICATOR-01`;
- hull type: supercarrier;
- commanding officer: Captain Alric Tann;
- approximate embarked population: 12,000;
- active flagship status;
- command ship for Marshal-led strike forces;
- host to a full Sentinel strike unit;
- hosted assets remain institutionally intact under `JUDICATOR-HOST-001`.

Dimensions, zone topology, internal capacities, craft complements, and facility sizing introduced here are STAGING. They may be used in narrative and simulation as provisional constraints but require owner promotion before becoming binding CANON.

## 2. Design principles

### 2.1 Concentration without collapse

The Judicator concentrates naval, Marshal, Sentinel, diplomatic, intelligence, scientific, medical, and logistical power without merging their chains of command or security domains.

### 2.2 Campaign endurance

The vessel is built to sustain a sector-scale campaign without depending on constant planetary access. It must support combat operations, investigation, detention, diplomacy, repair, medical care, intelligence analysis, and personnel recovery over extended deployments.

### 2.3 Distributed resilience

No single bridge, hangar, reactor room, data core, or transit spine may be the only path to continued operation. Critical functions are separated physically and logically so the ship can fight, recover craft, sustain life, and retain lawful command after major damage.

### 2.4 Human-scale navigation

Although the ship is very large, personnel should experience it as a network of functional districts rather than an undifferentiated maze. Stable zone identifiers, express transit, compartment markers, and local service hubs are required.

### 2.5 Hosted-asset independence

Marshal, Ranger, Sentinel, diplomatic, intelligence, scientific, and other independent units receive dedicated facilities and secure access routes. They can reach launch bays, briefing rooms, medical care, and support services without routine entry into naval command spaces.

## 3. Staged scale envelope

| Field | STAGING value |
|---|---|
| Nominal length | approximately 2.1 km |
| Acceptable design range | 1.9–2.3 km |
| Maximum beam | approximately 760 m |
| Maximum hull depth | approximately 340 m |
| Principal pressurized decks | approximately 84, excluding interstitial service volumes |
| Normal embarked population | approximately 12,000, consistent with CANON vessel record |
| Short-duration surge capacity | approximately 15,000–16,000 |
| End-to-end express transit | approximately 8–12 minutes under normal conditions |
| End-to-end pedestrian transit | approximately 30–45 minutes, route dependent |

The approximate 12,000-person figure is treated as the normal campaign population, including naval ship's company and routinely embarked operational personnel. CanonRec does not yet establish whether it is a strict crew-only count.

## 4. Primary internal zones

The ship is divided into ten major functional zones. Formal zone IDs are stable; crew shorthand is STAGING cultural language.

### `JP-Z01` — Command Crown

**Location:** dorsal-forward, deeply armored behind the forward sensor and defensive envelope.  
**Crew shorthand:** the Crown.

Contains:

- primary bridge;
- Combat Information Center;
- Flag Operations Center;
- Joint Operations Coordination Center;
- strategic communications and fleet-control rooms;
- secure command conference spaces;
- command intelligence watch floor;
- captain's and executive officer's working suites;
- protected access to the emergency battle bridge.

The Crown is not one room. The bridge commands the vessel; the Combat Information Center manages the ship's tactical picture; the Flag Operations Center coordinates fleet-level operations; the Joint Operations Coordination Center supports lawful multi-institution missions.

### `JP-Z02` — Defensive Belt

**Location:** forward and outer-hull armored volumes.  
**Crew shorthand:** the Belt.

Contains:

- primary sensor arrays and sensor-processing rooms;
- defensive-fire control;
- shield-distribution nodes;
- point-defense and countermeasure control;
- forward damage-control stations;
- hardened ammunition and power-routing trunks;
- redundant tactical communications relays.

Tactical Operations and Gunnery operates from the Crown but relies on distributed Belt stations so the ship can continue fighting after local command damage.

### `JP-Z03` — Port Flight Spine

**Location:** port longitudinal carrier volume.  
**Crew shorthand:** Port Wing.

Contains:

- armored internal hangars;
- rapid-launch lanes;
- recovery and deceleration corridors;
- aviation maintenance shops;
- fuel, power-cell, and ordnance handling zones;
- ready rooms and flight-control stations;
- emergency craft shelters.

### `JP-Z04` — Starboard Flight Spine

**Location:** starboard longitudinal carrier volume.  
**Crew shorthand:** Starboard Wing.

Mirrors the Port Flight Spine sufficiently to preserve launch and recovery capacity after one side is damaged, while allowing unequal mission loading when required.

### `JP-Z05` — Heavy Mission Bays

**Location:** ventral-midships.  
**Crew shorthand:** the Wells.

Contains:

- heavy shuttle and cutter docks;
- independent gunboat and specialist-craft berths;
- boarding and rescue-craft staging;
- modular mission bays;
- cargo transfer locks;
- diplomatic and command-shuttle docking;
- direct protected routes to the Marshal/Sentinel Operations Enclave.

The *Third Measure* and comparable hosted Ranger gunboats berth here rather than being absorbed into normal fighter squadrons.

### `JP-Z06` — Marshal and Sentinel Operations Enclave

**Location:** internal to the protected midships mission complex, adjacent to but access-controlled from the Heavy Mission Bays.  
**Crew shorthand:** the Enclave.

Contains:

- independent Marshal Operations Center;
- Ranger ready rooms and planning suites;
- secure evidence intake and custody vaults;
- forensic processing rooms;
- witness-protection and interview spaces;
- short-duration detention and protective-custody facilities;
- Judicial Council and Marshal command secure-link rooms;
- Sentinel mission planning and command suites;
- suit storage, maintenance, arming, decontamination, and medical interfaces;
- Sentinel-Diplomat preparation and secure diplomatic-support rooms;
- compartmented intelligence and special-operations briefing cells;
- independent armories and mission-equipment stores.

The Enclave is not under ordinary naval mission command. Vessel command controls access safety, weapons posture aboard ship, launch conditions, and emergency restrictions under `JUDICATOR-HOST-001`.

### `JP-Z07` — Engineering Spine

**Location:** axial-aft protected core.  
**Crew shorthand:** the Forge.

Contains:

- primary and auxiliary power-generation nodes;
- sublight propulsion systems;
- reserved volumes for the canonical vessel's FTL architecture, exact drive type unresolved;
- shield and weapons power-conditioning systems;
- engineering control rooms;
- fabrication and heavy-repair shops;
- coolant, atmosphere, and thermal-management plants;
- redundant life-support machinery;
- emergency isolation and manual-control stations.

The architecture assumes distributed generation and control rather than one vulnerable reactor room. Exact reactor and drive technologies remain open.

### `JP-Z08` — Logistics Keel

**Location:** ventral-aft and deep-midships cargo volumes.  
**Crew shorthand:** the Keel.

Contains:

- long-duration stores;
- spare parts and fabrication feedstock;
- aviation and mission ordnance magazines;
- shipwide drone depots;
- cargo sorting and automated distribution;
- refrigerated, medical, and hazardous-material storage;
- large-component workshops;
- waste reclamation and recycling;
- damage-control reserves;
- fleet resupply interfaces.

The Keel supports the Judicator as a mobile campaign base and allows hosted Ranger and Sentinel assets to draw mission-specific packages without becoming administratively part of the ship's naval establishment.

### `JP-Z09` — Medical and Science Complex

**Location:** central protected volumes with direct access from mission bays, habitation, and express transit.  
**Crew shorthand:** the Lantern.

Contains:

- main hospital and surgical center;
- trauma intake linked to flight and mission bays;
- Sentinel medicine and powered-suit casualty interfaces;
- quarantine and contamination isolation;
- rehabilitation and cybernetic medicine;
- forensic medicine;
- modular research laboratories;
- captured-technology examination rooms;
- anomaly and materials laboratories;
- science operations control;
- medical surge wards.

Staged planning capacity:

- approximately 250 acute-care beds under normal configuration;
- scalable mass-casualty capacity of approximately 600 through converted spaces;
- separated medical custody rooms for injured detainees and protected witnesses.

### `JP-Z10` — Habitation, Civic, and Diplomatic Districts

**Location:** distributed central and dorsal-midships residential volumes.  
**Crew shorthand:** the Hearth and the Forum.

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
- protected arrival routes separated from combat flight operations.

The diplomatic district is designed to host senior officials and negotiations without turning the bridge or Flag Operations Center into ceremonial space.

## 5. Command-space separation

### 5.1 Primary bridge

Commands navigation, maneuver, shipwide readiness, defensive posture, and execution of Captain Tann's vessel orders.

### 5.2 Combat Information Center

Maintains the immediate tactical picture, defensive coordination, weapons employment, sensor fusion, and ship combat execution under the captain and Tactical Operations.

### 5.3 Flag Operations Center

Coordinates fleet and task-force movement, escort operations, sector surveillance, strategic logistics, and naval campaign planning.

### 5.4 Joint Operations Coordination Center

Provides shared planning and real-time coordination for missions involving multiple independent institutions. It does not create permanent command authority. Every joint operation requires a named coordinating lead and reserved-authority statement under `JUDICATOR-HOST-001`.

### 5.5 Marshal Operations Center

Controls Marshal investigations, warrants, evidence, enforcement priorities, Ranger tasking, and liaison with the Judicial Council and Chief Marshal chain.

### 5.6 Sentinel Mission Control

Controls Sentinel readiness, suit deployment, mission-specific tactical planning, and coordination with Sentinel High Command. The unresolved Radek/Drayen boundary must be stated in each applicable mission order.

### 5.7 Emergency battle bridge

A physically isolated command node capable of navigation, defense, internal communications, and minimum launch/recovery control if the Crown is disabled.

## 6. Launch and recovery architecture

### 6.1 Flight spines

The Port and Starboard Flight Spines operate as independent carrier systems.

Each spine contains:

- four rapid-launch lanes;
- two primary recovery corridors;
- armored internal marshalling hangars;
- distributed ready rooms and flight-control stations;
- independent damage-control and emergency-seal capability.

Loss of one spine reduces sortie rate but does not eliminate carrier operations.

### 6.2 Heavy mission bays

The Heavy Mission Bays support craft too large, specialized, or institutionally independent for ordinary squadron handling.

STAGING berth plan:

- 12 independent gunboat/cutter berths;
- 6 modular special-mission berths;
- 4 diplomatic or command-shuttle berths;
- 8 heavy shuttle/transport positions;
- 4 external docking collars for vessels that cannot enter the internal bays.

### 6.3 Rapid-response cells

Twelve hardened rapid-response cells permit interceptors, rescue craft, or mission-loaded shuttles to launch without clearing a full hangar sequence. Exact craft type varies by deployment.

### 6.4 Launch authority

Mission authorization and flight clearance remain separate:

- parent command authorizes the hosted unit's mission;
- Judicator flight control authorizes safe launch and recovery;
- Captain Tann may delay, divert, recover, or suspend flight operations for lawful vessel-safety reasons;
- vessel command may not use flight clearance as a pretext to assume investigative or Sentinel mission authority.

## 7. Staged embarked craft envelope

The following is a planning complement, not yet CANON:

| Category | STAGING nominal capacity |
|---|---:|
| Fighters / interceptors | 96 |
| Multirole / strike craft | 48 |
| Shuttles, medevac, and utility craft | 36 |
| Boarding / rescue cutters | 12 |
| Independent Ranger, Marshal, intelligence, or specialist gunboats | 12 berths |
| Command / diplomatic shuttles | 4 |
| Heavy transports | 8 |
| Shipboard drones | Variable; mission and maintenance dependent |

The staged total of 144 combat aerospace craft reflects supercarrier function without fixing squadron names, manufacturers, or exact combat doctrine.

## 8. Embarked operational complements

### 8.1 Naval establishment

Includes bridge, combat systems, engineering, aviation, logistics, medical, science, administration, security, and ship services under Captain Tann's chain.

### 8.2 Sentinel strike unit

Canon establishes one full Sentinel strike unit aboard the ship. Exact strength, squad distribution, and variant mix remain unresolved and must not be inferred from facility capacity.

The architecture supports:

- multiple squad-ready rooms;
- segregated suit maintenance lines;
- covert and overt launch routes;
- medical and decontamination support;
- one or more Sentinel-Diplomat pairs;
- mission-specific attachments from Sentinel High Command.

### 8.3 Marshal and Ranger presence

Staged long-duration capacity:

- up to 8 Ranger crews in dedicated long-duration berths;
- up to 8 additional Ranger or specialist crews in surge configuration;
- one embarked Marshal command and liaison element;
- evidence, witness, interview, and temporary detention support sufficient for a sector campaign.

The presence of multiple Ranger berths does not make permanent supercarrier service normal for Ranger crews. Most berths support rotation, repair, staging, transfer, or exceptional campaign assignments.

### 8.4 Diplomatic and specialist detachments

The ship can host:

- diplomatic missions and negotiators;
- Sentinel-Diplomat pairs;
- Union Intelligence teams;
- scientific and technical detachments;
- Judicial Council, legal, and oversight personnel;
- medical or humanitarian teams;
- temporary planetary or allied delegations.

These assets are normally employed separately unless mission orders establish joint use.

## 9. Detention, evidence, and legal facilities

The Judicator is not a prison ship, but a Marshal campaign platform requires lawful short-duration custody.

STAGING capacity:

- 96 standard secure detention positions;
- 16 high-security isolation positions;
- 24 protective-custody or witness positions;
- 12 medical-custody rooms integrated with the hospital;
- expandable emergency holding space during mass boarding operations.

Rules:

- detention requires lawful Marshal, military, or emergency authority;
- evidence and detainees remain under distinct chains of custody;
- planetary transfer is preferred when lawful and secure;
- long-term incarceration is outside the vessel's normal purpose;
- medical access and Judicial Council review remain available.

## 10. Networks, cyberwarfare, and information boundaries

### 10.1 Segmented networks

The vessel uses physically and cryptographically segmented command domains:

- navigation and engineering;
- tactical and weapons;
- aviation and flight control;
- fleet command;
- Marshal evidence and operations;
- Sentinel operations;
- intelligence compartments;
- medical and scientific systems;
- diplomatic communications;
- public and crew services.

### 10.2 Controlled exchange

Cross-domain data passes through audited gateways. Hosted assets provide the minimum information needed for safe launch, recovery, medical response, access control, and ship defense while preserving lawful compartmentation.

### 10.3 AI-resistant command design

The legacy World Bible associates the Judicator with AI-resistant command systems. This architecture reserves hardened manual controls, isolated command paths, and degraded-mode operations, but the exact AI architecture remains STAGING pending reconciliation.

## 11. Transit and internal movement

The ship uses three movement layers:

1. **Axial express trunk:** high-speed end-to-end personnel and light-cargo transit.
2. **District loops:** local transit connecting habitation, command, medical, flight, and mission zones.
3. **Service trunks:** restricted logistics, maintenance, ordnance, and damage-control routes.

Hosted-asset routes connect the Heavy Mission Bays, Enclave, Medical and Science Complex, and diplomatic district without requiring routine passage through the Crown.

Emergency doors can divide every major zone into independently pressurized compartments. No single transit line is the only path between command, engineering, medical, and launch functions.

## 12. Approximate population planning model

This is a functional planning model, not a roster claim:

| Population group | STAGING planning figure |
|---|---:|
| Naval command, combat systems, security, and administration | 3,200 |
| Engineering, maintenance, and ship services | 2,600 |
| Aviation, flight deck, and aerospace support | 2,300 |
| Logistics, cargo, fabrication, and supply | 1,300 |
| Medical, science, intelligence, communications, and diplomatic staff | 1,000 |
| Embarked Marshal, Sentinel, specialist, and transient personnel | 1,600 |
| **Total** | **12,000** |

Operational deployments may shift these proportions without changing the approximate total.

## 13. Damage-control and continuity architecture

The Judicator's continuity model includes:

- primary bridge, Combat Information Center, and emergency battle bridge separation;
- two independently operable flight spines;
- distributed power generation and routing;
- multiple life-support and atmosphere-processing zones;
- decentralized damage-control stations;
- protected medical facilities near but not inside carrier and mission bays;
- separated ammunition magazines and hazardous stores;
- compartment-level isolation;
- manual and degraded-mode controls for navigation, propulsion, defense, launch, recovery, and communications.

## 14. Narrative-use constraints

Future scenes should treat the Judicator as a large institution rather than a single room with a ship around it.

- Travel takes time unless express transit is used.
- Departments have separate priorities and access rules.
- Hosted units can remain socially and operationally distinct from naval personnel.
- The ship's size provides resources but also creates bureaucracy, visibility, and political audiences.
- A Ranger crew can be physically close to overwhelming power while still waiting for lawful authorization, launch clearance, evidence review, or a specialist's availability.
- Damage to one bay, corridor, command room, or network does not automatically disable the entire vessel.
- The ship can dominate a battlespace but cannot solve legitimacy, corruption, or lawful-governance problems through mass alone.

## 15. Promotion matrix

| Claim group | Current disposition |
|---|---|
| Flagship / supercarrier / approximately 12,000 / Tann command | CANON_CONFIRMED |
| Marshal strike-force command role and full Sentinel unit | CANON_CONFIRMED |
| Hosted-asset independence and mission-specific coordination | CANON_CONFIRMED |
| 2.1 km scale and 84-deck model | STAGING |
| Ten-zone internal topology | STAGING |
| Dual flight spines and heavy mission-bay layout | STAGING |
| Craft capacities and rapid-response cells | STAGING |
| Ranger berth and detention capacities | STAGING |
| Medical and surge capacities | STAGING |
| Population planning breakdown | STAGING |
| AI-resistant and segmented command implementation | STAGING / LEGACY-SUPPORTED |
| Exact weapons, drives, reactors, armor, shield systems | OPEN |

## 16. Open decisions

1. Ratify or revise the staged scale envelope.
2. Decide whether the 12,000 figure includes all routinely embarked assets or ship's company only.
3. Resolve the permanently embarked Sentinel unit's command boundary between Major Elias Radek and Marshal-Captain Elias Drayen.
4. Define the Judicator's primary power and FTL systems.
5. Define armor, shields, main weapons, and defensive batteries.
6. Ratify the 144-combat-craft carrier envelope and support-craft mix.
7. Define the current sector-deployment event and escort group.
8. Decide which internal zone names become canonical crew language.
9. Create stable berth and compartment IDs for the *Third Measure*, Diplomatic Sentinels, and other recurring narrative locations.
10. Promote only after CanonRec review confirms no conflict with recovered ship or fleet material.
