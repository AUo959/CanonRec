---
title: L2 GUMAS Engine — Reading Guide
doc_id: ORION.L2.ENGINE.SOURCEGUIDE.0001
doc_type: reference
version: 1.0.0
last_updated: 2026-02-07
authority: primary
layer: L2
domain: simulation
tags:
  - l2
  - gumas
  - engine
  - guide
summary: How to interpret the engine source, and what to reference during runthroughs.
ad_code: AD-300
topic_type: Reference
audience: dev
status: active
storage: perplexity_space
related_docs:
  - ORION.L2.ENGINE.SOURCEBUNDLE.0001
  - ORION.L2.STATE.SCHEMA.0001
  - ORION.LOG.L2RUN.0001
---
# L2 GUMAS Engine — Reading Guide (v1.0.0)

During a runthrough, you normally cite the **Tech Reference** and **API Reference** first.
Use the Source Bundle when:
- you need exact class or function behavior
- you need to resolve ambiguity between docs
- you want to propose a canon promotion tied to implementation reality

Suggested entry points:
- `modules/gumas/engine.py` (orchestration)
- `modules/gumas/models.py` (core types)
- `modules/gumas/scenarios.py` (scenario setup)
- `modules/gumas/formulas.py` (metrics/scoring)

