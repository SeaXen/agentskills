<!-- Absorbed from the sibling skill 'incident-postmortem' (source: incident-postmortem/SKILL.md).
     Kept verbatim so this review skill stays self-contained.
     The sibling skill itself was NOT deleted. -->
---
name: incident-postmortem
description: Site Reliability Engineering (SRE) incident postmortem authoring, root-cause analysis (5 Whys), and timeline reconstruction. Use when documenting production outages, conducting post-incident reviews, analyzing failure modes, or creating corrective preventative action plans.
allowed-tools: Read, Write, Edit, Glob, Grep
version: 1.0
---

# Incident Postmortem & SRE Analysis

> **Blameless Postmortems, Root-Cause Analysis (5 Whys) & System Resiliency**

---

## 🏗️ Core Principles

| Principle | Rule |
|-----------|------|
| **Blameless Culture** | Focus on systemic vulnerabilities and process gaps, never individual human error. Humans make mistakes when systems allow them to. |
| **Chronological Precision** | Reconstruct exact timeline with timestamps (UTC): Detection time, Escalation time, Triage time, Mitigation time, Resolution time. |
| **5 Whys Root-Cause Deep-Dive** | Dig past the immediate trigger (e.g., "bad deploy") to the underlying architectural/process cause (e.g., "why was there no canary?"). |
| **Actionable Preventative Items** | Every action item must have a specific owner, clear priority (`P0`/`P1`), and a tracking issue link. |

---

## 📋 Blameless Postmortem Template

```markdown
# Incident Postmortem: [Incident Title / Outage Summary]

**Date:** YYYY-MM-DD  
**Severity:** SEV-1 / SEV-2  
**Duration:** X hours Y minutes  
**Impact:** Z% of users experienced 500 errors on checkout  
**Author(s):** SRE / Lead Engineer  

---

## 1. Executive Summary
Brief non-technical summary of what broke, customer impact, and how it was resolved.

## 2. Impact Metrics
- **User Impact:** ~14,000 affected requests
- **Financial/SLA Impact:** SLA breach (<99.9% uptime for month)
- **Time to Detect (TTD):** 4 minutes
- **Time to Mitigate (TTM):** 18 minutes

## 3. Timeline (All times in UTC)
- `14:02` - Automated deployment `v2.4.1` initiates.
- `14:05` - CloudWatch alerts fire: 5xx error rate spikes above 5%.
- `14:08` - On-call engineer acknowledges pager and initiates incident bridge.
- `14:15` - Root cause identified as unindexed DB query causing connection pool exhaustion.
- `14:20` - Rollback to `v2.4.0` completes. Error rate returns to baseline 0.01%.

## 4. Root Cause Analysis (5 Whys)
1. **Why did the service fail?** Database connections were exhausted.
2. **Why were connections exhausted?** A new query on the user table took 4.2s per request instead of 2ms.
3. **Why did the query take 4.2s?** The query was missing an index on `tenant_id`.
4. **Why was the index missing?** The migration was omitted from the release branch.
5. **Why was the migration omission not caught before prod?** Staging environment had mock data too small to reveal missing index latency, and CI lacked an automated EXPLAIN query check.

## 5. Action Items
| Action Item | Type | Owner | Priority |
|---|---|---|---|
| Add CI check running EXPLAIN on newly added Prisma queries | Preventative | Data Team | P0 |
| Configure RDS connection pooler with query timeout limits | Mitigation | DevOps | P1 |
| Seed staging database with realistic dataset scale | Process | QA Team | P2 |
```

---

## ❌ Anti-Patterns

- ❌ Assigning blame to specific developers ("Alice committed a bad line").
- ❌ Stopping at the superficial symptom ("the server ran out of memory") without answering why.
- ❌ Failing to track preventative action items to completion after publishing the postmortem.
