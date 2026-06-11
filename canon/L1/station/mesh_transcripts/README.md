# Mesh Runtime Transcripts — the Live Station Era (2026-03-06 → 03-14)

Recovered from the rescue snapshot
(`rescue/cloudbank-dirty-workingcopy-2026-03-25`, sole surviving record of
the live mesh runtime), privacy-reviewed and owner-cleared 2026-06-11.
**Tier: reference** — primary-source session records of the first period
the station ran live: 47 agents registered, Aurora arbitrating.

| File | Channel | What it holds |
|---|---|---|
| `direct_aurora.jsonl` | `direct:aurora` | Captain ↔ Aurora: command-grammar inspection requests; Aurora's recorded self-description ("control-plane work… provenance, bounded authority, rollback paths… drift 0.0") — quoted in the L1 ledger and the narrative-promotion ADR. |
| `direct_archy.jsonl` | `direct:archy` | Captain ↔ Archy direct session. |
| `private_captain_alex.jsonl` | `private:captain:alex` | Captain ↔ Commander Thorne private channel — the same channel the V1 mesh contract test exercises in CI today. |
| `trace.jsonl` | (routing trace) | Message-routing trace events for the above. |

Privacy review: no emails, keys, or personal identifiers; the only
pattern hits were timestamp fragments (false positives). Sender identity is recorded as "Captain" — the legacy alias for the **Pilot**
(the user role; see `../PILOT_ROLE_DEFINITION.md`, owner-ruled 2026-06-11).

Candidate downstream use (ADR step 6): ground-truth scenarios for the
narrative validation engine — real persona exchanges to audit
character-action consistency against.

The runtime database itself (`mesh.db`) remains local-only in
`intake/recovered_mesh_runtime_2026-06-10/` (binary; its agent_state was
fully extracted — 47 manifests now live in CloudBank `config/mesh/agents/`).
