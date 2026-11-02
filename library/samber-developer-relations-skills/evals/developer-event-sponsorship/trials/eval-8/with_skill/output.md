# Kilnworks — 2027 Event Measurement Plan (Porto hackathon + Chicago platform-eng conference)

## The KPI as stated won't survive contact with Porto

"Pipeline sourced from events" is a valid metric for exactly one of your two commitments. Applying it to both forces a choice between two bad outcomes: report zero for Porto (kills the case for ever sponsoring it again) or let someone backfill the number by pushing 500 student badge scans into the CRM as leads (fills the pipeline report with records the sales team will never work, and burns their trust in the number).

The two motions have different buyers, and the buyer decides what's measurable:

- **Self-serve CLI** ($29/mo, card, no sales contact): success is measured in-product — signups, activations, retention. There is no "opportunity" stage to source into.
- **Enterprise platform** (4-person sales team, 9-month cycle): success rides on the CRM. The attendee is a champion, not a signer — the event *influences* a pipeline that closes quarters later, it rarely *sources* a deal on its own.

Same split applies to the two events by audience:

- **Porto (500 students, hackathon)** — no budget authority, no buying influence, mostly not enterprise-track careers yet. This is the scorecard's own bottom anchor for a pipeline objective: *"students or pure hobbyists (for a pipeline objective)"* scores 0–1 on decision access. Objective: **Awareness**, with **Adoption** as the secondary signal (hackathon = hands-on build path with the CLI).
- **Chicago (enterprise-heavy platform engineering conference)** — practitioners who hold or influence platform-tooling budget. Objective: **Pipeline**.

Recommendation: **set the objective per event, not one for the year**, and replace the single KPI with a structure that still gives leadership one clean number — just not "pipeline."

| Event | Motion it serves | Objective | Primary metric | Do not claim |
|---|---|---|---|---|
| Porto hackathon | Self-serve CLI | Awareness (+ Adoption) | Branded search/direct-traffic lift vs. pre-event baseline; cohort activations still active at 30/60/90 days | Attributed revenue, pipeline sourced |
| Chicago conference | Enterprise platform | Pipeline | Opportunities and influenced pipeline traced to logged conversations | Sourced-revenue claims the CRM can't support — call it *influenced*, not *sourced*, unless first-touch CRM attribution genuinely credits the event |

## The one board-level KPI that actually works

Swap the board KPI from **"pipeline sourced from events"** to **"cost per qualified conversation (CPQC)"** — fully loaded cost ÷ qualified conversations. It's the one unit the skill's own model calls out as comparable "across a hackathon, a community day and a mega-conference." Pipeline $ isn't computable at Porto; CPQC is computable at both.

Board slide shape:

- **Top line (the one KPI):** CPQC, reported per event, both events lower than the current blended acquisition cost for the motion they feed.
- **Second line (what CPQC bought, motion-specific):** Chicago → pipeline $ influenced. Porto → cohort activations, expressed as an ARR-equivalent ($29/mo × activated seats × observed 90-day retention) so it still reads as a dollar figure without being mislabeled pipeline.

If leadership insists on keeping the word "pipeline" on the slide, fall back to a two-row honest version instead of one blended number: *"Pipeline & Activation Sourced/Influenced from Events"* as the section header, with Chicago's pipeline $ and Porto's activation $ as separate, clearly labeled rows. Don't let anyone collapse those two rows into one sum — a dollar of enterprise pipeline and a dollar of self-serve ARR-equivalent aren't the same risk-adjusted thing, and a merged figure invites exactly the "great buzz, no comparable number" failure mode this model exists to prevent.

## Porto hackathon — measurement one-pager

**Objective:** Awareness (+ Adoption) · **Owner:** self-serve growth/product-led-growth owner · **Buyer:** individual developer, card payment

**Qualification bar (adapted to self-serve — there's no "decision-maker" to check, the attendee *is* the decision):**
A conversation/interaction counts as qualified when the person (a) has a real workflow the CLI solves, (b) is the one who'd install and pay for it, (c) agreed to a concrete next step *during the event* — installed the CLI against a real project, redeemed the event promo code, or opted into a specific follow-up (not a generic newsletter).

**Fully loaded cost worksheet:**

| Line | Notes for Porto |
|---|---|
| Sponsorship fee | after any published discount |
| Add-ons | workshop/mentor slot if bought |
| Prizes and credits | hackathon prize track, plus the cost of honoring any credit awards |
| Swag and print | count what's handed out, not ordered |
| Travel and accommodation | per staff member, including travel days |
| Staff time | loaded daily rate × (prep + travel + on-site + follow-up) days |
| Opportunity cost | what those engineer-days would've shipped instead — note even if unpriced |

**Threshold (set before the sponsorship goes live, not after):**
- Target CPQC ≈ current blended paid-acquisition CAC for the self-serve motion × expected event-cohort trial→paid conversion (hands-on hackathon traffic typically converts better than cold paid traffic — use your own paid-channel CAC as the ceiling, not the sponsorship fee).
- Minimum qualified-interaction count: set from staffing capacity — how many meaningful conversations your on-site engineers can realistically log and quality-check across the event, not from the 500 headcount.

**Tracking mechanics:**
- One event-specific signup URL + one promo/credit code, unique to Porto — never reused.
- Pre-event baseline: branded search + direct traffic for the 1–4 weeks prior.
- Consent: workshop signup, opt-in draw, or QR to a Porto-specific landing page — no badge-scan-everyone default.
- Conversation log, one row each: name · what they built/tried · qualified (y/n) · next step · owner · follow-up sent date.
- Follow-up within 48 hours — a product invitation (trial extension, credit, onboarding help), never a sales sequence; this cohort has no sales contact by design.
- Measure activation/retention at 30/60/90 days against the event-cohort URL/code, not against a generic signup pool.

**Routing (adapted — no Sales route by default):**

| Conversation surfaced | Route to |
|---|---|
| Feedback / feature requests | Product |
| Bugs found live | Engineering |
| Usable build/demo story | Marketing (case study/DevRel content) |
| Genuine enterprise-track interest (rare, but happens even at student events) | Flag to enterprise Sales as a *future* lead, not this KPI |

## Chicago conference — measurement one-pager

**Objective:** Pipeline · **Owner:** enterprise sales lead (one of the 4 AEs, named) · **Buyer:** platform/infra decision-maker or influencer

**Qualification bar:** the conversation partner (a) has the platform-engineering problem the product solves, (b) holds or visibly influences the buying decision (title/role check, not just "attended"), (c) agreed to a named next step — scheduled discovery call or demo within 2 weeks, owner named.

**Fully loaded cost worksheet:** same line items as above, minus prizes, plus booth build/shipping and any branded-surface add-on; staff time here should price the AEs' and SEs' loaded day rate, which is typically the line that doubles the total for a 4-person team traveling together.

**Threshold:**
- Target CPQC ≈ current blended enterprise CAC (cost to generate one qualified opportunity through your existing pipeline) × your historical conversation→opportunity rate.
- Minimum qualified-conversation count: set jointly with the 4-person sales team based on what they can actually follow up on inside two weeks — a booth that produces more qualified conversations than the team can work is a staffing failure, not a win.

**Tracking mechanics:**
- One event-specific URL/code, distinct from Porto's.
- Pre-event baseline: not branded-traffic (wrong metric for pipeline) — baseline your current opportunity-creation rate per AE per week, so the event's lift is visible against normal pipeline generation.
- Badge scan only with purpose stated out loud; bounded record (name, title, company, work email).
- Same conversation-log schema as Porto (keeps CPQC comparable across the portfolio), qualification bar swapped per above.
- Follow-up within 48 hours, on the substance discussed, from the AE who owns the account.
- **Non-standard cadence for this event specifically:** the 30/60/90-day checkpoints will understate value against a 9-month cycle. Add one dedicated pipeline check timed to the sales cycle (~month 9 post-event), and report interim opportunity-creation and stage-progression at 30/60/90 as leading indicators only — label them as such on any interim slide so nobody reads a 90-day number as the final verdict.

**Routing:**

| Conversation surfaced | Route to |
|---|---|
| Buyer-track conversation | Sales (named AE) |
| Platform/integration partner interest | Partnerships |
| Feature feedback from platform teams | Product |
| Case-study-worthy account | Marketing |

## Pass check

Both events now carry what the skill requires before anything is called measurable: one primary objective each (not one for the year), a fully loaded cost worksheet, a target CPQC derived from your own blended CAC per motion (not the sponsorship fee), a minimum qualified-conversation count sized to staffing, and a named owner for follow-up. Open items only you can fill in: current blended CAC for each motion, and who specifically owns follow-up on each side — plug those into the two worksheets above before either contract is treated as locked.