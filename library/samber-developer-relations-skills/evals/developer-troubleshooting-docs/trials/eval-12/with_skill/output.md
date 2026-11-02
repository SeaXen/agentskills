Zendesk assumption: wrong. Knowledge in Agent Workspace creates a blank help-center draft linked to the ticket being worked. No auto-fill from ticket text, no clustering by root cause. Budget transcription time yourself, and cluster first — every major helpdesk (Zendesk, Dynamics, Freshdesk, Salesforce, Oracle) skips root-cause clustering, so the button alone produces one page per ticket, not one page per failure.

Four frameworks anchor what follows, so this is method, not taste: **KCS** (Consortium for Service Innovation) for the operating model, **OASIS DITA** `<troubleshooting>` topic type for entry structure, **Nielsen heuristic 9** for writing bar, **Google SRE** postmortem practice for the document-vs-fix gate.

## Why it resets every 6 months

Sprint model writes in a batch, after the fact, disconnected from ticket work. Root cause per KCS: capture has to happen *during* resolution, while the error text and environment are still in front of the resolver — reconstructed-from-memory entries are the ones that go stale first. No ownership stamp, no maintenance trigger, no re-clustering pass means drift is invisible until someone notices six months later. Also check: did the old 20 pages get last-verified dates and owners? Pages nobody can tell are stale don't get fixed, they get abandoned.

## Who writes what

- **Support (12), KCS Contributor role**: raw draft at ticket-close time only — error text, environment, cause, resolution steps. Not prose, not final copy. Add a required Zendesk ticket-close field for this; that's the actual fix for "the button doesn't do it for us."
- **You, Coach + Publisher role**: weekly triage, clustering, editing to structure, verification, publishing, findability wiring.
- **Engineering**: not ongoing docs work. Only error-string wording changes (when the message itself is the defect) and, conditionally, one small one-off task — see "One ask for engineering" below.
- Staffing check: KCS's own published ratio (v6 Practices Guide, Technique 7.1) is 1 coach to 5–8 contributors at start-up, loosening to ~1:50 mature. You're 1:12. You will bottleneck on editing before you bottleneck on drafts. Fix: train 2–3 senior support agents to Contributor-plus level so their drafts ship with light review, not full rewrite. That's your real capacity lever, not more writing hours.

## Cadence — this is the part that makes it stick

1. **Continuous**: agent fills the capture field on ticket close, for repeat-looking failures only.
2. **Weekly (~3 hrs, you)**: export tickets with the field filled, run `scripts/error-cluster.py tickets.csv --min-count 3`, triage new/growing clusters.
3. **Monthly (~1 hr, you + one support lead)**: agree ranked queue, confirm document-vs-escalate routing, assign a verifier per new entry.
4. **Per release (owner = whoever shipped it)**: update or retire any entry whose error text or cause changed.
5. **Quarterly (~half day, you)**: re-run clustering, diff against last quarter. Same clusters reappearing unchanged = discoverability problem (fix findability wiring), not a "write more" problem.

Store the agreed cluster ranking, coverage target, and routed-away clusters somewhere durable. Re-deriving them from scratch each cycle is exactly where this kind of work dies.

## Ranking, once you have real data

Rank by reader-hours unblocked per hour of writing, not raw frequency. Promotes: frequent+reproducible (afternoon each, empties queue fastest), first-use blockers (promote even if rare — the reader abandons before filing the ticket that would rank it). Demotes: rare-expensive stuff nobody can reproduce cheaply. Delete outright — don't queue — anything a reader can't act on alone, or that next release removes anyway.

## Protect your one writer: don't document a defect

Escalate instead of writing a page when any of these hold (cap your queue with this gate, it's what keeps 1 writer from drowning):

- error text itself doesn't say what to do → fix the message, not the docs
- fix is "edit three config files in order" → product/DX change
- cause is account state (quota, plan, suspension) → support macro, not a public page
- spike right after a release, single version → regression, file it, don't document it into permanence
- same failure class across several postmortems → scheduled product fix; a page here is Google SRE's "mitigative, not preventative" trap

## Zendesk workflow, mapped to what it actually does

Use "Convert to article" only as the last step (publish), never the first (capture). Capture happens in the ticket-close field above. Cluster with the script before anyone opens the Knowledge editor. If Zendesk help-center search logs are reachable, add zero-result queries as a second signal source alongside tickets — that's where silent abandonment shows up, tickets alone won't catch it.

## Targets

Self-set baseline, not a published number — negotiate down given your 1:12 ratio: 80% of top-20 clusters is the skill's baseline for a healthy team; you may want top-10-to-15 for cycle one. Track cluster coverage, ticket volume per covered error (fixed windows, before/after), zero-result searches for covered strings, entries touched since last release. Skip site-wide "deflection rate" — unmeasurable; per-error ticket volume is.

Set expectations against Gartner (Dec 2023, n=5,728): only 14% of support issues fully self-resolve, 36% even for "very simple" ones. "Zero tickets" isn't a real target. If engineering pushback needs a sourced argument: Dixon/Freeman/Toman (HBR 2010 / *Effortless Experience*) — 96% of customers hit with a high-effort support interaction become more disloyal, vs 9% for low-effort. Refuse the "$15–50 per ticket" figure going around — no traceable methodology; use Fenwick's own ticket cost or say it's unknown.

## One ask for engineering

Keep it to one ticket, ~1 day of their time: wire the entry URL into wherever the error surfaces (error payload field, or a doc link in the CLI/API response). That's the cheapest lever — it's literally how the reader finds the page. Only pitch the generated-catalog task (one source file feeding both the error-code constant and the doc table, à la Stripe/PostgreSQL/Rust) if you can first show the diff between documented codes and what the product actually emits — that diff is the business case, don't ask without it.

## Confirm before running this for real

- Does the product emit stable error identifiers, or free text only? Changes whether pages are per-code or per-symptom.
- Is there an error telemetry source, or is Zendesk your only signal? You need one reported + one unreported source; tickets alone hide silent failures.
- Does an AI assistant answer from your help center already? If yes, add re-index-on-change to the release trigger above.

**Next action, 10 minutes**: add the capture field (error text / environment / cause / resolution) to your Zendesk ticket-close form. That single change is what breaks the sprint-and-reset cycle.