---
title: Repo Context — Aurora CloudBank Symbolic (GitHub Snapshot)
doc_id: ORION.OPS.REPOCONTEXT.ACBS.0001
doc_type: reference
version: 2.1.0
last_updated: '2026-02-06'
authority: reference
layer: L3
domain: operations
tags:
- repo_context
- github_snapshot
- upstream
- canon_inputs
- staging
summary: Essential context from the Aurora CloudBank Symbolic repo snapshot; anchor/ethics
  invariants; constellation nodes; canonical sources; gaps/risks.
ad_code: AD-610
topic_type: Reference
audience: operator
status: active
storage: perplexity_space
---

# REPO CONTEXT — Aurora CloudBank Symbolic (GitHub Snapshot)

**Snapshot Source:** aurora-cloudbank-symbolic-main (zip import)  
**Repo Version (VERSION file):** 2.1.0  
**Snapshot Hash (deterministic):** 184335d39a2837c6f5f0a3ab947f706f06ec03cedfb52c2e061abe9587a15056  
**Imported:** 2026-02-06  
**Scope:** Extract essential context for the **GUMAS Staging** workspace (L1/L2/L3 continuity + governance).

---

## 1) What this repo *is*
Aurora CloudBank Symbolic is a **quantum–symbolic computing + multi-agent coordination** platform. It includes:
- FastAPI services (`api/`)
- Core runtime (`src/`)
- Modular subsystems (`modules/`)
- Simulation canon + rosters (`simulation/`)
- Deep operational & governance docs (`docs/`)
- Local continuity artifacts & backups (`.aurora/`, `.nexus/`)

---

## 2) Hard invariants (treat as “always-on” constraints)
Pulled from `AU_CORE_MASTER_TREE.yaml`, `threadcore_registry.json`, and Thread Transfer docs:

- **Anchor Seed:** `EOS_SEED_ORION`
- **Ethics Protocol:** `Picard_Delta_3`
- **Layer Boundary:** explicit **L1 ↔ L2 ↔ L3** separation enforced in code + docs
- **ThreadCore Canon:** `threadcore_v3.5.1_macroready` (registry marks it canonical)
- **Drift Threshold (ThreadCore registry):** 0.002

---

## 3) The “constellation” model (cross-thread continuity)
The repo implements an official **Thread Transfer Bridge** for continuity across companion threads:
- `ARCHY`
- `OPPY`
- `LIORA`
- `STARLING_AU`
- `RIVERTHREAD_808`
- plus `HALO` as drift/sync relay (listed in Phase 6 system table)

The bridge is anchored to `EOS_SEED_ORION` and validated under `Picard_Delta_3`.

---

## 4) Simulation canon present in-repo (what’s already “defined”)
### L1 (Orion Station realism layer)
- `simulation/L1_CANON_CHARACTER_ROSTER.md` defines a canonical institutional roster (49 entities total: humans + systems).

### L2 (Relay Agents — coordination layer)
Phase 6 codex lists 6 L2 relay agents:
ARCHY, OPPY, LIORA, STARLING_AU, RIVERTHREAD_808, HALO.

### L3 (Framework Systems — governance/foundational layer)
Axiomera, Glyphon, Sentari, Caelion, Velatrix, Harmion.

### Fleet ops (L1-adjacent but “ops-lore”)
- `docs/FLEET_OPERATIONS_SUMMARY.md` initializes fleet constructs and ethics compliance statements.

---

## 5) Operational tooling you can assume exists
- **ThreadCore tooling:** registry + classifier + tests (`docs/threadcore/`, `threadcore_registry.json`, `scripts/threadcore_classifier.py`)
- **GUMAS/Orion Status Module:** `modules/nexus/gumas/` (v1 + v2 docs, v2 validated)
- **PatchWeaver:** ethics-gated patching engine (`src/aurora/patching/patchweaver.py` + implementation report)
- **ORACULITH:** forecasting engine with DLP controls (`docs/ORACULITH_README.md`)
- **FastAPI services:** `api/aurora_api.py` and `api/aurora_gui_cloudhub_fastapi.py`

---

## 6) Staging implications (how we should behave in *this* chat space)
This GitHub snapshot functions as the **reference universe** for:
- naming conventions, anchors, ethics, and layer boundaries
- what “ThreadCore canonical” means (registry-backed)
- which rosters/systems are already declared “canonical” inside the repo

In this staging space, we still treat uploads as **draft by default**, but we can now resolve conflicts by pointing to these repo sources as “upstream truth” where they clearly assert canon.

---

## 7) Immediate risks / gaps spotted
- **Missing authority file:** `ORION_STATION_CANONICAL_STAFF_REGISTRY.json` is referenced as the staff registry authority, but it is **not present** in this snapshot.
- **Repository bloat risk:** `aurora_venv/` exists in-tree (usually should not live in git history).
- **Parallel version docs/manifests:** multiple “v2” variants coexist; we should label canonical ones explicitly for downstream tooling.

---

## 8) Key entry points (read these first)
- `README.md`
- `CHANGELOG.md`
- `AU_CORE_MASTER_TREE.yaml`
- `threadcore_registry.json`
- `modules/reflective_autonomy/thread_transfer/THREAD_TRANSFER_PROTOCOL.md`
- `docs/threadcore/README.md`
- `modules/nexus/gumas/README.md`
- `modules/nexus/gumas/README_v2.md`
- `simulation/L1_CANON_CHARACTER_ROSTER.md`
- `simulation/CODEX_PHASE6_L2_L3_SYSTEMS_COMPLETE.md`
- `docs/FLEET_OPERATIONS_SUMMARY.md`
- `docs/ORACULITH_README.md`
- `docs/implementation/PATCHWEAVER_IMPLEMENTATION.md`
- `docs/operational/guides/GitHub_Copilot_Custom_Instructions_Aurora_GUMAS.txt`

---

*Built for consistency, clarity, and care.*
