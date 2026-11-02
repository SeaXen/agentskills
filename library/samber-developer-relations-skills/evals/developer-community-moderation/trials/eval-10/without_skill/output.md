## Page structure

Add "Community" section to docs.sablewick.dev, 4 pages under one hub, 3 levels deep, matching doc-site pattern:

```
Community (/community)
├── Code of Conduct (/community/code-of-conduct)      — behavior standard, values
├── Report a Concern (/community/report)              — how to report, channels, what happens after, no-retaliation promise
├── Conduct Process (/community/conduct-process)      — who decides, principles, timeline, outcomes, appeals
└── Data & Retention (/community/data-retention)      — what's collected, how long kept, who can access, rights
```

Nav: put "Community" in header/sidebar next to Docs/Guides, 4-7 items max rule respected. Each child page ≤2 clicks from home. Full 9-page internal doc stays in private handbook (wiki, internal repo, Notion — wherever team already keeps ops docs), never mirrored in full on public site. Public pages summarize; private doc stays source of truth for the team running process.

Breadcrumb: `Home > Community > Report a Concern`.

## Core rule for what to cut

Publish what reporter needs to trust process. Cut what lets bad actor game it, lets committee member's personal life leak, or turns policy into legal liability. Below: verdict per section of your 9 pages.

## Cut checklist, before publish

1. **Intake steps** — publish narrative only ("what happens after you report": ack timeline, who reviews, confidentiality). Cut exact triage checklist and thresholds. Reason: exact thresholds become playbook — bad actor crafts report to dodge scrutiny, or crafts misconduct to stay under stated line.

2. **Recusal** — publish rule only ("member recuses on conflict of interest, e.g. personal/professional relationship to either party"). Cut any mapping of named committee member to specific conflict. Reason: that's a personal-life leak about your own people, not transparency about process.

3. **Decision rule** — publish standard in plain terms ("credible, corroborated reports lead to action; committee decides by [majority/consensus]"). Cut exact scoring formulas, vote counts, numeric severity thresholds. Reason: exact numbers let abuser calibrate right up to the line, and let brigaders learn exact report count needed to trigger action against innocent target.

4. **Exact templates** — highest risk, redact hardest.
   - Cut internal tool names, ticket-ID formats, log/evidence-source names (e.g. "pull DM history from Slack admin logs"). Reason: reveals evidence method, teaches evasion.
   - Cut any real case quote or example tied to past incident, even edited. Reason: small community, re-identification risk stays high no matter how much you trim.
   - Publish generic version only: plain-language description of what reporter and accused each receive, tone and reassurance kept, operational detail stripped.

5. **Retention window** — safe to publish exact period (e.g. "case files kept 18 months, then deleted"). Builds trust, common practice. But cut storage location, backup system, access-control detail. Reason: that's attack-surface map for legal fishing or breach, adds nothing for reporter trust. Flag to legal: once published, this becomes commitment you must actually follow — mismatch between stated and real retention is worse than not stating a period.

6. **Named contacts** — publish roles ("Sablewick Conduct Committee"), not personal emails or direct lines beyond one official report channel. Reason: named individuals become harassment targets themselves.

7. **Liability hedge** — add one line team hasn't written yet: "steps may adapt for safety, legal, or complexity reasons." Reason: without it, any real-world deviation (real cases are messy) becomes evidence you broke your own published policy — used against you in dispute or PR crisis.

8. **Timeline commitments** — soften hard SLAs to targets ("we aim to acknowledge within 48 hours") unless team is fully confident it always hits them. Missed stated deadline damages trust more than no deadline stated.

## Bottom line

"Total transparency" theory is right for: what happens when you report, who decides, appeals path, retention period, confidentiality promise. Wrong for: exact thresholds, exact templates, exact recusal mapping, storage/system detail. Those aren't secrecy for its own sake — they're the parts that, once public, get reverse-engineered by exactly the people the process exists to stop.

Next: send this cut list to whoever wrote the 9 pages, have them mark each section keep/generalize/cut against the 8 items above, then I draft the 4 public pages from what survives.