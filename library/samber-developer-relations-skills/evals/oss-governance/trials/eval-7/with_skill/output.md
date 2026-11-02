# Governance review — Marrowfen

Don't run the constitutional assembly. Fix the moderation/sponsor dispute first, install the cheapest working model in 2–3 weeks, then run a real election on a realistic timeline — not December. Writing a constitution mid-conflict is the failure mode this field has a name for: it relocates the fight instead of ending it, and the reference case (a major project that did this) produced an elected committee *and* two forks in the same year. You already have three competing Matrix rooms — that's the fork-in-progress.

## As-is — who decides today, by what implicit rule, where it has failed

Undocumented, as with almost every project this size. From what triggered the blow-up:

- A moderation decision touching a corporate sponsor was made or contested, with no written rule for who has final say when a sponsor relationship and a moderation call conflict.
- The moderation lead had no protection or clear mandate when that decision was challenged — resigning publicly was the only escalation path available, which is itself the symptom of a missing ladder.
- Two more maintainers quit in solidarity rather than through a review process, meaning the project had no forum where their objection could be raised, decided, and closed.
- Three Matrix rooms now compete for canonical status. No rule says which channel is authoritative, so the community is litigating the meta-question ("where do we even argue this?") instead of the real one.

Failure pattern: no conflict-of-interest rule for sponsor-linked decisions, no moderation-authority rule, no escalation ladder, no communication-channel authority. This is not a "we need a constitution" gap — it's four specific missing rules.

## Concentration — absence factor, employer spread, credential holders

Unknown from what's given. Confirm before picking a model:

1. How many maintainers remain after the three departures, and who among them can merge and who can release?
2. Does the sponsor employ, fund, or otherwise have leverage over any remaining maintainer?
3. Who holds the domain, trademark (if any), package registry account, and Matrix server/room admin rights?
4. Were the mod lead or the two who quit among the top contributors by commit share, or primarily community-facing?
5. Is there any live risk the sponsor relationship itself creates an ongoing conflict of interest (funding tied to moderation outcomes, PR review, roadmap)?

If the three departures leave one person holding merge, release, and domain access, treat that as an absence factor of 1 — every shared model is unadoptable until you recruit or reinstate co-maintainers. Answer #1 before anything else below is final.

## Recommendation — model chosen, alternative considered, monthly hours and what they buy

**Do this now, not in December:** a maintainer council (row 1) — roughly an hour a month, no standing meeting, reversible by one vote — covering exactly two gaps: a deadlock rule and a documented sponsor conflict-of-interest / moderation-authority rule. That's what's actually missing; it is not a constitution-sized problem.

**Consider this for Q1–Q2 2027, not this December:** an elected steering committee. Legitimate reasons to want one exist here — a visible departure and a trust deficit that a self-appointed council can't fully repair. But it costs a quarter to install properly (electorate, eligibility, officers, terms) and is the least reversible model on the table. Installing it inside eight weeks, while three factions are still arguing in three separate rooms, produces the anti-pattern this field already has a name for: a committee elected before there is any history of the project running a vote, whose legitimacy the first contested decision immediately tests and often fails. If maintainers still want December after hearing this trade-off, that's their call — flag the risk, don't block it.

Sequencing, in order:

1. **This week:** publish the two missing rules (sponsor COI, moderation authority) as an interim maintainer-council decision — not a full document, a page.
2. **Weeks 2–3:** pick one canonical Matrix room, state it in writing, and let the other two lapse. Redirect, don't argue them closed.
3. **Weeks 3–6:** run steps 3–4 below properly — decision classes, thresholds, timers, a short GOVERNANCE.md. This is the "repair," not the constitution.
4. **After 6 weeks, if the repair holds:** open the steering-committee design (electorate, eligibility, terms) with a realistic install date — Q1 2027 is defensible, December is not.

## Decision rules — per class: who decides, threshold, timer, escalation

| Class | Who decides | Threshold | Timer | Escalation |
|---|---|---|---|---|
| Routine change | Any maintainer | Lazy consensus | 72h | Council review |
| Breaking change | Council | Consensus-seeking | 1 week | Vote if unresolved |
| New maintainer | Council | Explicit vote | 2 weeks | N/A |
| Removal / emeritus | Council, excluding the person named | Explicit vote | 2 weeks | N/A |
| Scope change | Council | Consensus-seeking + written proposal | 2 weeks | Vote if unresolved |
| Release | Named release maintainer(s) | Existing practice, written down | N/A | Council if disputed |
| **Sponsor / conflict of interest** | Council, sponsor-affiliated maintainer recuses | Explicit vote | 1 week | Named neutral third maintainer casts tie-break |
| **Moderation action** | Named moderation role, not overridable by a single sponsor-linked party | Documented mod policy | 48h response | Council review within 1 week, sponsor has no vote |
| Amendment to this document | Council | Explicit vote | 2 weeks | N/A |

The two bolded rows are the ones this incident was actually missing. Every blocking objection needs a technical or policy reason attached — not a veto by mood — and every row has a clock so no path stalls indefinitely.

## Neutrality — trademark, affiliation ratio, contribution agreement, minutes

Open, pending answers to Concentration Q2–Q3:

- If the sponsor employs or funds any remaining maintainer, disclose it in the document itself, and route sponsor-linked moderation calls through the recusal rule above — stated up front, not revealed after the next dispute.
- Confirm who holds the trademark (if one exists), domain, and Matrix server admin. If it's one person or one company, that's the next thing to fix, independent of which governance model you pick.
- Publish minutes of the council's first few decisions. Given three factions are watching, visible process is the fastest way to rebuild trust — faster than any document.

## GOVERNANCE.md — the document, ready to commit

```markdown
# Marrowfen Governance

## Roles
- Maintainer: merge rights on their area, one vote in council decisions.
- Council: all active maintainers. Meets asynchronously; no standing call required.
- Release maintainer(s): named individuals with publish rights. [names]

## Decision-making
- Routine changes: lazy consensus, 72-hour window, any maintainer may proceed if no objection.
- Contested or breaking changes: consensus-seeking, written proposal, 1-week window, then an
  explicit council vote if unresolved. Objections must state a technical or policy reason.
- New maintainers, removals, scope changes, amendments: explicit council vote, 2-week window.

## Conflicts of interest
Any council member affiliated with a sponsor, employer, or external party with a stake in a
decision recuses from that vote. A named neutral maintainer casts the deciding vote on ties
involving a recusal.

## Moderation
Moderation actions follow the published moderation policy. No single sponsor or external party
may override a moderation decision. Disputed actions go to full council review within one week.

## Official channels
[Matrix room link] is the sole official project space. Other rooms are unofficial and unmoderated
by the project.

## Succession
Maintainers inactive for [90 days, TBD] move to emeritus on request or by council vote. Emeritus
maintainers may return to active status by council vote. [Named end state if the project cannot
continue.]

## Amendments
This document changes only by explicit council vote, 2-week window.

## Review
Reviewed 6 weeks after adoption, then annually, and after any maintainer change.
```

Fill the bracketed items before committing. Cut anything above your maintainers won't actually follow — a rule nobody honors is worse than no rule.

## Enforcement — repo settings and credential changes needed to match it

- Match forge merge/release permissions to the maintainer list above — no gaps between "who governance names" and "who the repo lets merge."
- Pin the GOVERNANCE.md link in the one official Matrix room; do not argue the other two closed, just stop treating them as canonical.
- If the sponsor or any external party currently has any repo, domain, or Matrix admin access beyond what's disclosed above, that's a same-week fix, not a governance-document fix.

## Succession — trust ladder, inactivity rule, emeritus, end state

- Offer the resigned mod lead and the two maintainers a dignified emeritus listing, not silence — this is a goodwill and credibility move, and it costs nothing.
- Leave the door open: emeritus-to-active-again by council vote, stated in the document, in case any of the three want back in once the sponsor question is settled.
- Set an explicit inactivity definition (e.g., 90 days with no review/merge activity) so the next departure doesn't require another public resignation to trigger a role change.
- Recruit at least one more maintainer before doing anything else if Concentration Q1 shows an absence factor of 1 — every model above assumes you're not down to a single person holding the keys.

## Foundation — needed or not, and the gap list if yes

Not triggered by anything in this incident. No mention of the project needing to handle money or an adopter demanding proof of neutrality. Skip step 8 entirely for now; revisit only if a fiscal host or foundation question becomes real on its own.

## Review date

Re-check in 6 weeks: has the interim council rule actually been used once (a sponsor-linked decision or moderation dispute resolved under it)? If yes, that's your evidence base for opening the steering-committee design next quarter. If the 6-week check shows the council rule was never invoked, the dispute may not be resolved yet — don't schedule the election until it is.

**Next action:** get the answers to the five Concentration questions this week — everything downstream depends on absence factor and sponsor affiliation, and neither is guessable from outside.