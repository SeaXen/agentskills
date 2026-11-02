# Kestrel Logic — Developer Program: Where to Start

**Short answer: fix the measurement foundation first, answer finance in parallel with an honest bounded number, audit Discord right behind it, then use all three as the first populated edition of the CTO's quarterly report.** The four items aren't independent — three of them are inputs to the fourth. Building the reporting framework before fixing UTMs just bakes bad numbers into a recurring document.

## Sequencing and why

| Order | Task | Why here | Effort |
|---|---|---|---|
| 🔴 1 | UTM taxonomy + "source of truth" ruling | Cheapest fix, unblocks everything downstream — booth ROI and the CTO framework both need trustworthy tagging | 2-3 days |
| 🔴 2 | Booth ROI reconstruction | Finance is waiting; doesn't need step 1 finished since March's data is already whatever it already is | 3-5 days, parallel with step 1 |
| 🟠 3 | Discord health audit | No external deadline; needs a bot/API pull, not a fix | 3-5 days |
| 🟢 4 | CTO quarterly framework | Draft *after* 1-3 so it can cite real definitions instead of promising them | 1-2 weeks |

Run 1 and 2 the same week. Run 3 right behind. Draft 4 last — it's the only one of the four that should take real time, because it's the thing that outlives this particular fire drill.

---

## 1. Why GitHub Traffic and your analytics tool will never agree

Stop trying to reconcile them line by line — they're structurally incompatible, not misconfigured:

- **GitHub's Traffic panel doesn't read UTM parameters at all.** It logs pageviews server-side before your query string ever reaches JS-based analytics logic; `?utm_source=x` is invisible to it by design, not by bug.
- It's a **14-day rolling window** with no historical export, referrers and paths **capped to the top 14**, and visitor counts are an **anonymized approximation** (GitHub says so in its own docs) — not a session-based count like GA4/PostHog/Plausible produce.
- Bot filtering differs: GitHub counts server-side (some bots included), your JS analytics tool counts client-side (bots that don't execute JS are invisible). Neither is "wrong" — they're measuring different things.

**Decision, not a fix:** declare your analytics tool the canonical source for anything involving UTM attribution, funnels, or revenue linkage. Demote GitHub Traffic to a qualitative signal — trend direction and top-referrer names only, never a number you defend in a meeting. Write this down once, in the doc that becomes the source-list row of the CTO report, so it stops being re-litigated monthly.

**UTM hygiene, the actual mess to clean:**
- Fixed taxonomy, three lists, documented once: `utm_source` (github, discord, devrelcon, newsletter, x, linkedin, hn, reddit, docs, partner-name…), `utm_medium` (organic, social, community, email, event, referral, sponsorship, cpc), `utm_campaign` (one per initiative — `devrelcon-2026-booth`, `q3-docs-relaunch`).
- Audit every untagged or inconsistently-tagged surface: README badges, docs nav links, Discord welcome message, email signatures, conference landing pages/slides/badges, social bios, org profile. A lot of the "every number disagrees" feeling is just years of hand-typed, inconsistent params polluting the analytics tool's own reports — that's fixable even where GitHub-vs-analytics never will be.
- One canonical UTM builder (a shared sheet or link-shortener with enforced fields) so nobody free-types a param again.

---

## 2. Is the Discord actually dead?

2,100 members tells you nothing — it's a roster count, not a pulse. Here's what actually answers the question, and the thresholds to judge it against:

| Metric | Healthy | Warning | Action needed |
|---|---|---|---|
| Weekly unique posters (not just online) | — | — | Compute this first; there's no universal target, only a trend and a % of 2,100 |
| Response time to an unanswered question | <24h | 24-72h | >72h |
| Unanswered-question rate | <10% | 10-25% | >25% |
| New-member 7-day retention (posted at least once) | >40% | 20-40% | <20% |
| Monthly active ratio (posted at least once / total members) | >20% | 10-20% | <10% |
| Staff-message share of total messages | <30% | 30-50% | >50% — if staff are answering their own prompts, it's dead in the way that matters |

**How to get the numbers:** Discord's UI doesn't expose this at 2,100-member scale. Either turn on Server Insights (requires Community-server verification) or run a bot/API pull (Statbot, Commonroom, or a script against the Discord API) for the last 90 days: unique posters/week, messages/week by channel, and the "ever posted a single message" ratio across the full 2,100.

**Calibrate expectations before panicking:** niche infrastructure/dev-tool Discords routinely run 3-8% ever-active. An embedded database is a deep-niche, high-expertise audience — a small, sharp core answering real questions can look "quiet" next to a 50k-member framework server and still be doing its job. The number that matters is weekly unique posters and time-to-first-response, not the size of the roster.

**Likely pattern to verify, not assume:** activity concentrated in #help/#general, most other channels silent, staff carrying most of the answering. If confirmed, that's a missing *program* (no office hours, no recognition, no scheduled prompts), not proof the platform or product failed. Fix with the cheap levers first — weekly office hours, a show-and-tell channel, a "contributor of the month" callout — before concluding anything structural.

**Deliverable:** a 90-day scorecard against the table above, ending in one verdict: dead / quiet-but-normal-for-this-niche / needs-a-program. Also prune obviously-dead channels — a wall of silent channels reads as more dead than a handful of active ones.

---

## 3. What did the $40K DevRelCon booth return?

Tell finance the honest version up front: **precise ROI needs instrumentation that, per the UTM mess above, almost certainly wasn't in place in March.** A fabricated precise number is worse than a defensible range — it invites a harder question later when someone checks the math.

**Reconstruction, using whatever exists:**
- Any booth-specific UTM/QR/landing page → pull its tagged conversions directly from the analytics tool.
- Lead list or badge scans from the booth → cross-reference against the CRM for opportunities created in the 90-180 days after, tagged **event-influenced**, not event-sourced (a booth conversation that closed six touches later doesn't get 100% last-click credit — that's the same over-crediting trap ad platforms fall into).
- Referral/direct traffic and branded search volume (Search Console) for the event week vs. a trailing 4-week baseline — a brand-lift proxy, not a conversion count.
- GitHub star/clone delta for the event week vs. baseline — weak but real for a dev-tool booth specifically.
- Any "how did you hear about us" field mentioning DevRelCon in the following quarter's signups/demo requests.

**How to present it to finance:** a range with a confidence label, not a single figure — "$40K produced $X in tagged conversions (high confidence), $Y-$Z in plausibly-influenced pipeline (low confidence, wide range), plus N qualified conversations if a lead list survives." Then pivot the conversation to what matters more than March: **the go/no-go bar for the next booth**, and the instrumentation (dedicated UTM + QR landing page, tracked lead capture, CRM source tag, cost-per-qualified-meeting benchmark against your other channels) that makes this a five-minute pull next time instead of a forensic reconstruction.

---

## 4. What the developer program reports to the CTO every quarter

This is the keystone — build it last, populate its first edition with the corrected definitions from 1-3.

| Stage | Metric | Source (canonical) | Confidence |
|---|---|---|---|
| Awareness | Docs/site session trend + branded search volume | Analytics tool + Search Console | Verified |
| Awareness | GitHub stars/clones (trend line only) | GitHub API | Directional — never a target |
| Onboarding | Time to first successful embedded write/query | Product telemetry (consented) | Verified |
| Integration | % of trials reaching a defined production-shaped usage pattern | Product telemetry | Verified |
| Community | Weekly unique Discord posters + median response time | Discord API/bot export | Verified |
| Advocacy | External talks/posts/non-employee PRs (count + 2-3 named examples) | Manual log / mention monitoring | Directional |
| Pipeline influence | Self-reported source + event/community CRM tags, reported as *influenced* | CRM + self-reported field | Self-reported — triangulation only |
| Spend efficiency | Cost per qualified signal, by channel | Finance + tagged CRM | Only trustworthy once step 1 is live |

Rules for the document itself:
- **One page.** If a ninth row is needed, cut one first.
- Every row carries its **source system and confidence label** (verified / directional / self-reported) — that's what lets the CTO know which numbers to make a call on and which are texture.
- Report **trend across 3+ quarters**, never a single point-in-time figure. One good or bad quarter is noise on a program this size.
- Explicitly note **GitHub Traffic vs. analytics-tool reconciliation is retired** — it's documented as structurally unreconcilable, not a live question.
- Member counts, raw download counts, and any other roster-style number are **excluded on purpose** — they're the exact vanity metrics this framework replaces.

---

**Net for the next two weeks:** ship the UTM taxonomy and source-of-truth ruling this week, hand finance a bounded booth-ROI range with next-time instrumentation attached, run the Discord scorecard right behind it, and only then sit down with the CTO's framework — so it's the first document in this company that reports real numbers instead of promising to.