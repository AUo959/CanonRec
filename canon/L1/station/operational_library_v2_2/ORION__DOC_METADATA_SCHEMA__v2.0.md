---
title: ORION Document Metadata Schema
doc_id: ORION.GOV.METASCHEMA.0002
doc_type: schema
version: 2.0.0
last_updated: 2026-02-07
authority: canonical
layer: L3
domain: governance
tags:
  - yaml
  - metadata
  - schema
  - authority
summary: YAML frontmatter contract for ORION docs; tuned for stable retrieval and conflict handling.
ad_code: AD-100
topic_type: Reference
audience: mixed
status: active
storage: perplexity_space
supersedes:
  - ORION__DOC_METADATA_SCHEMA__v1.0.md
---
# ORION Document Metadata Schema (v2.0.0)

## Required keys
```yaml
title:
doc_id:
doc_type:
version:
last_updated:
authority: canonical | primary | reference | draft | run_output | deprecated
layer: L1 | L2 | L3
domain:
tags:
summary:
```

## Strongly recommended keys
```yaml
ad_code:
topic_type: Task | Concept | Reference
audience: operator | dev | narrative | mixed
status: active | staging | archived | deprecated
storage: perplexity_space | github | export_zip | other
related_docs:
depends_on:
supersedes:
contradicts:
```

## Notes
- Filenames must include **version** (platforms do not track versions).
- `contradicts` should be used whenever two docs disagree materially.

