# Canon Reconciliation Report
**Date:** 2026-06-10
**Input:** reports/recovered_canon/ (March-lineage salvage: staff registry v2.4.1, canonical_validation.yaml, THREADCORE v3.5.1 capsule, T70/T71 anchor manifests, continuity anchor state) reconciled against reports/analysis/L1_ENTITY_LEDGER__2026-03-08.json
**Layer:** L1 (characters, station registry) + L3 (contracts, capsules, anchor rules)
**Entities processed:** 41 characters + 1 station registry + 6 L3 artifacts

## Validation Summary
- 41/41 ledger humans carry required L1 character fields (name, role, division, status, summary, provenance); 9 enriched with registry command fields (clearance, reports_to, responsibilities).
- 12 registry command seats: 10 matched to ledger entities; 2 are rotating seat definitions (institutional, not characters — retained inside the station registry artifact, not promoted as characters).
- L3 artifacts promoted as source artifacts (validation contract, THREADCORE capsule, anchor manifests, continuity anchors); schema validation for L3 protocol types deferred to threadcore-governor.

## Conflicts Found
4 role-title conflicts (see DRIFT_LOG.md) — all previously recorded in the ledger's legacy-drift traces. Resolution: defer to ledger; registry titles kept as legacy aliases.

## Drift Artifacts
None beyond the documented role aliases. No identity collisions, no ghost entities, no timeline contradictions. Aurora is intentionally NOT a character entity: canon defines Aurora as `aurora_core` (CORE_SYSTEM, L1 technical node) in the station registry.

## Promotion Assessment
All 41 characters: `CANON_PROMOTE` (ledger certainty was already CANON for 35, STAGING for 6 vessel-crew/cadet entries — their ledger certainty is preserved in frontmatter `registry_authority`/`status`; promotion here makes them resolvable Primary Canon files). Station registry + L3 artifacts: promoted as provenance-bearing source artifacts.

## Action Items
1. Owner: spot-check 2–3 character files for tone/fidelity.
2. Owner: confirm the 6 STAGING-era entities (Lt. Nakamura, Lt. Hassan, Chief Thomson, Samantha Gray, Ren Takahashi, Cadet Mira Chen) belong in Primary Canon or should remain reference-tier.
3. Run threadcore-governor over canon/L3/THREADCORE payload (next session).

## Resolution Addendum — 2026-06-11

Action item 2 resolved: the owner confirmed all 6 STAGING-era entities
(Lt. Nakamura, Lt. Hassan, Chief Thomson, Samantha Gray, Ren Takahashi,
Cadet Mira Chen) for Primary Canon. Frontmatter updated with
`owner_confirmed: 2026-06-11`. All 41 L1 character entities are CANON.
Action item 3 resolved separately: THREADCORE capsule passed the governor
clean (see THREADCORE_GOVERNANCE_RECEIPT__2026-06-10.md).
