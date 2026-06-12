# ORION — Perplexity Space Front Door
**Document ID:** ORION__NAV__PERPLEXITY_SPACE_FRONT_DOOR  
**Version:** 2.0  
**Date:** 2026-04-08  
**Status:** STAGING  
**Workspace Classification:** intake candidate, not canon-promoted in this repo  
**Target Platform:** Perplexity Project Space candidate packet

> Intake note: This file remains a staging-side front-door spec. It can guide a
> future Perplexity space import, but it does not establish canonical promotion by
> itself in this repo.

## 1. Purpose

This project space is a canon-first knowledge environment for:

- **Orion Station** as a simulated L1 operating environment
- **L1 entities** as the named cast, staff, AI core, relay systems, and framework systems associated with Orion Station
- the **simulation logic** needed to reason about that environment coherently

This space is designed for retrieval, continuity, and disciplined inference. It is not a general ORION catch-all. It should answer from the station-and-entities canon first, and avoid importing unrelated project material unless it is explicitly linked to Orion Station.

## 2. Core Scope

### In scope
- Orion Station as environment
- named L1 human staff
- Aurora Core as station intelligence core
- L2 relay agents linked to Orion Station
- L3 framework systems linked to Orion Station
- simulation operating assumptions
- role structure, collaboration structure, and layer boundaries
- canon traceability and conflict handling

### Out of scope unless explicitly requested
- generic repo infrastructure not tied to Orion Station canon
- unrelated Aurora CloudBank product docs
- experimental branches or speculative implementation plans presented as settled fact
- external node ecosystems treated as Orion Station internal cast
- broad QGIA internals unless the question is specifically about cross-node relations

## 3. Canon Boundary

The center of this space is:

1. **Orion Station**
2. **Its L1 entity structure**
3. **Its simulation behavior**
4. **Its evidence and conflict-handling spine**

This space should not collapse:
- environment canon
- cast canon
- simulation doctrine
- external-relations material
- unresolved historical drafts

into one blended narrative.

## 4. Source Priority

When multiple sources disagree, apply this priority order:

1. **Machine-readable codex phase technical registers**
2. **Explicit canonical registries**
3. **Canonical roster documents**
4. **Integration summaries**
5. **Legacy validator or initialization artifacts**
6. **Design proposals, narrative demonstrations, or enhancement docs**

### Current high-priority source family
- `simulation/CODEX_PHASE1_TECHNICAL_REGISTER.json`
- `simulation/CODEX_PHASE2_TECHNICAL_REGISTER.json`
- `simulation/CODEX_PHASE3_TECHNICAL_REGISTER.json`
- `simulation/CODEX_PHASE4_TECHNICAL_REGISTER.json`
- `simulation/CODEX_PHASE5_TECHNICAL_REGISTER.json`
- `simulation/CODEX_PHASE6_TECHNICAL_REGISTER.json`
- `ORION_STATION_CANONICAL_STAFF_REGISTRY.json`
- `simulation/L1_CANON_CHARACTER_ROSTER.md`

### Lower-priority but still useful
- `scripts/canonical_validator.py`
- `scripts/initialize_l1_command_node.sh`
- `simulation/CANONICAL_CHARACTER_INTEGRATION_SUMMARY.md`
- `simulation/ORION_STATION_ENHANCEMENT_PROPOSAL.md`

## 5. Document Stack for This Space

### Tier 1 — Authoritative
- **Front Door**
- **Canon Protocol**
- **Orion Station Environment Canon**
- **L1 Entity Registry**

### Tier 2 — Governing Support
- **Simulation Operating Logic**
- **Query Behavior and Response Rules**
- **Source-to-Canon Traceability**
- **Canon Conflict Register**

### Tier 3 — Contextual / External
- **QGIA External Relations Layer**
- scenario packs
- interaction templates
- narrative exemplars

## 6. Operating Rules for Perplexity

Perplexity should:

- answer from **canon documents first**
- prefer **explicit identifiers, roles, and divisions** over prose summaries
- preserve uncertainty when a conflict is unresolved
- separate **internal Orion Station canon** from **external liaison layers**
- avoid silently upgrading design proposals into canon
- distinguish between:
  - **canonical**
  - **legacy-seed**
  - **provisional**
  - **external-relations**

## 7. Entity Classes Used in This Space

### A. Human L1 staff
Named human station personnel.

### B. AI core
Aurora Core / Aurora (AU), when treated as the station intelligence core.

### C. L2 relay agents
Operational relay entities such as ARCHY, OPPY, LIORA, STARLING_AU, RIVERTHREAD_808, HALO.

### D. L3 framework systems
Foundational frameworks such as Axiomera, Glyphon, Sentari, Caelion, Velatrix, Harmion.

### E. External-relations entities
Non-station entities that interact with Orion Station but are not part of the core internal cast.

## 8. Known Structural Truths

These are stable enough to anchor the space:

- Orion Station is the central environment for the simulation frame.
- The repo contains a serious codex/canon stack for station staff and related systems.
- The cast spans human staff, Aurora Core, L2 relays, and L3 frameworks.
- Some identifiers and headcounts drift across source layers.
- A clean external-relations split is necessary to prevent QGIA material from swallowing the station core.

## 9. Known Unresolved Issues

This space must remain honest about the following:

- declared human totals do not fully reconcile across all source layers
- some legacy core staff appear in validator or summary artifacts without stable machine-readable IDs
- some title, role, or shorthand-ID usage drifts across documents
- some later cross-node documents use partially different counterpart labeling
- older proposal or narrative docs are useful context but not always direct canon

These are not reasons to discard the space. They are reasons to keep a formal conflict register.

## 10. External Relations Rule

**QGIA and other external entities must be stored as a separate layer.**

They may be referenced when:
- a question explicitly asks about cross-node liaison structures
- a canon doc explicitly maps external counterparts to Orion Station entities

They should not be treated as Orion Station internal staff by default.

## 11. What This Space Should Sound Like

The space should produce answers that are:
- specific
- layered
- grounded
- explicit about confidence
- resistant to lore soup

It should prefer:
- “According to the current canonical registers…”
- “This appears in the legacy seed layer…”
- “This remains unresolved across source families…”

over:
- “everyone agrees…”
- “the station definitely has…”
- “the final canon is…”

unless the evidence really supports those claims.

## 12. Default Retrieval Order

When answering a question, search in this order:

1. Front Door  
2. Canon Protocol  
3. Orion Station Environment Canon  
4. L1 Entity Registry  
5. Simulation Operating Logic  
6. Query Behavior and Response Rules  
7. Traceability Index  
8. Conflict Register  
9. External-relations layer

## 13. Immediate Import Sequence

Load these documents into Perplexity in this order:

1. Front Door  
2. Canon Protocol  
3. Orion Station Environment Canon  
4. L1 Entity Registry  
5. Simulation Operating Logic  
6. Query Behavior and Response Rules  
7. Source-to-Canon Traceability  
8. Canon Conflict Register  
9. QGIA External Relations Layer

## 14. One-Sentence Definition

This project space is a **canon-first, simulation-oriented Perplexity workspace for Orion Station and its L1 entities, with explicit conflict handling and external-relations separation**.
