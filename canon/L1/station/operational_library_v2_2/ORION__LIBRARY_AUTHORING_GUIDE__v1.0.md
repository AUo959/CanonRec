---
title: ORION Library Authoring Guide — Retrieval-Optimized Practice
doc_id: ORION.GOV.AUTHORINGGUIDE.0001
doc_type: reference
version: 1.0.0
last_updated: 2026-02-07
authority: canonical
layer: L3
domain: governance
tags:
  - retrieval
  - progressive_disclosure
  - chunking
  - authority
  - conflicts
summary: Design rules derived from LLM retrieval failure modes (progressive disclosure, lost-in-middle, authority conflicts).
ad_code: AD-100
topic_type: Reference
audience: mixed
status: active
storage: perplexity_space
---
# ORION Library Authoring Guide — Retrieval-Optimized Practice (v1.0.0)

This library is organized for **progressive disclosure**:
Master Index → Category Index → Document Map → Section(s).

## Why (the failure modes)
- **Context waste**: loading “everything” yields low relevance.  
- **Lost-in-the-middle**: important info buried mid-context degrades performance.  
- **Broken cross-references**: chunking severs “see Section X” links.  
- **Authority conflicts**: platforms don’t resolve contradictions.

## Writing rules (hard)
1) Put the **operational answer near the top** of a section.  
2) Use headings as stable anchors (`##`, `###`) and keep sections **~512–1024 tokens** where feasible.  
3) Prefer **one canonical file** over multiple near-duplicates.  
4) Encode **version + authority** in frontmatter and filename.  
5) Any contradiction must be logged (Conflict Matrix) — no silent synthesis.

## Boilerplate control
Avoid repeating large disclaimer blocks across many docs. Keep boilerplate in:
- Master Index, Runbook, Custom Instructions
…and link to it elsewhere.

