# L2 — GUMAS Galactic Simulation Canon

**Established:** 2026-06-13 (owner ruling: "all L2 entities should be promoted").
This is the canonical home for the **L2 layer** — the galaxy the GUMAS engine
simulates — mirroring the L1 station canon under `../L1/`. Per the Architecture
Contract: L1 = Orion Station reality, **L2 = GUMAS galactic simulation**,
L3 = THREADCORE governance. Anchor `EOS_SEED_ORION`, ethics `Picard_Delta_3`.

The L2 material is among the **oldest in the project** (traceable to early-2025
conversation exports; see `reports/analysis/l2_lineage_genesis__2026-06-13.md`)
and was reworked several times. Much of it carried a self-declared *"Secondary
Canon (draft / pre-canonical)"* status pending commit to the repo. This routing
**is that commit** — the promotion the source material was written for.

## Structure

| Dir | Contents | Source |
|---|---|---|
| `entities/` | The promoted entity set: characters, `locations/` (23), `organizations/` (12, incl. Union Marshals, Union Senate, Office of Strategic Diplomacy), `mobile_assets/` (16), plus `CANON_LOCK_RECORD` + `DISAMBIGUATION_RECEIPT` | `SIM_ENGINE_OUTPUTS/L2_CANON__2026-03-19/` (March L2 promotion pass) |
| `world_bible/` | GUMAS L2 World Bible v0.2 (lore) | `projects/GUMAS_SIM_2.0/03_SIMULATION/Location_Data/` |
| `map/` | Location Authority Table (LAT), the galactic map **source of truth**, the Physical Galaxy Packet v0.1 | LAT from Sim_Locations; map SoT + packet from `GUMAS_Legacy/Original_Materials/GUMAS_OG/` |
| `marshals_sentinels/` | The **Galactic Marshals** & **Sentinel-Class Power Suit** corpus: the 28KB source-linked ledger, 8 hardware tables (Marshal/enemy starship classes + capabilities, defensive, shielding/propulsion, ship-to-ship combat, vehicles), and the Marshal Standard Kit | `03_SIMULATION/Entity_Profiles/Marshals_Sentinels/` + Mission_Logs |
| `operations/` | Mission logs and narratives: **Operation Obsidian Dawn** (briefing, execution, conflict, outcome), the Excision Task Force mandate, Director Varek Norr profile, Chancellor Zylox's diplomatic-offensive strategy, the Office of Strategic Diplomacy | `03_SIMULATION/Mission_Logs/SimLogsBuild/` |
| `mechanics/` | The **L2 Mechanic Registry** (MECH-GOV-001 Faction Decision Retrieval Model, etc.), polity/ship/character dossiers, the galactic-union mechanics-and-models + canon-reconciliation + character roster | `_staging/recovered_textAu__2026-03-13/L2/` |
| `primary_sources/` | In-world journalism: **The Lanternline** (L2 primary-source newsletter, cycle 38) | `projects/GUMAS_SIM_2.0/02_DEVELOPMENT/` |

## Canon status

- **`entities/`** were promoted in the March 2026 L2 canon pass (CANON_LOCK_RECORD
  present) and are routed here as the canonical entity set.
- **`world_bible/`, `map/`, `marshals_sentinels/`, `operations/`,
  `mechanics/`, `primary_sources/`** are promoted from Secondary Canon to
  **CANON-routed** by this commit, preserving source content verbatim (lore is
  not rewritten — same discipline as the L1 station canon). Where the World
  Bible and the LAT/map disagree on physical placement, **the map is source of
  truth** (per the World Bible's own migration hooks).

## Known open items (logged, not silently resolved)

- The **Mechanic Registry** entities (kind `mechanic`) were blocked in March by
  an L2-validator `entity_kind` gap, not by quality. The registry is canon here;
  realizing **MECH-GOV-001** (memory-driven faction decisions: Q-learning +
  retrieval) in the engine is the outstanding implementation — it exists as
  design, not code (see the genesis lineage report).
- A deeper **raw corpus** (April-2025 session-archive zips: `chat.zip`,
  `conversations.zip`, GUMAS dev kits) contains further Marshals/galaxy material
  not yet extracted. This routing covers the **structured** corpus; the raw
  archives are flagged for a future mining pass.
- L2 canon currently has no per-entity ledger like L1's Entity Ledger v2; a
  future pass can generate one over `entities/`.
