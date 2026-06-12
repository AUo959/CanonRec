---
title: ORION Drift Containment Protocol
doc_id: ORION.GOV.DRIFTPROTOCOL.0002
doc_type: reference
version: 1.1.0
last_updated: 2026-02-07
authority: canonical
layer: L3
domain: governance
tags:
  - drift
  - containment
  - integrity
  - audit
summary: Detect, log, and contain drift across L1–L3.
ad_code: AD-400
topic_type: Task
audience: operator
status: active
storage: perplexity_space
---
# ORION Drift Containment Protocol (v1.1.0)

Drift signals:
- new facts without cited doc_id / file provenance
- L3 language leaks into L1 reality claims
- entity names fork instead of using the Entity Registry
- contradictions get blended

Containment steps:
1) quarantine as draft (do not overwrite canon)
2) log drift (LOG__DRIFT_LOG)
3) log conflicts (LOG__CONFLICT_MATRIX)
4) propose repair/promotion (LOG__PROMOTION_QUEUE)

