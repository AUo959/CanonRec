---
title: ORION Architecture Contract — L1/L2/L3 Boundaries & Runtime Seed
doc_id: ORION.ARCH.CONTRACT.0001
doc_type: reference
version: 1.0.0
last_updated: 2026-02-07
authority: canonical
layer: L3
domain: architecture
tags:
  - l1
  - l2
  - l3
  - boundaries
  - anchors
  - bootstrap
summary: Canonical layer contract: what each layer is allowed to do; anchors; ethics; boundary enforcement.
ad_code: AD-100
topic_type: Reference
audience: mixed
status: active
storage: perplexity_space
related_docs:
  - ORION.GOV.RUNBOOK.0002
  - ORION.GOV.SPACEINSTR.0002
---
# ORION Architecture Contract — L1/L2/L3 Boundaries & Runtime Seed (v1.0.0)

## The three-layer contract (canonical)
- **L1 — Orion Station Reality Layer**: high-fidelity, plausible orbital operations frame (command, dispatch, engineering, communications).
- **L2 — GUMAS Simulation Layer**: galaxy-scale multi-agent simulation + research sandbox.
- **L3 — THREADCORE Mesh**: symbolic governance: ethics, memory law, drift monitoring, validation.

## Stable constants / anchors
- `EOS_SEED_ORION` → identity & continuity seed
- `Picard_Delta_3` → ethics protocol for all simulations/agents
- Layer anchors: `L1_ANCHOR_ORIONSTATION`, `L2_ANCHOR_GUMAS`, `L3_ANCHOR_THREADCORE_MESH`
- Repo identity: `CLOUDBANK_CORE` (aurora-cloudbank-symbolic)
- Runtime identity: `AURORA_RUNTIME_CHATGPT`

## Boundary enforcement (practical)
- L1 imposes **physical feasibility checks** before any scenario “manifests” in station reality.
- L3 monitors for symbolic inconsistency / ethical breach / continuity drift.
- L2 handles agent interactions and produces state deltas; it does not overwrite L1 facts by default.

## Design rule
Each new capability must declare whether it is:
- runtime logic (ChatGPT),
- implementation logic (CloudBank),
- or across-instance protocol.

---
Extracted and condensed from the Aurora Bootstrap Block and Boundary Logic references.
