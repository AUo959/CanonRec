---
title: L1 Dispatch Protocol — The Observatory
doc_id: ORION.L1.DISPATCH.PROTOCOL.0002
doc_type: reference
version: 1.1.0
last_updated: 2026-02-07
authority: primary
layer: L1
domain: dispatch
tags:
  - l1
  - dispatch
  - communications
  - briefings
summary: How dispatch requests are written, routed, acknowledged, and logged.
ad_code: AD-200
topic_type: Task
audience: operator
status: active
storage: perplexity_space
---
# L1 Dispatch Protocol — The Observatory (v1.1.0)

Dispatch fields:
- Timestamp (UTC-05)
- Objective
- Constraints
- Resources
- Risk notes
- Completion criteria

Every dispatch yields:
- a short entry in L1 Run Log
- an incident report if safety-critical

