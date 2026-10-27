# Deep security mode (the absorbed `security-audit` skill)

This skill absorbs the machine-checkable core of the sibling `security-audit`
skill, so a full security pass does not need that skill installed.

| What | Where it lives |
|------|----------------|
| The finding schema (`confirmed` / `needs_validation` / `rejected`) | `scripts/security_audit_pack/report-schema.json` |
| The two validators | `scripts/security_audit_pack/validate-findings.cjs`, `validate-coverage-ledger.cjs` |
| A portable (Windows-safe) re-implementation of both checks | `scripts/schema_validate.py` |
| The runner that produces and validates the artefacts | `scripts/security_audit.py` |
| The hunting playbooks (attack classes + domain companions) | this folder |

## Run it

```bash
python scripts/security_audit.py --root <app_root>              # writes qa/security/
python scripts/security_audit.py --root <app_root> --json       # machine-readable
```

It produces two files inside the app under review:

* `qa/security/findings.json` - one record per finding, in the security-audit schema.
* `qa/security/coverage-ledger.json` - what was inspected, per
  surface x boundary x subsystem x attack class, with the evidence of each attempt.

Both are then validated. The Node validators are authoritative where they can run; they refuse to
run on platforms without no-follow, nonblocking file access (Windows), and the report says so
explicitly instead of pretending the check passed. The portable Python check in
`scripts/schema_validate.py` always runs, so the artefacts are verified on every platform.

Exit codes: `0` = valid, `1` = a validator rejected the artefacts, `2` = no validator available.

## How a finding is classified

The static scan (Gate E) produces a flat HIGH/MEDIUM/LOW list. This mode maps it onto the
security-audit doctrine, which is stricter than "the regex matched":

| Static result | Verdict | Why |
|---------------|---------|-----|
| HIGH + credential material (secret, API key, token, password, private key) | `confirmed` | The exposure is a fact: the credential is in the reviewed source, so every reader of the repository obtains it. The credential's validity is *not* tested and the record says so. |
| Everything else | `needs_validation` | A pattern match never proves a trust boundary was crossed. The record carries the exact blocker and a safe local validation plan. |

Nothing is reported as `rejected` automatically: a rule that fired but turned out to be a false
positive should be rejected by a human, with the reason recorded.

Every record carries a `fingerprint` (stable id), a `trace` (file + line + scope), `evidence`, and
- for confirmed findings - `root_cause`, `intended_behavior`, `conditions`, `execution`,
`remediation` and a calibrated `severity` with `confidence`.

## The coverage ledger

A ledger unit is one `surface :: boundary :: subsystem :: attack_class` cell. `coverage_id` is the
canonical percent-encoded join of those four references, so the same unit always has the same id
across runs and machines.

Rules the artefacts must satisfy (enforced by both validators):

* every unit declares what it looked at (`starting_paths`, `reviewed_paths`), which checks ran
  (`local_checks`), and which fingerprints came out (`result_fingerprints`);
* a `covered` unit has evidence and **no** fingerprints; a `candidate` unit has fingerprints;
* every reviewed path is owned by a check, and every owned path appears in the aggregate;
* archived attempts have strictly increasing waves that precede the current wave, and each
  attempt has a fresh owner.

## The playbooks in this folder

| File | Use it for |
|------|-----------|
| `SECURITY-AUDIT-WORKFLOW.md` | the six-phase workflow (recon -> hunting waves -> validation -> artefacts -> independent verification -> report) |
| `RECONNAISSANCE.md` | mapping the source, trust boundaries and the coverage units |
| `HUNTING.md` | how to run an isolated hunter and what a candidate must contain |
| `VALIDATION-AND-REPORTING.md` | how a candidate becomes a finding, and the report rules |
| `ATTACK-CLASSES.md` | the canonical attack-class catalogue used by the ledger |
| `AI-AND-LLM.md` | LLM/agent specific classes (prompt injection, tool abuse, data leakage) |
| `CLIENT-SIDE.md` | XSS, storage, postMessage, third-party scripts |
| `CLOUD-AND-DEPLOYMENT.md` | IAM, storage policies, secrets, CI/CD |
| `DATA-ISOLATION-AND-LIFECYCLE.md` | tenant isolation, PII lifecycle, retention, deletion |
| `DESKTOP-MOBILE-AND-LOCAL-IPC.md` | local IPC, deep links, desktop and mobile surfaces |
| `MEMORY-SAFETY-AND-BINARY.md` | unsafe memory and binary parsing |
| `PROTOCOLS-RPC-AND-MESSAGING.md` | RPC/queue/deserialization surfaces |
| `RESOURCE-EXHAUSTION-AND-AVAILABILITY.md` | DoS, quotas, cost amplification |
| `SUPPLY-CHAIN-AND-RELEASE.md` | dependencies, lockfiles, CI, release integrity |
| `WEB-PROTOCOL-AND-AUTH.md` | sessions, tokens, OAuth, CSRF, request smuggling |

## Scope and limits

This is a **source-first static pass**, not a pen test. It does not probe live endpoints, does not
try to escalate, and does not claim a vulnerability it cannot point at in the source. Everything it
cannot prove from the source is reported as `needs_validation` with the blocker written down.
