## Why the current model is failing

Four separate problems are stacked here, and re-weighting alone won't fix them:

- **No fit dimension.** Every point comes from behavior (visits, opens, signup). A score of 60 tells you someone was *active*, not that they're a buyer. A student, a competitor's engineer, or someone building a demo could all cross 60 purely on curiosity.
- **Email "opens" are not a real signal anymore.** Apple Mail Privacy Protection (iOS 15+, since 2021) pre-fetches every image in an email the moment it's delivered, so Apple Mail users show as "opened" whether a human ever looked at it or not. A large share of your 5-point "opens" are Apple's servers, not people. This alone can be inflating scores across your whole base.
- **No decay.** Points from three months ago count exactly the same as points from three hours ago. Someone who skimmed docs in June and opened two newsletters since is treated identically to someone actively evaluating you this week.
- **Scoring and routing both operate at the contact level, not the account level.** This is exactly what produced the bank incident: 40 individual employees each independently crossed 60 points, each fired an independent SDR trigger, and 40 near-identical cold emails landed inside one company. Nothing in the model recognizes "these 40 people work at the same place" as a single event — in fact it's your *best* signal (organic multi-seat adoption inside one account) and you turned it into spam.

The 2% reply rate and the Twitter complaints are the visible symptom of all four combined: low-intent people crossing threshold, stale signals counted as fresh, and duplicate outreach hitting the same company repeatedly.

---

## Redesigned model

### Step 1 — Fit gate (new, runs before any engagement scoring)

A lead can only enter the engagement-scoring pipeline if it passes this gate. This is the single highest-leverage fix — it stops non-ICP traffic from ever reaching the SDR queue, regardless of how much they click around.

| Signal | Rule |
|---|---|
| Email domain | Personal domains (gmail/yahoo/outlook.com/etc.) → **hard block**, never enters SDR queue |
| Email domain | Known competitor domains → **hard block** |
| Company size (via domain enrichment — Clearbit/Apollo) | Below your minimum ICP size (e.g. <5 employees, adjust to your actual ICP) → **does not gate SDR queue automatically**, routes to self-serve nurture instead |
| Role signal (from signup form or enrichment) | Engineering/DevOps/technical title → pass; non-technical/unknown → pass but flagged lower priority |

Everything below only applies to leads that pass this gate.

### Step 2 — Engagement score (revised weights)

| Signal | Old | New | Why |
|---|---|---|---|
| Pricing page visit | 10 | 8, **capped at 16 pts / rolling 7 days** | Prevents "visited pricing 6 times" alone from hitting threshold — that's browsing, not intent |
| Docs visit (generic page) | 8 | 3 | Was overweighted; most docs traffic is pre-purchase research or existing free-tier users |
| Docs visit — high-intent pages (SSO/SAML, API keys, migration guide, enterprise docs) | n/a | 10 | New tier — these pages are visited by people actually implementing, not browsing |
| Marketing email **open** | 5 | **0 — remove entirely** | Unreliable per MPP issue above; don't score it at all |
| Marketing email **click-through to site** | n/a | 4 | Requires a deliberate action; use this instead of opens |
| Signed up (self-serve account created) | 15 | 15 (unchanged) | This one was already reasonable |
| Created first feature flag | n/a | 20 | Real product usage — much stronger signal than any marketing touch for a dev tool |
| Invited a teammate | n/a | 25 | Strongest available signal — indicates team-level adoption intent |
| Connected an SDK/integration outside sandbox | n/a | 20 | Real implementation effort, hard to fake |
| 2nd+ signup from same email domain within 14 days | n/a | +10 per additional signup, rolled up to the **account**, capped at +40 | Turns the bank scenario into a *positive* high-priority signal instead of 40 duplicate triggers |

**Decay:** apply a 14-day half-life to the engagement score — multiply by 0.5 every 14 days since the last qualifying activity. A score built from stale activity should fade, not sit at peak value indefinitely.

**Score gaming guard:** require at least 2 distinct signal types (not just repeated instances of one) within the trailing 14 days before a score counts toward threshold. Stops "6 pricing visits and nothing else" from qualifying.

### Step 3 — Threshold

- Raise the SDR-queue threshold from 60 to **75** on the new point scale, since product-usage signals (worth 20-25 each) now carry real weight and marketing-only activity tops out lower than before.
- Require the fit gate to have passed *and* the 2-distinct-signal-type guard *and* the recency requirement (activity within the last 14 days, post-decay) — not score alone.

---

## Routing fix (this directly prevents the bank incident from repeating)

1. **Score and route at the account level** (company domain), not the contact level. One account = one score, one queue entry, aggregated across every contact at that domain.
2. **One active SDR thread per account.** Once an account enters the queue, suppress new auto-triggers from that domain for 30 days. Additional signups get appended as context to the existing CRM record/task, not a new outbound send.
3. **When multiple people sign up from the same domain, treat it as a priority escalation, not N separate leads.** Route to the single most senior/relevant contact (highest title match, or first signup), and have the SDR reference the team-level pattern ("noticed a few people from your team signed up") rather than sending each person an isolated cold email.
4. **Add a fallback owner** for accounts that pass the fit gate but never cross engagement threshold — route to nurture, not silence.

---

## A note on the 2% reply rate specifically

Even with perfect routing, template copy that says "I noticed you looked at our pricing page" reads as surveillance to developers — this audience is unusually sensitive to being visibly tracked, which likely explains the Twitter complaints as much as volume did. Once product-usage signals (flag created, teammate invited, SDK connected) are driving outreach instead of page-view tracking, have SDRs reference the *usage* action, not the *browsing* action — "saw you got your first flag live" lands very differently than "saw you checked pricing." Worth a copy pass alongside the model change; the routing fix alone won't fully solve the reply-rate problem if the messaging still reads as creepy.

---

## Rollout plan

1. **Backtest before launching:** pull your last 20-30 closed-won accounts and run their historical activity through the new model. Confirm it would have flagged them, and check what score/timing they'd have hit — this calibrates whether 75 is the right cutoff before you commit to it live.
2. **Ship the account-level dedup and the fit gate first** — these are the two changes with zero downside and they stop the active bleeding (duplicate emails, non-ICP leads) immediately.
3. **Ship the new point weights and decay second**, once the backtest confirms the threshold.
4. **Recalibrate monthly for the first quarter**, then move to quarterly once reply rate and SQL-acceptance rate stabilize.
5. **Track two numbers going forward, not just volume:** reply rate (target: meaningfully above 2%, most PLG dev-tool benchmarks run 8-15% for well-targeted outreach) and MQL-to-SQL acceptance rate from the SDR's own judgment — if SDRs start rejecting queue entries as bad fits again, the fit gate needs tightening.

### What would sharpen this further
I don't have your actual closed-won data, CRM/enrichment stack, or current ICP definition (company size band, target roles) — those would let me set the fit-gate thresholds precisely instead of the placeholder numbers above. If you can pull 20-30 closed-won accounts' historical activity, I can help backtest the exact threshold instead of estimating it.