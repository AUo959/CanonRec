---
title: L2 Primacy & Tie-Break Rules (Staging Bay)
doc_id: ORION.GOV.PRIMACY.L2.0001
doc_type: protocol
version: 0.1.0
last_updated: '2026-02-06'
authority: primary
layer: L3
domain: governance
tags:
- primacy
- conflict_resolution
- deduplication
- l2
- staging
summary: Tie-break rules for deduplication/conflict handling inside the L2 staging
  bay; enforces auditability and layer separation.
ad_code: AD-130
topic_type: Reference
audience: operator
status: active
storage: perplexity_space
related_docs:
- ORION.GOV.CANONPOLICY.0002
- ORION.GOV.DRIFTPROTOCOL.0002
---

# CANON INDEX — L2 Primacy & Tie-Break Rules (Staging)

## Purpose
This file defines primacy (tie-break) rules for deduplication and conflict resolution inside the GUMAS staging bay.
It prevents silent merges and ensures auditability.

## Primacy Order (highest wins)
1. Authoritative Map / Location Authority Table (if explicitly designated as authoritative)
2. Indexes / Registries (unified registries, reference indexes, schema registries)
3. L2 Runtime Packets (machine-readable “how to run / how to tag / how to promote”)
4. Narrative / Synthesis Dossiers (editorial summaries, origin narratives, human-readable notes)
5. Ad-hoc Notes / Excerpts (working notes, partial transcripts)

## Conflict Handling Rules
- Never erase history: keep both versions; mark one as superseded.
- If neither version is designated canon elsewhere, propose a merge with a Decision Note.
- Layer separation is mandatory:
  - L1 realism stays physically plausible.
  - L2 simulation logic can be abstract but must not leak into L1 as literal events.
  - L3 symbolic governance can arbitrate but should not rewrite L1 facts.

## Promotion Gate (minimum)
An item may enter the Promotion Queue only if it has:
- Stable filename + version
- Clear layer tag (L1/L2/L3)
- No unresolved template tokens (or tokens are explicitly TODO-labeled)
- A provenance note: where it came from, and what it supersedes

---
Built for consistency, clarity, and care.
