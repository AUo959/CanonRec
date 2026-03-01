---
entity_id: L3-SCHEMA-THREADCORE-BENCH-001
entity_type: schema_definition
layer: L3
certainty: STAGING
doc_sources:
  - echoes_benchmark_thread_meta_narrative_technical_report.md
---

schema_name: ThreadCore Benchmark Loom Run Schema
version: "1.0"
fields:
  - timestamp
  - model
  - scenario_id
  - persona
  - filename
  - latency_s
  - trust_score
  - tone_drift
  - symbolic_leakage
notes: Candidate schema extracted from Echoes benchmark report; no detected external name collision.
