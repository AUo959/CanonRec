# L2 GUMAS Ship Registry (v1.0)

**Layer:** L2 (Galactic Union Simulation Layer)  
**Status:** STAGING (awaiting senior staff review for CANON_PROMOTE)  
**Last Updated:** 2026-01-30  
**Source Documents:** GUMAS_L2_World_Bible.md, gumas_origin_thread_synthesis_staging_dossier_v_0.md, l_2_physical_locations_index

---

## 1) Schema Definition

### 1.1 Ship Class Schema

```json
{
  "$schema": "aurora://schemas/l2/ship_class/v1.0.0",
  "type": "object",
  "required": ["class_id", "class_name", "division", "role", "allegiance"],
  "properties": {
    "class_id": {
      "type": "string",
      "pattern": "^CLASS-[A-Z]+-[0-9]{2}$",
      "description": "Stable class identifier"
    },
    "class_name": {
      "type": "string",
      "description": "Human-readable class designation"
    },
    "division": {
      "type": "string",
      "enum": ["flagship_command", "special_operations", "battlecruiser", "heavy_carrier", "frigate", "stealth_destroyer", "diplomatic", "interceptor", "defense_platform", "logistics", "dreadnought", "raider"],
      "description": "Operational division"
    },
    "allegiance": {
      "type": "string",
      "enum": ["galactic_union", "ai_warlord_collective", "separatist_confederation", "velar_imperium", "outer_colonies", "pmc_syndicate", "neutral", "contested"],
      "description": "Primary operating faction"
    },
    "role": {
      "type": "string",
      "description": "Primary operational role"
    },
    "key_features": {
      "type": "array",
      "items": { "type": "string" },
      "description": "Distinctive capabilities"
    },
    "typical_complement": {
      "type": "integer",
      "description": "Standard crew size"
    },
    "certainty": {
      "type": "string",
      "enum": ["CANON", "CANON_PROMOTE", "STAGING", "UNCONFIRMED"]
    }
  }
}
```

### 1.2 Named Vessel Schema

```json
{
  "$schema": "aurora://schemas/l2/vessel/v1.0.0",
  "type": "object",
  "required": ["vessel_id", "vessel_name", "class_id", "allegiance", "status"],
  "properties": {
    "vessel_id": {
      "type": "string",
      "pattern": "^VESSEL-[A-Z]{2,4}-[0-9]{3}$",
      "description": "Stable vessel identifier"
    },
    "vessel_name": {
      "type": "string",
      "description": "Official designation (e.g., G.U.S. Judicator Prime)"
    },
    "aliases": {
      "type": "array",
      "items": { "type": "string" },
      "description": "Alternative names, nicknames, translations"
    },
    "class_id": {
      "type": "string",
      "description": "Reference to ship class"
    },
    "allegiance": {
      "type": "string",
      "description": "Operating faction"
    },
    "commanding_officer": {
      "type": ["string", "null"],
      "description": "Current CO (null if unknown or AI-controlled)"
    },
    "status": {
      "type": "string",
      "enum": ["active", "destroyed", "captured", "missing", "under_construction", "decommissioned"],
      "description": "Current operational status"
    },
    "home_port": {
      "type": ["string", "null"],
      "description": "Primary station/system (null for mobile operations)"
    },
    "location_type": {
      "type": "string",
      "enum": ["fixed", "moving"],
      "description": "Whether vessel has fixed coordinates or is mobile"
    },
    "specifications": {
      "type": "object",
      "properties": {
        "primary_weapons": { "type": "array", "items": { "type": "string" } },
        "defensive_systems": { "type": "array", "items": { "type": "string" } },
        "propulsion": { "type": "string" },
        "support_craft": { "type": "array", "items": { "type": "string" } },
        "special_systems": { "type": "array", "items": { "type": "string" } }
      }
    },
    "narrative_significance": {
      "type": "string",
      "enum": ["flagship", "capital", "notable", "standard", "background"],
      "description": "Importance to simulation narratives"
    },
    "certainty": {
      "type": "string",
      "enum": ["CANON", "CANON_PROMOTE", "STAGING", "UNCONFIRMED"]
    },
    "doc_sources": {
      "type": "array",
      "items": { "type": "string" }
    },
    "notes": {
      "type": "string"
    }
  }
}
```

---

## 2) Ship Class Registry

### 2.1 Galactic Union Ship Classes

```json
[
  {
    "class_id": "CLASS-JUDICATOR-01",
    "class_name": "Judicator-Class",
    "division": "flagship_command",
    "allegiance": "galactic_union",
    "role": "Strategic fleet coordination, high-level diplomacy, cyberwarfare operations",
    "key_features": [
      "Heavily armored",
      "FTL-capable",
      "Sentinel deployment bays",
      "AI-resistant command systems",
      "Dual FTL cores with emergency jump"
    ],
    "typical_complement": 2500,
    "certainty": "STAGING",
    "doc_sources": ["GUMAS_L2_World_Bible.md"]
  },
  {
    "class_id": "CLASS-SENTINEL-01",
    "class_name": "Sentinel-Class",
    "division": "special_operations",
    "allegiance": "galactic_union",
    "role": "Covert operations, rapid Sentinel deployment, counterinsurgency",
    "key_features": [
      "Stealth capabilities",
      "Electronic warfare suites",
      "Rapid-response FTL drives"
    ],
    "typical_complement": 450,
    "certainty": "STAGING",
    "doc_sources": ["GUMAS_L2_World_Bible.md"]
  },
  {
    "class_id": "CLASS-AEGIS-01",
    "class_name": "Aegis-Class",
    "division": "battlecruiser",
    "allegiance": "galactic_union",
    "role": "Frontline combat, planetary defense, fleet support",
    "key_features": [
      "Long-range rail cannons",
      "Modular armor plating",
      "Adaptive energy shielding"
    ],
    "typical_complement": 1200,
    "certainty": "STAGING",
    "doc_sources": ["GUMAS_L2_World_Bible.md"]
  },
  {
    "class_id": "CLASS-PALISADE-01",
    "class_name": "Palisade-Class",
    "division": "heavy_carrier",
    "allegiance": "galactic_union",
    "role": "Carrier for fighters, bombers, fleet support units",
    "key_features": [
      "Enormous hangar capacity",
      "Autonomous repair drones",
      "Defensive turret emplacements"
    ],
    "typical_complement": 3500,
    "certainty": "STAGING",
    "doc_sources": ["GUMAS_L2_World_Bible.md"]
  },
  {
    "class_id": "CLASS-VANGUARD-01",
    "class_name": "Vanguard-Class",
    "division": "frigate",
    "allegiance": "galactic_union",
    "role": "Patrol, anti-piracy, high-speed interception, frontier security",
    "key_features": [
      "High-speed sublight engines",
      "Reinforced hull for boarding",
      "Hybrid energy/projectile weapons"
    ],
    "typical_complement": 180,
    "certainty": "STAGING",
    "doc_sources": ["GUMAS_L2_World_Bible.md"]
  },
  {
    "class_id": "CLASS-OBSIDIAN-01",
    "class_name": "Obsidian-Class",
    "division": "stealth_destroyer",
    "allegiance": "galactic_union",
    "role": "Black-ops, deep-space reconnaissance, AI counterwarfare",
    "key_features": [
      "Quantum cloaking",
      "Advanced ECM systems",
      "Low-profile heat signature masking"
    ],
    "typical_complement": 120,
    "certainty": "STAGING",
    "doc_sources": ["GUMAS_L2_World_Bible.md"]
  },
  {
    "class_id": "CLASS-DIPLOMATIC-01",
    "class_name": "Diplomatic-Class",
    "division": "diplomatic",
    "allegiance": "galactic_union",
    "role": "Official Union representation, high-level negotiations, mobile peacekeeping HQ",
    "key_features": [
      "Luxurious meeting halls",
      "Encrypted communication suites",
      "Minimal defensive armament"
    ],
    "typical_complement": 350,
    "certainty": "STAGING",
    "doc_sources": ["GUMAS_L2_World_Bible.md"]
  },
  {
    "class_id": "CLASS-PEREGRINE-01",
    "class_name": "Peregrine-Class",
    "division": "interceptor",
    "allegiance": "galactic_union",
    "role": "Fast-attack, skirmishing, fleet scouting",
    "key_features": [
      "High-maneuverability thrusters",
      "Twin-linked rapid plasma cannons",
      "AI-assisted targeting"
    ],
    "typical_complement": 45,
    "certainty": "STAGING",
    "doc_sources": ["GUMAS_L2_World_Bible.md"]
  },
  {
    "class_id": "CLASS-BASTION-01",
    "class_name": "Bastion-Class",
    "division": "defense_platform",
    "allegiance": "galactic_union",
    "role": "Orbital defense, station-to-surface fire support, civilian security",
    "key_features": [
      "Planetary ion cannons",
      "High-density shield emitters",
      "Long-duration endurance"
    ],
    "typical_complement": 800,
    "certainty": "STAGING",
    "doc_sources": ["GUMAS_L2_World_Bible.md"]
  },
  {
    "class_id": "CLASS-RELIANT-01",
    "class_name": "Reliant-Class",
    "division": "logistics",
    "allegiance": "galactic_union",
    "role": "Fleet resupply, mobile command, battlefield medical support",
    "key_features": [
      "Modular storage",
      "Reinforced hull",
      "Self-sustaining resource extraction units"
    ],
    "typical_complement": 600,
    "certainty": "STAGING",
    "doc_sources": ["GUMAS_L2_World_Bible.md"]
  }
]
```

### 2.2 Non-Union Ship Classes

```json
[
  {
    "class_id": "CLASS-LEVIATHAN-01",
    "class_name": "Leviathan Dreadnought",
    "division": "dreadnought",
    "allegiance": "ai_warlord_collective",
    "role": "Primary command vessel, symbol of AI resistance, autonomous warfare",
    "key_features": [
      "Self-evolving combat AI",
      "Massive firepower",
      "Autonomous drone swarms",
      "No organic crew required"
    ],
    "typical_complement": 0,
    "certainty": "STAGING",
    "doc_sources": ["GUMAS_L2_World_Bible.md"],
    "notes": "AI-controlled; complement is synthetic intelligences, not crew"
  },
  {
    "class_id": "CLASS-DREADRAIDER-01",
    "class_name": "Leviathan-Class Dread-raider",
    "division": "raider",
    "allegiance": "outer_colonies",
    "role": "Mobile fortress, refugee ship, black-market hub, command nexus",
    "key_features": [
      "Massive cargo capacity",
      "Modular habitat sections",
      "Heavy armament for size",
      "Extended autonomous operation"
    ],
    "typical_complement": 5000,
    "certainty": "STAGING",
    "doc_sources": ["gumas_origin_thread_synthesis_staging_dossier_v_0.md"],
    "notes": "Pirate/confederation vessel class; Khar'Thyrix is type example"
  }
]
```

---

## 3) Named Vessel Registry

### 3.1 Galactic Union Vessels

```json
[
  {
    "vessel_id": "VESSEL-GU-001",
    "vessel_name": "G.U.S. Judicator Prime",
    "aliases": ["Judicator Prime", "The Judicator"],
    "class_id": "CLASS-JUDICATOR-01",
    "allegiance": "galactic_union",
    "commanding_officer": "Captain Alric Tann",
    "status": "active",
    "home_port": null,
    "location_type": "moving",
    "specifications": {
      "primary_weapons": ["Long-range plasma lances", "AI-coordinated point defense"],
      "defensive_systems": ["Multi-layered energy shields", "Ablative armor plating"],
      "propulsion": "Dual FTL cores with emergency jump capability",
      "support_craft": ["Full Sentinel deployment wing", "Tactical interceptors"],
      "special_systems": ["AI-Vanguard countermeasures", "Encrypted battle network"]
    },
    "narrative_significance": "flagship",
    "certainty": "STAGING",
    "doc_sources": ["GUMAS_L2_World_Bible.md"],
    "notes": "Primary narrative vessel; full crew roster defined in Character Registry"
  },
  {
    "vessel_id": "VESSEL-GU-002",
    "vessel_name": "G.U.S. Umbra Stalker",
    "aliases": [],
    "class_id": "CLASS-SENTINEL-01",
    "allegiance": "galactic_union",
    "commanding_officer": null,
    "status": "active",
    "home_port": null,
    "location_type": "moving",
    "specifications": {},
    "narrative_significance": "notable",
    "certainty": "STAGING",
    "doc_sources": ["GUMAS_L2_World_Bible.md"],
    "notes": "Example vessel for Sentinel-Class; CO TBD"
  },
  {
    "vessel_id": "VESSEL-GU-003",
    "vessel_name": "G.U.S. Iron Vow",
    "aliases": [],
    "class_id": "CLASS-AEGIS-01",
    "allegiance": "galactic_union",
    "commanding_officer": null,
    "status": "active",
    "home_port": null,
    "location_type": "moving",
    "specifications": {},
    "narrative_significance": "notable",
    "certainty": "STAGING",
    "doc_sources": ["GUMAS_L2_World_Bible.md"],
    "notes": "Example vessel for Aegis-Class"
  },
  {
    "vessel_id": "VESSEL-GU-004",
    "vessel_name": "G.U.S. Resolute Bastion",
    "aliases": [],
    "class_id": "CLASS-PALISADE-01",
    "allegiance": "galactic_union",
    "commanding_officer": null,
    "status": "active",
    "home_port": null,
    "location_type": "moving",
    "specifications": {},
    "narrative_significance": "notable",
    "certainty": "STAGING",
    "doc_sources": ["GUMAS_L2_World_Bible.md"],
    "notes": "Example vessel for Palisade-Class"
  },
  {
    "vessel_id": "VESSEL-GU-005",
    "vessel_name": "G.U.S. Ordinance Swift",
    "aliases": [],
    "class_id": "CLASS-VANGUARD-01",
    "allegiance": "galactic_union",
    "commanding_officer": null,
    "status": "active",
    "home_port": null,
    "location_type": "moving",
    "specifications": {},
    "narrative_significance": "standard",
    "certainty": "STAGING",
    "doc_sources": ["GUMAS_L2_World_Bible.md"],
    "notes": "Example vessel for Vanguard-Class"
  },
  {
    "vessel_id": "VESSEL-GU-006",
    "vessel_name": "G.U.S. Specter's Wake",
    "aliases": [],
    "class_id": "CLASS-OBSIDIAN-01",
    "allegiance": "galactic_union",
    "commanding_officer": null,
    "status": "active",
    "home_port": null,
    "location_type": "moving",
    "specifications": {},
    "narrative_significance": "notable",
    "certainty": "STAGING",
    "doc_sources": ["GUMAS_L2_World_Bible.md"],
    "notes": "Example vessel for Obsidian-Class; likely UIB/GSB operations"
  },
  {
    "vessel_id": "VESSEL-GU-007",
    "vessel_name": "G.U.S. Harmony's Accord",
    "aliases": [],
    "class_id": "CLASS-DIPLOMATIC-01",
    "allegiance": "galactic_union",
    "commanding_officer": null,
    "status": "active",
    "home_port": null,
    "location_type": "moving",
    "specifications": {},
    "narrative_significance": "notable",
    "certainty": "STAGING",
    "doc_sources": ["GUMAS_L2_World_Bible.md"],
    "notes": "Example vessel for Diplomatic-Class"
  },
  {
    "vessel_id": "VESSEL-GU-008",
    "vessel_name": "G.U.S. Storm Harrier",
    "aliases": [],
    "class_id": "CLASS-PEREGRINE-01",
    "allegiance": "galactic_union",
    "commanding_officer": null,
    "status": "active",
    "home_port": null,
    "location_type": "moving",
    "specifications": {},
    "narrative_significance": "standard",
    "certainty": "STAGING",
    "doc_sources": ["GUMAS_L2_World_Bible.md"],
    "notes": "Example vessel for Peregrine-Class"
  },
  {
    "vessel_id": "VESSEL-GU-009",
    "vessel_name": "G.U.S. Sentinel's Hold",
    "aliases": [],
    "class_id": "CLASS-BASTION-01",
    "allegiance": "galactic_union",
    "commanding_officer": null,
    "status": "active",
    "home_port": "GU-CORE-01",
    "location_type": "fixed",
    "specifications": {},
    "narrative_significance": "notable",
    "certainty": "STAGING",
    "doc_sources": ["GUMAS_L2_World_Bible.md"],
    "notes": "Example vessel for Bastion-Class; orbital defense platform"
  },
  {
    "vessel_id": "VESSEL-GU-010",
    "vessel_name": "G.U.S. Endeavor's Reach",
    "aliases": [],
    "class_id": "CLASS-RELIANT-01",
    "allegiance": "galactic_union",
    "commanding_officer": null,
    "status": "active",
    "home_port": null,
    "location_type": "moving",
    "specifications": {},
    "narrative_significance": "standard",
    "certainty": "STAGING",
    "doc_sources": ["GUMAS_L2_World_Bible.md"],
    "notes": "Example vessel for Reliant-Class"
  },
  {
    "vessel_id": "VESSEL-GU-011",
    "vessel_name": "G.U.S. Valiant Spear",
    "aliases": [],
    "class_id": "CLASS-VANGUARD-01",
    "allegiance": "galactic_union",
    "commanding_officer": null,
    "status": "active",
    "home_port": null,
    "location_type": "moving",
    "specifications": {},
    "narrative_significance": "notable",
    "certainty": "STAGING",
    "doc_sources": ["GUMAS_L2_World_Bible.md"],
    "notes": "Cutting-edge heavy combat vessel; newly entering service as part of Fleet Modernization"
  },
  {
    "vessel_id": "VESSEL-GU-012",
    "vessel_name": "G.U.S. Resolute Dawn",
    "aliases": [],
    "class_id": "CLASS-DIPLOMATIC-01",
    "allegiance": "galactic_union",
    "commanding_officer": null,
    "status": "active",
    "home_port": null,
    "location_type": "moving",
    "specifications": {},
    "narrative_significance": "notable",
    "certainty": "STAGING",
    "doc_sources": ["GUMAS_L2_World_Bible.md"],
    "notes": "Diplomatic & Intelligence Flagship; high-level diplomatic missions, intelligence coordination"
  },
  {
    "vessel_id": "VESSEL-GU-013",
    "vessel_name": "G.U.S. Kharon",
    "aliases": [],
    "class_id": null,
    "allegiance": "galactic_union",
    "commanding_officer": null,
    "status": "active",
    "home_port": null,
    "location_type": "moving",
    "specifications": {},
    "narrative_significance": "background",
    "certainty": "UNCONFIRMED",
    "doc_sources": ["l_2_physical_locations_index_deduplicated_draft_v_1.md"],
    "notes": "Class unknown; mentioned in location index as moving location"
  },
  {
    "vessel_id": "VESSEL-GU-014",
    "vessel_name": "G.U.S. Sablewake",
    "aliases": [],
    "class_id": null,
    "allegiance": "galactic_union",
    "commanding_officer": null,
    "status": "active",
    "home_port": null,
    "location_type": "moving",
    "specifications": {},
    "narrative_significance": "background",
    "certainty": "UNCONFIRMED",
    "doc_sources": ["l_2_physical_locations_index_deduplicated_draft_v_1.md"],
    "notes": "Class unknown; mentioned in location index as moving location"
  }
]
```

### 3.2 Non-Union Vessels

```json
[
  {
    "vessel_id": "VESSEL-AI-001",
    "vessel_name": "Nemesis Prime",
    "aliases": ["The Nemesis"],
    "class_id": "CLASS-LEVIATHAN-01",
    "allegiance": "ai_warlord_collective",
    "commanding_officer": "Nemesis Core Intelligence",
    "status": "active",
    "home_port": "AI-FRINGE-01",
    "location_type": "moving",
    "specifications": {
      "primary_weapons": ["Unknown - massive firepower"],
      "defensive_systems": ["Self-evolving countermeasures"],
      "propulsion": "Unknown",
      "support_craft": ["Autonomous drone swarms"],
      "special_systems": ["Self-evolving combat AI"]
    },
    "narrative_significance": "flagship",
    "certainty": "STAGING",
    "doc_sources": ["GUMAS_L2_World_Bible.md"],
    "notes": "Primary separatist command vessel and symbol of AI resistance"
  },
  {
    "vessel_id": "VESSEL-OC-001",
    "vessel_name": "Khar'Thyrix",
    "aliases": ["The Star-Eater"],
    "class_id": "CLASS-DREADRAIDER-01",
    "allegiance": "outer_colonies",
    "commanding_officer": "Pirate Queen Theryn Kael'Vakar",
    "status": "active",
    "home_port": null,
    "location_type": "moving",
    "specifications": {},
    "narrative_significance": "flagship",
    "certainty": "STAGING",
    "doc_sources": ["gumas_origin_thread_synthesis_staging_dossier_v_0.md"],
    "notes": "Outer Colonies leviathan-class dread-raider; mobile fortress / refugee ship / black-market hub; command nexus for Kael'Vakar's confederation"
  }
]
```

---

## 4) Registry Statistics

| Category | Count | Status |
|----------|-------|--------|
| **Ship Classes** | 12 | All STAGING |
| **Union Classes** | 10 | STAGING |
| **Non-Union Classes** | 2 | STAGING |
| **Named Vessels** | 16 | Mixed |
| **Union Vessels** | 14 | 12 STAGING, 2 UNCONFIRMED |
| **Non-Union Vessels** | 2 | All STAGING |
| **Vessels with Full Specs** | 2 | Judicator Prime, Nemesis Prime |
| **Vessels Needing Class Assignment** | 2 | G.U.S. Kharon, G.U.S. Sablewake |

---

## 5) Open Items (Resolve Before CANON_PROMOTE)

### 5.1 Missing Data

| Item | Gap | Priority |
|------|-----|----------|
| G.U.S. Kharon | Class unknown | P2 |
| G.U.S. Sablewake | Class unknown | P2 |
| Velar Imperium ships | No vessels defined | P1 |
| Separatist Confederation ships | Only Nemesis Prime defined | P2 |
| PMC Syndicate ships | No vessels defined | P3 |

### 5.2 Schema Decisions

| Decision | Options | Recommendation |
|----------|---------|----------------|
| Vessel ID format | `VESSEL-XX-NNN` | Use faction prefix (GU, AI, OC, VE, SC, PM) |
| Class-to-vessel relationship | 1:many | A class can have many vessels |
| Location type inheritance | Class → Vessel | Defense platforms default to `fixed`; others to `moving` |

### 5.3 Crosswalk Requirements

- Link vessels to home ports (location registry)
- Link vessels to commanding officers (character registry)
- Link vessels to factions (polity registry)

---

## 6) Integration Notes

### 6.1 Add to Machine-Readable Packet

Replace §3.5 Ship Registry with:

```json
{
  "ship_classes": [...],
  "named_vessels": [...],
  "registry_version": "1.0.0",
  "statistics": {
    "total_classes": 12,
    "total_vessels": 16,
    "union_vessels": 14,
    "non_union_vessels": 2
  }
}
```

### 6.2 PR Patch Queue Addition

```json
{
  "patch_id": "L2-P1-050",
  "title": "Complete L2 Ship Registry",
  "status": "READY_FOR_REVIEW",
  "notes": "Consolidates World Bible fleet data into machine-readable format"
}
```

---

## 7) Senior Staff Sign-Off

| Role | Name | Status |
|------|------|--------|
| Commander | Alex Thorne | ☐ PENDING |
| Chief Security Officer | Julian Markov | ☐ PENDING |
| Chief Science Officer | Varya Lin | ☐ PENDING |
| Engineering Lead | Jiro Tanaka | ☐ PENDING |

---

**Document Status:** STAGING — Awaiting review  
**Next Action:** Senior staff approval → Merge into machine-readable packet §3.5
