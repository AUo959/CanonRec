# Security Policy

## Supported version

Security fixes target the current `main` branch. Historical ZIP and `.skill`
release artifacts are retained for provenance but are not separately supported
runtime distributions.

## Reporting a vulnerability

Do not open a public issue containing a vulnerability, credential, private
source, or exploit detail. Use GitHub private vulnerability reporting when it
is enabled. Until then, contact the repository owner through an existing
private channel and provide the affected path, impact, and reproduction details.

## Repository security boundary

CanonRec is a source and governance repository, not a hosted service. Its
scripts are developer-operated reconciliation and validation tools. Canon data
is consumed by other repositories only through explicit propagation and review
steps.

Operational credentials are never valid repository content. Deterministic test
values may exist in test fixtures, but they must be clearly scoped and must not
be reused in deployments. Exact historical false positives are recorded by
fingerprint in `.gitleaksignore`; broad rules or path-wide exclusions are not
accepted.

Run the history scan before publication or release:

```bash
make secrets
```

If a real credential is found, revoke or rotate it first. Removing a value from
the current tree does not remove it from Git history.
