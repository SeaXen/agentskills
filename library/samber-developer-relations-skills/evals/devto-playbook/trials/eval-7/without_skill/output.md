**Next action:** send the CMO the 3-line pitch in section 1 today, then book 30 minutes with your data architect SME (section 7).

Status: plan done, three inputs missing (section 8). Reading time about 6 minutes.

## 1. Verdict and CMO pitch

**Recommendation: do not run 3 posts/week. Run 1 deep post/week for 10 weeks, gated, starting Mon 2026-11-16.**

Pitch to CMO:
- Dev.to readers are developers. Your buyers (CISOs, data architects) are on dev.to only partly. Data architects yes, CISOs rarely.
- 3 posts/week needs about 45 writer-hours/week. You have one marketer, so the quality would be generic.
- We will test the channel with 1 post/week, aimed at bank data architects (the champion who recommends a $220k tool). A week-12 gate decides scale-up.

What the competitor example likely misses: they probably have a free tier or open-source project. Dev.to posts there end with "try it". Yours cannot. The plan replaces that with a public companion repo (section 5).

## 2. Options ranked

| Option | Cadence | Cost | Fails when |
|---|---|---|---|
| A. Pilot (recommend) | 1 post/wk, 10 weeks | about 40% of one marketer + 2.5 reviewer-hours/post | Gate shows no bank-account signal |
| B. Boosted | 2/wk | A + freelance technical writer, 8-9 week lead time to ramp | SME review becomes the bottleneck |
| C. CMO ask | 3/wk | About 3 FTE-equivalents or agency, plus 8+ SME-hours/wk | Quality drops to listicles; bank readers ignore it |

Capacity estimate per post, in passes (my assumptions; replace with your real last-quarter numbers): research 2h, draft 6h, code/diagram 3h, publish and replies 2h, so 13h writer. Plus one SME technical pass (1.5h) and one compliance/legal pass (1h). 3/wk = 39h writer alone, with zero time for anything else.

## 3. Audience and pillars

Primary reader: data architect at a bank (champion). Secondary: CISO, reached through LinkedIn repurposing, not dev.to.

Mix: 100% searchable or practitioner-useful. No product announcements in the pilot (cap: 0 promo posts; product mention limited to a 2-line footer).

| Pillar | Reader question it answers |
|---|---|
| P1 Lineage and classification in regulated stacks | "How do I trace a field from core banking to a regulatory report?" |
| P2 Governance as code (policy, access, CI checks) | "How do I enforce data policy in pipelines, not spreadsheets?" |
| P3 Audit and evidence | "How do I prove who accessed what, to an auditor?" |

## 4. Calendar (publish Tue; prep starts Mon 2026-11-02)

Weeks of 2026-11-02 and 11-09: build a backlog of 4 finished posts before publishing anything. Slack week: 2026-12-21 and 12-28 (holiday pause, no publishing). Gate review: Mon 2027-02-08.

| Pub week | Working title | Pillar | Shelf life | Owner | Reviewers | Evidence/hypothesis |
|---|---|---|---|---|---|---|
| 11-17 | Tracing one column from core banking to a regulatory report | P1 | evergreen | Content marketer | SME + legal | Hypothesis: lineage is the top architect pain; check sales call notes |
| 11-24 | Classifying PII across 40 schemas without a spreadsheet | P1 | evergreen | Content marketer | SME + legal | Support/sales questions on classification |
| 12-01 | Data access policy as code: a worked example | P2 | evergreen | Content marketer | SME + legal | Companion repo launch |
| 12-08 | Why data catalogs go stale, and a fix that survives reorgs | P1 | evergreen | Content marketer | SME + legal | Objection from sales calls (confirm) |
| 12-15 | Evidence an auditor will accept: access logs done right | P3 | evergreen | Content marketer | SME + legal | Hypothesis: CISO interest, tests LinkedIn spillover |
| 01-05 | Governance checks in CI: failing a build on a policy break | P2 | evergreen | Content marketer | SME + legal | Repo extends post 12-01 |
| 01-12 | Lineage across batch and streaming: where it breaks | P1 | evergreen | Content marketer | SME + legal | Comments from 11-17 post |
| 01-19 | Reading a regulation as a data architect (DORA, BCBS 239) | P3 | refresh yearly | Content marketer | SME + legal | Verify every regulatory claim against the primary text |
| 01-26 | What we learned from the first 7 posts' comments | P1-P3 | timely | Content marketer | SME | Reader questions mined into next slots |
| 02-02 | Open-sourcing the policy library (or "Policy examples, v1") | P2 | evergreen | Content marketer | SME + legal | Only if repo is approved (section 8) |

Replace the "Reviewers" roles with real names before 11-02. A slot without a named reviewer does not ship.

## 5. Replace the missing free tier

Without a "try it" button, each post needs one low-friction next step:

1. Companion public GitHub repo: sample dataset, sample policies, a lineage diagram template. No customer data, no internal paths.
2. Footer link to a "talk to an architect" page, not a sales demo form.
3. Canonical URL on your own blog (set `canonical_url` in dev.to front matter) so search authority accrues to your domain. Publish from an organization account on dev.to.

## 6. Repurposing (each is its own slot, same week)

- LinkedIn post for CISOs (same insight, risk framing): Wed.
- One-paragraph note to account executives with the post link for named bank accounts: Thu.
- Month 2 onward: bundle 4 posts into one PDF guide behind a form (first owned-audience asset).

Workload with repurposing: about 16h writer/week, which is 40% of one person. The remaining 60% stays as slack for reactive work and replies.

## 7. Review ritual and guardrails

- SME (data architect): 30-minute kickoff Mon 11-02, then one pass per post, 48h turnaround.
- Legal/compliance: one pass per post, 48h SLA.
- Banned from every post: customer names, unannounced features, pricing, internal hostnames or paths, anything from an NDA.
- Monthly plan review (Dec 14, Jan 11, Feb 8): published vs slotted, topics earning replies, kill/defer decisions.
- Reply to every dev.to comment within 24h. Answers come from the SME, not generic text.

## 8. Metrics and gate (Mon 2027-02-08)

Do not judge on views. At $220k ACV and an enterprise bank cycle, closed revenue will not show by February.

Leading metrics:
- Publish rate (target 80% or more: 8 of 10 shipped).
- Named-account signal: contacts with data-architect or CISO titles at banks on your ICP list who comment, reply, connect on LinkedIn citing the post, or request a call.
- Companion repo stars/forks from bank-domain accounts.
- Demo-request free-text "how did you hear" mentioning dev.to or a post.

Proposed gate (adjust to your sales reality):
- **Continue/scale to 2/wk:** at least 3 named-account signals from 10 posts, AND publish rate at least 80%.
- **Redirect:** zero named-account signals. Move the effort to LinkedIn, industry newsletters, or conference talks where bank buyers sit.
- Influenced-pipeline rule: count a deal only if a named contact engaged before the opportunity opened (365-day lookback). No retrofitting.

## 9. Decisions I need from you

1. CMO accepts the 1/wk pilot? If no, which option B/C and who funds the writer?
2. Names for the SME reviewer and the legal/compliance reviewer.
3. Can you publish a public GitHub repo (sample policies only)? If no, drop post 02-02 and the CTAs fall back to the "talk to an architect" page.

**Next:** send the pitch (section 1) to the CMO, then reply to me with answers to the three questions above.