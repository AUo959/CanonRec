---
title: L2 GUMAS Engine — Clean Package Artifact
doc_id: ORION.TOOL.GUMASPKG.0001
doc_type: reference
version: 1.0.1
last_updated: 2026-02-07
authority: primary
layer: L2
domain: tooling
tags:
  - gumas
  - package
  - zip
summary: "Explains the cleaned, importable engine ZIP artifact for repos or project spaces."
related_docs:
  - ORION.TOOL.GUMASENGINE.0001
  - ORION.LOG.CONFLICTS.0001
audience: dev
topic_type: Reference
---

# L2 GUMAS Engine — Clean Package Artifact (v1.0.1)

**Artifact:** `L2_GUMAS_ENGINE__CLEAN_PACKAGE__v1.0.1.zip`  
**Timestamp (UTC-05):** 2026-02-07 16:31 UTC-05

## What’s inside
- `modules/gumas/*.py` (engine, models, scenarios, formulas)
- `tests/test_gumas_engine.py`
- `README.md`

## What’s intentionally excluded
- `__pycache__/`
- `.pytest_cache/`
- duplicate “legacy” copies that would break imports

## Why this exists
The staging archive contained duplicate variants; this ZIP preserves the *resolved* importable package that matches the passing pytest suite.

---
Built for consistency, clarity, and care.
