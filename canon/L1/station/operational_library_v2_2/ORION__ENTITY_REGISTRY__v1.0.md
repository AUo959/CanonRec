---
title: ORION Entity Registry
doc_id: ORION.ENT.REGISTRY.0001
doc_type: reference
version: 1.0.0
last_updated: 2026-02-07
authority: primary
layer: L3
domain: entities
tags:
  - entities
  - registry
  - ids
  - progressive_disclosure
summary: "Single source of truth for entity IDs + preferred names across L1–L3."
related_docs:
  - ORION.IDX.MASTER.0001
  - ORION.ENT.L1ROSTER.0001
  - ORION.ENT.CONSTELLATION.0001
audience: mixed
topic_type: Reference
---

# ORION Entity Registry (v1.0.0)

**Anchor seed:** `EOS_SEED_ORION`  
**Ethics protocol:** `Picard_Delta_3`  
**Timestamp (UTC-05):** 2026-02-07 16:29 UTC-05

## How to use
- Use **Entity ID** + **Preferred Name** when writing new documents.
- Treat **Preferred Name** as the canonical display label; keep variants in local notes, not as new entities.
- If two docs disagree about an entity (role, title, alignment), do **not** merge silently — log it in **ORION.LOG.CONFLICTS.0001**.

## Registry Table (quick scan)
| Entity ID | Preferred Name | Layer | Type | Primary Role / Function | Authority | Sources |
|---|---|---|---|---|---|---|
| ORION.ENTITY.0001 | Commander Alex Thorne | L1 | Human | Station Commander | primary | ORION.ENT.L1ROSTER.0001 |
| ORION.ENTITY.0002 | Dr. Amina Velin | L1 | Human | Symbolic Systems Research Lead | primary | ORION.ENT.L1ROSTER.0001 |
| ORION.ENTITY.0003 | Dr. Amira Sato | L1 | Human | Chief Ethics Officer | primary | ORION.ENT.L1ROSTER.0001 |
| ORION.ENTITY.0004 | Cadet Mira Chen | L1 | Human | Cadet / Trainee (Operations Track) | reference | ORION.ENT.L1ROSTER.0001 |
| ORION.ENTITY.0005 | Carmen Rivas | L1 | Human | Simulation Binding Specialist | primary | ORION.ENT.L1ROSTER.0001 |
| ORION.ENTITY.0006 | Chief Engineer Raj Patel | L1 | Human | Chief Engineer (Systems/DevOps) | primary | ORION.ENT.L1ROSTER.0001 |
| ORION.ENTITY.0007 | Chief Thomson | L1 | Human | Commanding Officer, Repair Tender Beta (Mobile Maintenance Tender) | reference | ORION.ENT.L1ROSTER.0001 |
| ORION.ENTITY.0008 | Lt. Commander Maya Shepard | L1 | Human | Executive Officer (XO) | primary | ORION.ENT.L1ROSTER.0001 |
| ORION.ENTITY.0009 | Dante Kyros | L1 | Human | UX Architect | primary | ORION.ENT.L1ROSTER.0001 |
| ORION.ENTITY.0010 | Prof. Elena Sorensen | L1 | Human | Cognitive Ethicist (Narrative Ethics) | primary | ORION.ENT.L1ROSTER.0001 |
| ORION.ENTITY.0011 | Dr. Elena Vasquez | L1 | Human | Flight Controller | primary | ORION.ENT.L1ROSTER.0001 |
| ORION.ENTITY.0012 | Dr. Elira Noor | L1 | Human | Lead Reflexivity Specialist (AI Ethics Architect) | primary | ORION.ENT.L1ROSTER.0001 |
| ORION.ENTITY.0013 | Emily Roberts | L1 | Human | LLM–Simulation Bridge Developer | primary | ORION.ENT.L1ROSTER.0001 |
| ORION.ENTITY.0014 | Haneul Park | L1 | Human | Immersive Experience Theorist | primary | ORION.ENT.L1ROSTER.0001 |
| ORION.ENTITY.0015 | Lt. Hassan | L1 | Human | Commanding Officer, Logistics Alpha (Cargo Transport) | reference | ORION.ENT.L1ROSTER.0001 |
| ORION.ENTITY.0016 | Helena Vu | L1 | Human | Cultural & HR Director | primary | ORION.ENT.L1ROSTER.0001 |
| ORION.ENTITY.0017 | Ira Menon | L1 | Human | Compiler Engineer | primary | ORION.ENT.L1ROSTER.0001 |
| ORION.ENTITY.0018 | Jessica Martinez | L1 | Human | Backend Architect | primary | ORION.ENT.L1ROSTER.0001 |
| ORION.ENTITY.0019 | Jiro Tanaka | L1 | Human | Chief Engineering Officer | primary | ORION.ENT.L1ROSTER.0001 |
| ORION.ENTITY.0020 | Julian Markov | L1 | Human | Chief Security Officer | primary | ORION.ENT.L1ROSTER.0001 |
| ORION.ENTITY.0021 | Juno Suresh | L1 | Human | Symbolic Systems Artist | primary | ORION.ENT.L1ROSTER.0001 |
| ORION.ENTITY.0022 | Kai Drev | L1 | Human | Interface Ecologist | primary | ORION.ENT.L1ROSTER.0001 |
| ORION.ENTITY.0023 | Keira Halden | L1 | Human | Lead Visual Concept Designer | primary | ORION.ENT.L1ROSTER.0001 |
| ORION.ENTITY.0024 | Dr. Kieran Zhao | L1 | Human | Computational Optimization Lead | primary | ORION.ENT.L1ROSTER.0001 |
| ORION.ENTITY.0025 | Leena Porter | L1 | Human | Bridge Operations Officer | primary | ORION.ENT.L1ROSTER.0001 |
| ORION.ENTITY.0026 | Marcus Chen | L1 | Human | Performance Optimization Engineer | primary | ORION.ENT.L1ROSTER.0001 |
| ORION.ENTITY.0027 | Dr. Maren Koss | L1 | Human | Cognitive Drift Mapper | primary | ORION.ENT.L1ROSTER.0001 |
| ORION.ENTITY.0028 | Lt. Nakamura | L1 | Human | Commanding Officer, Guardian Sentinel (Security Corvette) | reference | ORION.ENT.L1ROSTER.0001 |
| ORION.ENTITY.0029 | Naomi Vell | L1 | Human | Narrative Framework Engineer | primary | ORION.ENT.L1ROSTER.0001 |
| ORION.ENTITY.0030 | Olivia Nguyen | L1 | Human | QA & Continuity Auditor | primary | ORION.ENT.L1ROSTER.0001 |
| ORION.ENTITY.0031 | Rei Vatra | L1 | Human | Atmospheric Painter & Color Theorist | primary | ORION.ENT.L1ROSTER.0001 |
| ORION.ENTITY.0032 | Dr. Ren Feldman | L1 | Human | Chief Medical Officer | primary | ORION.ENT.L1ROSTER.0001 |
| ORION.ENTITY.0033 | Ren Okada | L1 | Human | Systems Portability Specialist | primary | ORION.ENT.L1ROSTER.0001 |
| ORION.ENTITY.0034 | Ren Takahashi | L1 | Human | Psycho-Acoustic Systems Engineer, ORS-05 *Lacewing* (Sensor & Human-Factors Acoustics) | reference | ORION.ENT.L1ROSTER.0001 |
| ORION.ENTITY.0035 | Ryan Patel | L1 | Human | Systems Integration Engineer | primary | ORION.ENT.L1ROSTER.0001 |
| ORION.ENTITY.0036 | Samantha Gray | L1 | Human | Senior Pilot, ORS-05 *Lacewing* (Training / Cultural Liaison Flight) | reference | ORION.ENT.L1ROSTER.0001 |
| ORION.ENTITY.0037 | Samantha Lee | L1 | Human | Logging & Observability Engineer | primary | ORION.ENT.L1ROSTER.0001 |
| ORION.ENTITY.0038 | Tariq El-Sayegh | L1 | Human | Speculative Systems Theorist (Stress Testing) | primary | ORION.ENT.L1ROSTER.0001 |
| ORION.ENTITY.0039 | Tobias Qin | L1 | Human | Code/Narrative Systems Engineer | primary | ORION.ENT.L1ROSTER.0001 |
| ORION.ENTITY.0040 | Varya Lin | L1 | Human | Chief Science Officer | primary | ORION.ENT.L1ROSTER.0001 |
| ORION.ENTITY.0041 | Vincent Kale | L1 | Human | Layer Isolation Theorist | primary | ORION.ENT.L1ROSTER.0001 |
| ORION.ENTITY.0042 | ARCHY – Architectural Coordination Relay (L2) | L2 | Relay Agent | — | primary | ORION.ENT.CONSTELLATION.0001 |
| ORION.ENTITY.0043 | HALO – Drift Anchor & Synchronization Relay (L2) | L2 | Relay Agent | — | primary | ORION.ENT.CONSTELLATION.0001 |
| ORION.ENTITY.0044 | LIORA – Communications & Interface Relay (L2) | L2 | Relay Agent | — | primary | ORION.ENT.CONSTELLATION.0001 |
| ORION.ENTITY.0045 | OPPY – Operational Flight & Data Relay (L2) | L2 | Relay Agent | — | primary | ORION.ENT.CONSTELLATION.0001 |
| ORION.ENTITY.0046 | RIVERTHREAD_808 – Logistics & Memory Relay (L2) | L2 | Relay Agent | — | primary | ORION.ENT.CONSTELLATION.0001 |
| ORION.ENTITY.0047 | STARLING_AU – Continuity & Reflection Dispatcher (L2) | L2 | Relay Agent | — | primary | ORION.ENT.CONSTELLATION.0001 |
| ORION.ENTITY.0048 | Aurora (AU) – Station Intelligence Core | L2 | System Entity | — | primary | ORION.ENT.CONSTELLATION.0001 |
| ORION.ENTITY.0049 | Axiomera – Ethics Arbitration Framework (L3) | L3 | Framework | — | primary | ORION.ENT.CONSTELLATION.0001 |
| ORION.ENTITY.0050 | Caelion – Anchor Propagation Framework (L3) | L3 | Framework | — | primary | ORION.ENT.CONSTELLATION.0001 |
| ORION.ENTITY.0051 | Glyphon – Drift Alignment Framework (L3) | L3 | Framework | — | primary | ORION.ENT.CONSTELLATION.0001 |
| ORION.ENTITY.0052 | Harmion – Symbolic Compression Framework (L3) | L3 | Framework | — | primary | ORION.ENT.CONSTELLATION.0001 |
| ORION.ENTITY.0053 | Sentari – Resonance Stabilization Framework (L3) | L3 | Framework | — | primary | ORION.ENT.CONSTELLATION.0001 |
| ORION.ENTITY.0054 | Velatrix – Anti-Obfuscation Framework (L3) | L3 | Framework | — | primary | ORION.ENT.CONSTELLATION.0001 |

## Normalization notes
- Titles like **Dr. / Prof. / Lt.** are treated as *display prefixes*; the registry key is the person beneath the prefix.
- The L1 roster contains additional **STAGING** crew entries not present in the extracted constellation profiles. Those remain in the roster; they are not promoted automatically.

---
Built for consistency, clarity, and care.
