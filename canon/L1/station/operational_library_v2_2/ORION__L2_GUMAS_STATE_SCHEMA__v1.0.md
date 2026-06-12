---
title: L2 State Schema — GUMASState Interpretation Guide
doc_id: ORION.L2.STATE.SCHEMA.0001
doc_type: reference
version: 1.0.0
last_updated: 2026-02-07
authority: primary
layer: L2
domain: simulation
tags:
  - l2
  - gumas
  - state
  - schema
summary: Human-readable guide to interpreting GUMASState and TickResult outputs.
ad_code: AD-300
topic_type: Reference
audience: mixed
status: staging
storage: perplexity_space
---
# L2 State Schema — GUMASState Interpretation Guide (v1.0.0)

Core objects:
- **GUMASState**: world-state at a moment
- **TickResult**: what happened this tick (events + deltas + metrics)

Minimum tick report:
- conflict stage + escalation pressure
- treaty breach score + active treaties
- leader bias vectors
- faction reputations
- notable events

Keep “facts” (candidate canon) separate from “color” (narrative flavor).

