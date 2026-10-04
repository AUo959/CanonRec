# Galactic Union Ship Design Language

**Domain:** GUMAS L2 / Galactic Union  
**Artifact:** Visual-development system  
**Version:** v0.1  
**Date:** 2026-07-21  
**Certainty:** STAGING  
**Status:** Ready for concept-art use; not approved for canon promotion

## 1. Purpose

This document establishes a reusable visual-development language for Galactic Union spacecraft. It translates committed operational roles and system anchors into coherent visual guidance without promoting new hull geometry, livery, materials, dimensions, or insignia placement into canon.

The design language must make Union vessels look related without making every class a scaled copy of one hull.

## 2. Certainty boundary

### 2.1 Binding source anchors

The following class identities, roles, features, and named-vessel relationships are CANON through their individual CanonRec records:

- Judicator-Class / G.U.S. Judicator Prime;
- Sentinel-Class / G.U.S. Umbra Stalker;
- Aegis-Class / G.U.S. Iron Vow;
- Palisade-Class / G.U.S. Resolute Bastion;
- Obsidian-Class / G.U.S. Specter's Wake.

### 2.2 Visual staging layer

The following remain free visual-development decisions until separately reviewed and promoted:

- hull silhouette and proportions;
- exterior materials and finish;
- fleet colors and livery;
- insignia geometry and placement;
- window and lighting patterns;
- drive and exhaust geometry;
- visible weapon placement;
- shield-emitter appearance;
- armor-panel size and arrangement;
- sensor architecture;
- scale relationships beyond committed or expressly staged figures;
- manufacturer or shipyard vocabulary.

Every generated image must therefore be labeled **VISUAL STAGING — NOT YET CANON**.

## 3. Union-wide visual principles

### 3.1 Institutional engineering

Union ships should look like products of a large, regulated, multi-world civilization. Their forms should communicate:

- clear functional zoning;
- maintainable modular systems;
- redundant routes and protected subsystems;
- accountable human control;
- long-service durability;
- visible accommodation of logistics, repair, rescue, and diplomacy alongside combat capability.

Avoid mystical, purely ornamental, or biologically organic hull language unless a later source explicitly establishes it.

### 3.2 Controlled mass

Large Union ships should communicate power through organized mass rather than random spikes or excessive surface noise. Major volumes should be legible at distance:

- central structural spine or citadel;
- mission-specific side or ventral volumes;
- protected command and sensor regions;
- separated propulsion clusters;
- recognizable maintenance and access bands.

### 3.3 Layered protection

Where armor is relevant, show a hierarchy of protection:

1. sacrificial outer panels;
2. thermal and fragmentation layers;
3. protected structural citadel;
4. recessed critical systems.

Modular armor should read as replaceable and maintainable rather than decorative plating.

### 3.4 Distributed systems

Point defense, sensors, shield emitters, maneuvering thrusters, and damage-control interfaces should appear distributed across the hull. Avoid a single exposed component whose loss would obviously disable the entire ship.

### 3.5 Human accountability

Union automation may be advanced, but consequential actions remain attributable. Visuals should preserve signs of crewed command and manual fallback:

- protected bridge or command apertures rather than a fully transparent panoramic cockpit;
- local control nodes;
- maintenance access;
- segmented communications arrays;
- physical launch and recovery infrastructure.

### 3.6 Civic presence

Even military vessels belong to a political union. Where scale permits, include restrained signals of civil authority:

- formal arrival apertures;
- diplomatic docking routes;
- rescue and medical markings;
- registry identifiers;
- clear navigation and hazard markings.

These should not make combat ships ceremonial or brightly exposed.

## 4. Proposed material and livery vocabulary

All items in this section are STAGING.

### 4.1 Base materials

- low-gloss ceramic-metal composite hull skin;
- cooler pale-gray or desaturated silver primary surfaces;
- darker graphite armor, radiator, sensor, and maintenance regions;
- limited warm-metal accents around high-energy or service interfaces;
- visibly replaceable armor panels with subtle tonal variation.

### 4.2 Fleet markings

- restrained Galactic Union emblem on dorsal and ventral identification surfaces;
- large registry code readable at docking and inspection distance;
- class-specific accent stripe or geometric band;
- high-contrast safety markings only around launch lanes, docking collars, rescue apertures, and hazardous systems;
- no decorative camouflage unless mission doctrine requires it.

### 4.3 Lighting

- sparse cool-white navigation and maintenance lighting;
- amber hazard lighting around active launch or engineering zones;
- minimal visible illumination during stealth operations;
- no continuous glowing hull seams unless tied to an identified system.

## 5. Shared silhouette grammar

A Union vessel should normally exhibit at least three of the following:

- a stable axial or keel-based structural logic;
- clear protected command volume;
- separated drive clusters or drive shielding;
- modular outer armor fields;
- recessed sensors and communications equipment;
- visible but protected mission apertures;
- distributed defensive nodes;
- readable dorsal/ventral orientation.

The grammar is intentionally broad. A carrier should still read as a carrier, a stealth destroyer as a stealth destroyer, and a diplomatic vessel as a diplomatic vessel.

## 6. Class differentiation rules

### 6.1 Judicator-Class

Visual priority: institutional concentration, flagship command, supercarrier scale, campaign endurance.

Suggested cues:

- immense central citadel;
- paired carrier spines;
- ventral heavy-mission volumes;
- protected dorsal command crown;
- segmented armor and shield districts;
- long axial silhouette with broad midships mass.

### 6.2 Sentinel-Class

Visual priority: covert deployment, electronic warfare, rapid response.

Suggested cues:

- compact low-observable hull;
- recessed launch and sensor apertures;
- minimal thermal exposure;
- narrow frontal and lateral radar profile;
- integrated rather than externally mounted mission systems.

### 6.3 Aegis-Class

Visual priority: frontline combat, planetary defense, fleet support.

Suggested cues:

- strongly axial weapons architecture;
- armored forward citadel;
- modular side armor fields;
- visible but protected shield and sensor bands;
- balanced maneuverability and sustained-fire mass.

### 6.4 Palisade-Class

Visual priority: aerospace capacity, repair, sortie generation, defensive persistence.

Suggested cues:

- broad carrier body;
- multiple protected launch and recovery apertures;
- layered hangar volumes;
- extensive service and drone-access cavities;
- dense perimeter defense architecture.

### 6.5 Obsidian-Class

Visual priority: black operations, reconnaissance, AI counterwarfare.

Suggested cues:

- dark continuous hull planes;
- retractable or concealed apertures;
- shielded propulsion;
- very low visible-light signature;
- ambiguous silhouette at distance without literal transparency.

## 7. Prohibited drift patterns

Do not introduce the following without an explicit future ruling:

- borrowed insignia or direct visual copies from existing commercial science-fiction franchises;
- unexplained gravity-defying fins or wings used only as decoration;
- exposed crew bridges on capital warships;
- unrestricted autonomous strategic weapons;
- glowing energy conduits with no functional explanation;
- a single universal hull reused unchanged across all classes;
- class dimensions inferred solely from crew complement;
- visual claims that convert STAGING counts or architecture into CANON.

## 8. Image metadata requirements

Every visual-development asset should record:

```yaml
visual_asset_metadata:
  domain: GUMAS_L2
  faction: galactic_union
  certainty: STAGING
  canon_status: not_promoted
  source_records: []
  class_id: null
  vessel_id: null
  generated_at: null
  creator_or_model: null
  prompt_version: null
  unresolved_visual_decisions: []
```

## 9. Promotion path

A visual may become canon only after:

1. comparison against the relevant vessel and class records;
2. conflict scan against existing operational specifications;
3. explicit approval of silhouette, materials, livery, and scale claims;
4. stable asset identification and provenance;
5. committed CanonRec promotion record.

## 10. Source records

- `canon/L2/entities/mobile_assets/vessel_gu_001.json`
- `canon/L2/entities/mobile_assets/vessel_gu_002.json`
- `canon/L2/entities/mobile_assets/vessel_gu_003.json`
- `canon/L2/entities/mobile_assets/vessel_gu_004.json`
- `canon/L2/entities/mobile_assets/vessel_gu_006.json`
- `canon/L2/entities/ship_classes/cls_sentinel.json`
- `canon/L2/entities/ship_classes/cls_aegis.json`
- `canon/L2/entities/ship_classes/cls_palisade.json`
- `canon/L2/entities/ship_classes/cls_obsidian.json`
- `canon/L2/operations/GUMAS_L2__SPEC__JUDICATOR_PRIME_FUNCTIONAL_ARCHITECTURE__v1.1__2026-07-21.md`

---

**Design principle:** Related by institutional logic; differentiated by mission.