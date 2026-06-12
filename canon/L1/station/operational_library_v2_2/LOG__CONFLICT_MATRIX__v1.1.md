---
title: Conflict Matrix Ledger
doc_id: ORION.LOG.CONFLICTS.0001
doc_type: log
version: 1.1.0
last_updated: 2026-02-07
authority: primary
layer: L3
domain: governance
tags:
  - log
  - conflicts
  - authority
  - resolution
summary: "Ledger of known contradictions/duplicates + the chosen resolution."
related_docs:
  - ORION.ENT.REGISTRY.0001
  - ORION.ENT.L1ROSTER.0001
  - ORION.ENT.CONSTELLATION.0001
  - ORION.TOOL.GUMASENGINE.0001
audience: mixed
topic_type: Reference
---

# Conflict Matrix Ledger (v1.1.0)
**Timestamp (UTC-05):** 2026-02-07 16:29 UTC-05

| Conflict ID | Type | Artifact / Scope | Resolution |
|---|---|---|---|
| C-0001 | revision_conflict | Duplicate L2 engine source variants inside New_Engine_Archive | Prefer outputs/gumas_engine variant; archive root-level legacy copies. |
| C-0002 | Name variant mismatch | Helena Vu vs Dr. Helena Vu (same person) | Normalize under Entity Registry; keep title as display prefix in roster/profiles. |
| C-0003 | Name variant mismatch | Julian Markov vs Lt. Julian Markov (same person) | Normalize under Entity Registry; keep rank as display prefix. |
| C-0004 | Name variant mismatch | Maren Koss vs Dr. Maren Koss (same person) | Normalize under Entity Registry; treat 'Dr.' as display prefix unless roster confirms. |
| C-0005 | authority_pointer_gap | L1 roster references an authority JSON registry not present in space bundle | Use `ORION__ENTITY_REGISTRY__v1.0.md` as interim authority pointer; log missing JSON as upstream gap (see Repo Context). |
| C-0006 | drift_threshold_mismatch | Repo Context mentions drift threshold 0.002 vs ThreadCore v3.5.1 drift max 0.2 | Treat 0.002 as *repo-tooling* threshold pending verification; keep operational drift alerts at 0.2 in this space until reconciled. |
| C-0007 | staging_token_residue | Origin-thread synthesis contained uncompiled template tokens | Repaired by converting tokens to explicit TODO blocks; keep dossier authority=draft until compiled from authoritative inputs. |

## Notes
- **C-0005..C-0007** come from integrating the BAY01 AllMarkdown archive: authority-pointer gaps, drift-threshold variance, and staging-token residue.
- **C-0001** originates from the staging bundle conflict scan (duplicate `engine.py/models.py/scenarios.py/tests` variants). The resolved engine package matches the variant that passes the full test suite.
- **C-0002..C-0004** are *name-prefix collisions* between the roster and extracted profiles; the Entity Registry standardizes them so downstream documents don’t fork new “phantom” entities.

---
Built for consistency, clarity, and care.