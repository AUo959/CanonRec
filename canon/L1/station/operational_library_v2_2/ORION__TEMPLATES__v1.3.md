---
title: ORION Templates Pack (consolidated)
doc_id: ORION.TPL.PACK.0002
doc_type: template
version: 1.3.0.0
last_updated: 2026-02-08
authority: primary
layer: L3
domain: governance
tags:
  - templates
  - runthrough
  - incident
  - dispatch
  - promotion
  - document_map
summary: All essential templates consolidated into one file to preserve cap headroom.
ad_code: AD-100
topic_type: Task
audience: operator
status: active
storage: perplexity_space
---
# ORION Templates Pack (v1.2.0)

## TEMPLATE - Runthrough Report (L1/L2/L3)
Timestamp: [YYYY-MM-DD HH:MM UTC-05]

### Phase 0 - Boot receipts
Anchor: EOS_SEED_ORION; ethics: Picard_Delta_3.  
Sources used: (doc_ids + filenames)

### Phase 1 - L1 Log
...

### Phase 2 - L2 State Delta
...

### Phase 3 - L3 Receipts
Ethics + drift + conflicts.

### Phase 4 - Consolidation
Promotions proposed → Promotion Queue (never auto-canon).

---

## TEMPLATE - Document Map (for long docs)
- Purpose (1-2 lines)
- Sections:
  - §1 Title - (keywords)
  - §2 Title - (keywords)
  - §3 Title - (keywords)

---

## TEMPLATE - L1 Incident Report
- Incident ID:
- Timestamp (UTC-05):
- Location/module:
- Trigger:
- Immediate risk:
- Actions taken:
- Current status:
- Follow-up owner:
- Linked docs/logs:

---

## TEMPLATE - Dispatch Entry
Timestamp: [YYYY-MM-DD HH:MM UTC-05]
- Objective:
- Constraints:
- Resources requested:
- Risk notes:
- Completion criteria:
- Logging: (Run Log entry + incident ID if needed)

---

## TEMPLATE - Canon Promotion Proposal (minimal)
- Proposal ID:
- Candidate fact(s):
- Source doc_ids:
- Rationale:
- Conflicts:
- Ethics receipts (Picard_Delta_3):
- Decision: pending / approved / rejected



## Template - Multi-file response (archive-first)
When producing a response that generates more than two files, include in-chat:

- Files included in the archive:
  - `00_README_INDEX.md`
  - `bundle.manifest.json`
  - (list every file path inside the ZIP)

- Completeness:
  - "Completeness: This archive contains all materials generated in this response. No additional files were produced outside the archive."

## Appendix - Workspace Profile (directory-awareness input)
Use this only if the operator provides it. Do not invent paths.

### Workspace Profile (example JSON)
```json
{
  "profile_id": "ORION_WORKSPACE__EXAMPLE__v0.1",
  "created_at": "2026-02-08T14:43:00Z",
  "anchor_seed": "EOS_SEED_ORION",
  "ethics_protocol": "Picard_Delta_3",
  "roots": [
    {"label":"ORION_ROOT","path":"~/OrionStation/","notes":"Primary project root"},
    {"label":"AURORA_REPO","path":"~/OrionStation/AuroraCloudBankSymbolic/","notes":"Git working copy"}
  ],
  "routing_rules": [
    {"match":{"layer":"L3","domain":"governance"}, "target_root_label":"AURORA_REPO", "target_subpath":"l3/governance/", "strategy":"append"}
  ]
}
```

---

Built for consistency, clarity, and care.
