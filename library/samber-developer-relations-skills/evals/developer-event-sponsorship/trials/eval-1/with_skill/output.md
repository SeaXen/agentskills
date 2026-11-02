# Halyard Systems — 2027 developer-event sponsorship plan

**Recommended shape: Ecosystem-anchored, inside Rust, with Ferrous Summit as the flagship node.** Every candidate event already on your desk sits inside one community, so the ecosystem-anchored shape doesn't compete with flagship-led here — it absorbs it. Build the demo, staff brief and follow-up motion once, reuse at every event, and let recognition compound the way your boss asked for.

Two structural facts drove every choice below, and I want them stated up front because they override the generic defaults:

- **You are the only person who touches event measurement.** The skill this plan follows is explicit: delete the farm-team shape (hackathons + a practitioner conference) whenever one person owns measurement, because two objectives on one owner produce one metric and a lot of excuses. That's why both hackathons are declined below, not just deprioritized.
- **"Two senior SRE hires" and "student hackathons" don't overlap.** Hackathons are the right venue for junior/new-grad recruiting pipelines. Senior SREs are in the room at Ferrous Summit and the regional Rust days — that's where the recruiting objective actually rides.

## Objective, set per event

Halyard sells both self-serve (EUR 49/mo) and enterprise — a mixed-motion company. The skill's rule for that case: set the objective per event, not one primary for the whole year.

| Event | Primary objective | Why |
|---|---|---|
| Ferrous Summit | **Awareness** | Largest audience, first contact with Rust engineers who don't know Halyard yet — the direct match for "awareness in the Rust community." |
| Regional Rust Days (×2 committed) | **Adoption** | Self-serve product behaves like consumer marketing here: event-specific signup URL + promo credit, measured as activations still live at 30/60/90 days — the direct match for "more signups." |
| Berlin meetup (continuing) | **Adoption**, low-cost | Two prior editions = an audience that already half-knows you. Cheapest channel on the list; keep it running. |

**Recruiting rides all three as a secondary lane, not a fourth objective.** Every booth conversation gets logged once, on one sheet, with a routing column — a "candidate" conversation routes to Recruiting exactly like a "bug" routes to Engineering. No second measurement system, no second owner. Set expectations correctly with your boss: the event-level metric is *candidates entering the hiring funnel*, not hires — the two hires are a downstream outcome of your hiring process, not something a sponsorship can promise on its own.

## Three portfolios considered

**A — Ecosystem-anchored (recommended).** Ferrous Summit + 2 regional Rust days + continued Berlin meetup. Hackathons declined. One demo, one staff brief, one follow-up motion, reused four times. Fails geographic reach beyond Rust — accepted, because Rust *is* the mandate.

**B — Flagship-led only.** Ferrous Summit at a deeper tier (bigger booth + workshop add-on) plus Berlin meetup, nothing else. Strongest single-event recognition, but zero EU presence where your signups and senior-SRE candidates are more likely reachable on a EUR 90k budget — all the year's visibility sits in one week, one country. Rejected: it doesn't reach "more signups" at all, and a single flagship is a fragile bet for something meant to "build and last."

**C — Regional spread + both hackathons.** Many small EU touches plus junior recruiting pipeline via hackathons, skip Ferrous Summit entirely. Cheapest per event, but misses the explicit awareness ask (no flagship), misses the recruiting ask (wrong seniority), and directly triggers the single-owner multi-metric problem the skill tells you to delete on sight. Rejected.

## Recommended portfolio — Portfolio A

| Event | Date | Objective | Model / tier | Fully loaded cost (planning band) | Threshold | Owner |
|---|---|---|---|---|---|---|
| Ferrous Summit | TBD 2027 | Awareness | Foundation/vendor-conf model, mid tier + one reach add-on | EUR 25,000–35,000 | See below | You (measurement) + lead engineer (on-site) |
| Regional Rust Day #1 | TBD 2027 | Adoption | Community conference, booth + demo | EUR 4,000–7,000 | See below | You + rotating engineer lead |
| Regional Rust Day #2 | TBD 2027 | Adoption | Community conference, booth + demo | EUR 4,000–7,000 | See below | You + rotating engineer lead |
| Berlin meetup (series) | Ongoing | Adoption | Meetup/user-group, sponsor the series | EUR 1,500–2,500/yr | Track, no hard threshold | You |
| Shared collateral (demo signage, senior-SRE recruiting card, reused across every event) | Once | — | — | EUR 500–1,000 | — | You |

**Reserve: EUR 15,000–20,000 (17–22%)**, held back for whichever of these lands mid-year:
- Regional Rust Day #3, if its audience evidence (step 2 below) scores as well as #1 and #2.
- The workshop add-on at a regional day once you've built a reusable curriculum — deliberately *not* funded in year one (see activation notes).
- A branded surface at Ferrous Summit if one worth having is still unsold when you're ready to buy.

**Cash total: roughly EUR 55,000–75,000 committed, plus the reserve** — leaves genuine headroom against EUR 90,000 rather than spending it all in January. These are planning bands from published analogous events (PyCon US, DjangoCon tier sheets), not quotes — get the real numbers before signing anything (next actions, below).

**Staff-time isn't in that cash figure.** Add your engineers' loaded daily rate × (prep + travel + on-site + follow-up) days per person before you call any of these numbers "fully loaded" — that line is the one teams skip and the one that most often doubles the real cost.

## Declined, with reason

| Event | Reason declined |
|---|---|
| Student hackathon #1 | ICP mismatch for the recruiting ask (senior SRE ≠ student), highest-effort model on the list (nights + weekend + judging), and stacking a third measurement track on one owner is exactly what this skill says to delete rather than rank. |
| Student hackathon #2 | Same. |

If a junior/new-grad pipeline becomes a real goal later — not this year's ask — hackathons are the right tool then. Not now.

## Effort ceiling check (36 travel-days across 3 engineers, 12 each)

| Item | People | Days each | Person-days |
|---|---|---|---|
| Ferrous Summit | 2 | ~5 (travel + on-site, US trip) | 10 |
| Regional Rust Day #1 | 2 | ~3 | 6 |
| Regional Rust Day #2 | 2 | ~3 | 6 |
| Berlin meetup (3–4 touches/yr) | 1 | ~1 each | 3 |
| **Committed** | | | **25 / 36** |
| Slack (Regional Day #3, follow-up trips, contingency) | | | 11 |

Two engineers minimum on every booth shift, per the activation playbook — a lone staffer can't cover a queue and a deep conversation at once. Leaving 11 days unspent is deliberate, not waste: it's what funds the third regional day if the evidence justifies it, and it's your margin against the trip that runs long.

## Activation, per event

**Ferrous Summit — help-desk booth, not a workshop.** Two technical engineers, rotating, both able to debug a stranger's cluster on their own laptop. Five-minute win: point the demo at a read-only sample cluster and show wasted spend live. No workshop here yet — you don't have a reusable curriculum, and building one for a single event burns a quarter of prep for one outing. If your CFP submission lands a talk slot, that's free awareness the sponsorship fee didn't buy — worth a shot (route to `conference-cfp-submission`). Design the live-demo failure plan before the event (`developer-live-demo-design`) — a demo that breaks in front of the one senior SRE you wanted to hire costs more than the booth fee.

**Regional Rust Days — booth + event-specific signup code this year, workshop next year.** Same demo, same staff brief, reused from Ferrous Summit — that reuse is the entire point of anchoring on one ecosystem. Build a real workshop curriculum once this year (a week of prep, not a quarter, because you'll have run the demo twice already) and debut it at these events in 2028, or at the reserve-funded third regional day if that gets triggered this year.

**Berlin meetup — stay informal.** No booth to buy at meetup scale; keep sending one person, keep it a light-touch, sponsor the series rather than one night so the host keeps editorial control.

**Recruiting overlay, everywhere.** One card at the booth: "we're hiring senior SREs." Any conversation that turns into a real recruiting conversation gets logged and routed to Recruiting on the same sheet as everything else — no separate booth, no separate trip.

## Measurement — one log, one owner, routed

Since you're the only measurement owner, discipline here matters more than anything above.

- **One conversation log**, one row per conversation: name, company, role, problem discussed, qualified (y/n), agreed next step, route (Marketing / Product / Engineering / Recruiting / Sales), follow-up sent date.
- **One event-specific signup URL + promo code per event**, never reused across events — a shared code makes every number unattributable.
- **Pre-event baseline**, captured 1–4 weeks ahead: branded search + direct traffic for the awareness read at Ferrous Summit; signup rate for the adoption read at the regional days.
- **Consent, explicit, at the EU events.** Regional Rust Days and Berlin sit under GDPR — badge scanning (if any exists) needs a purpose stated out loud, or default to opt-in (workshop signup, QR to a landing page) rather than assuming scan data is usable.
- **Follow-up within 48 hours**, referencing the actual conversation — never a batch sequence, and never all routed to Sales by default; most booth conversations aren't sales leads.
- **Check 30/60/90 days out** for adoption activations; one pipeline check a full sales cycle out if any enterprise conversation surfaced.

**Thresholds — set these before you sign anything, using your real numbers, not mine:**

CPQC target = derive from your blended CAC, not from the sponsorship fee. Example only, replace the inputs: if your blended self-serve CAC is roughly EUR 400 and you'd accept an event converting at a similar or better rate, target CPQC ≤ EUR 250–300 and a minimum of 25–35 qualified conversations at Ferrous Summit, 12–18 at each regional day. Fill in your actual CAC before this becomes a real threshold — an invented number here is worse than no number, because it looks decided when it isn't.

## Next actions, in order

1. **Send the evidence-request email** (audience actuals, track record, full package sheet, contract deadlines) to Ferrous Summit and all three regional Rust days before discussing price with any of them. A missing answer is itself the answer.
2. **Find Ferrous Summit's contract deadline now.** Large events close roughly a quarter ahead of the event — you're planning this in September 2026 for a 2027 event, which is good timing, but only if you move on it this quarter rather than next.
3. **Confirm who signs** and the earliest deadline you're actually facing — not asked in the brief, and it changes how fast step 1 needs to happen.
4. **Score all three regional Rust days** against the scorecard once evidence arrives; the two you commit to and the one you hold in reserve should come out of that score, not out of which one emailed back first.
5. **Set the real CPQC target** with your actual blended CAC before any contract is signed — not after.
6. **Review each event within two weeks of it happening**, while the conversation log is still accurate, and write the verdict (renew / renegotiate / drop) somewhere next year's budget cycle will find it. Judge Ferrous Summit's first year against awareness-stage expectations, not a pipeline verdict — that's a second-edition question.