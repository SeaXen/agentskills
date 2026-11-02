# 2027 Developer Events Plan — €90,000 / 36 travel-days

**Working thesis:** Rust's systems-programming community and your buyer/hire profile are close to the same group — people who build and operate infrastructure. Treat "Rust awareness," "signups," and "senior SRE hires" as three outputs of one audience, not three separate campaigns. That's what makes a single €90k budget coherent instead of split three ways.

**The real constraint isn't the money, it's the 36 person-days.** €90k buys a lot; three engineers × 12 days doesn't. Every allocation below is sized against travel-days first, budget second.

⚠️ **Flag for your boss now, not in December:** "two senior SRE hires" is a fair target for events to *source*, not to *close*. Events build the warm pipeline — talks that establish credibility, meetups where people meet your engineers, a champions program that surfaces names. Someone still has to run interviews and make offers. If no recruiting owner is committed to working that pipeline monthly, set the KPI as "senior hiring conversations opened" and let hiring own the conversion number.

---

## What's already on your desk — verdict on each

| Item | Verdict | Why |
|---|---|---|
| **Ferrous Summit** (big US Rust conf) | Keep, resize | Best single venue for both "Rust awareness" and senior-hire density. But a booth at a mega-conference is noise + audience dilution. Trade the booth for a CFP talk, a lean recruiting presence, and pre-booked 1:1s. |
| **3 regional Rust days (EU)** | Keep, double down | This is your highest-ROI tier. Regional/niche events consistently beat mega-conferences on cost-per-qualified-conversation. Sponsor all three, speak at all three. |
| **2 student hackathons** | Scale down, don't cut | Wrong crowd for "senior SRE hires" and weak for self-serve signups from companies running K8s in prod — but you have two years of relationship equity here. Downgrade to in-kind/light presence rather than walking away. |
| **Berlin meetup (2x sponsored)** | Promote to anchor | This is your only asset that already has a compounding curve. Everything else on this list is a single event; this one is a relationship. Build the year's "lasts" strategy around it. |

---

## Budget allocation (planning estimates — validate against actual quotes before committing)

| Line | Spend | Travel-days | Serves |
|---|---:|---:|---|
| Ferrous Summit — CFP talk, lean sponsorship/recruiting presence (no booth), 2 engineers, pre-booked 1:1s, targeted senior dinner | €20,000 | 10 | Awareness, hiring |
| 3× regional Rust days — sponsor + speak at all three, rotate which engineer attends | €26,000 | 12 | Awareness, signups, hiring |
| Berlin meetup — upgrade to quarterly anchor (co-host, not just sponsor) | €9,000 | 4 | Awareness, signups, hiring (compounding) |
| New second city — pilot 2 meetups in H2, seeded from Berlin playbook | €4,000 | 2 | Awareness (long-lever) |
| 2 student hackathons — in-kind/credits for one, light in-person for the other | €4,000 | 2 | Goodwill only; explicitly not sized for this year's KPIs |
| Rust Champions program — 5–8 engaged community members, early access, 1–2 conference-ticket sponsorships | €5,000 | 0 (piggybacks) | Hiring pipeline, signups (advocates) |
| Content capture & repurposing — recording every talk, cutting clips/posts/quotes all year | €6,000 | 0 | Awareness (durable, compounds, also feeds AI-search citations) |
| Measurement tooling, UTM/attribution setup, swag | €3,000 | 0 | Everything (see below) |
| **Reserve (unallocated, ~14%)** | €13,000 | 6 | Opportunistic CFP acceptances, a regional day that overperforms, an unplanned hiring trip |
| **Total** | **€90,000** | **36** | |

Travel-days land at 30 committed / 6 reserve — don't spend the reserve days on a plan; spend them reacting to what the first two quarters tell you.

---

## The "build something that lasts" mechanism

Don't add a fourth flagship event. Compound the one asset that's already compounding:

1. **Berlin:** go from occasional sponsor to the meetup's anchor partner — recurring speaking slot, food/drinks every quarter, one Halyard engineer hosting each time (rotate people, not the commitment).
2. **Champions program:** pull the 5–8 most engaged Berlin/regional-day regulars into a small private program (early access, one conference ticket sponsored, direct line to engineering). This is your cheapest, most honest hiring pipeline — these are people who already chose you.
3. **Second city, H2 only:** once Berlin's quarterly rhythm is proven (not before), run two pilot meetups in a second city using the same format. If it holds, it's your second anchor for 2028. If it doesn't, you've spent €4k and 2 days finding out, not €20k.

That's the whole "lasts" strategy: one proven format, replicated, rather than a bigger one-off each year.

## What to say no to

- No booth at Ferrous Summit. A talk plus 15–20 pre-booked meetings will out-perform a booth for both awareness and hiring, at a third of the cost.
- No scaling the hackathons up. They're the weakest fit for this year's two goals — resource them to match, not to their historical size.
- No new flagship event in 2027. Prove the two-city meetup model first; a user-conference-scale bet before that is premature.

---

## Measurement — sized for one person

You're the only one tracking this, so the system has to survive being run by one person across ~10 events:

- **One spreadsheet (or one CRM view), one row per event.** Columns: cost, person-days, qualified conversations (not badge scans), meetings booked, "talent-warm" flags with a one-line note, signups attributed within 60 days.
- **One attribution mechanism, reused everywhere:** a single UTM pattern per event + a "how did you hear about us" field at signup. Don't build a bespoke tracking setup per event type.
- **Two KPIs, reviewed quarterly, not per event:** cost per qualified conversation, cost per talent-warm flag. Per-event numbers are noisy; the Berlin meetup and the regional days should be judged on a rolling 2–3 instance trend, not the first outing.
- **Hand off "talent-warm" monthly.** Your job is surfacing the names with context; hiring's job is working the list. Keep that boundary explicit so the SRE-hire KPI doesn't silently become yours alone.

## Rough shape of the year

- **Q1** — Champions program live, Berlin #3, CFPs submitted for Ferrous Summit + all 3 regional days, measurement sheet stood up.
- **Q2** — Regional day #1, Berlin #4 (year's first "anchor" edition), second-city pilot #1.
- **Q3** — Ferrous Summit, regional day #2, Berlin #5, lighter hackathon.
- **Q4** — Regional day #3, Berlin #6 (anchor + champions spotlight), second-city pilot #2, quarterly review feeding 2028 planning.