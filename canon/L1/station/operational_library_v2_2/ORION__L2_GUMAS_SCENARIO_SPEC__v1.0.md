---
title: L2 Scenario Spec — GUMAS Canonical v1
doc_id: ORION.L2.SCENARIO.0001
doc_type: reference
version: 1.0.0
last_updated: 2026-02-07
authority: primary
layer: L2
domain: simulation
tags:
  - l2
  - gumas
  - scenario
  - seed
summary: Defines scenario ID + seeding + initialization pattern for a run.
ad_code: AD-300
topic_type: Task
audience: dev
status: active
storage: perplexity_space
---
# L2 Scenario Spec — GUMAS Canonical v1 (v1.0.0)

Scenario ID: `gumas_canonical_v1`

Initialization:
- choose `seed` (int)
- init engine
- initialize scenario
- record seed + scenario ID in `LOG__L2_RUN_LOG__v1.0.md`

