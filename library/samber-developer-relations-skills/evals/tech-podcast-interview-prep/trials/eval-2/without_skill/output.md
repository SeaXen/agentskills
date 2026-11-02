Two hours, no research trip needed — you already have the material, you just haven't organized it. Here's the full prep, ready to use tonight.

## The one-sentence thesis (say this to yourself first)

*"Everything about Postgres that's 'just a footnote' at 500GB becomes the thing that pages you at 40TB — and almost none of it shows up in the documentation."*

That's your spine. Every story you tell should hang off it. If a story doesn't illustrate "the thing that was invisible until scale made it load-bearing," cut it.

## Tonight's two hours, blocked

**0:00–0:30 — Mine your own war stories.** Don't invent content — extract it. Grab a notebook and answer these five prompts with real numbers from your own incidents (Priya was SRE — she will ask "what was the actual number," so vague answers die on air):
- What's the worst `autovacuum`/wraparound scare you've had at scale, and how many hours from "noticed" to "fixed"?
- What backup/restore number surprised you (time to `pg_basebackup`, time to replay WAL, time to PITR to a point 6 hours back)?
- What's a query that was fine at 2TB and became a P1 at 40TB — what changed in the planner's behavior?
- What's a piece of hardware/infra math that broke (IOPS budget, WAL bandwidth vs NIC, replica lag under load)?
- What's a decision you'd undo — a schema choice, a partitioning scheme, an upgrade path — knowing what you know now?

Five answers, each with one real number, is more prep than most guests do in five hours.

**0:30–1:00 — Build the outline below into your own words**, swapping in your five answers. Don't write a script — write six index cards, one per section, three bullets each. Audio-only + edited means disfluency doesn't matter; forgetting your own point does.

**1:00–1:30 — Anticipate Priya's angle and rehearse the two landmine answers** (below) out loud, once, at speaking pace.

**1:30–1:50 — Say the whole thing out loud once, start to finish, no stopping to fix mistakes.** This is the single highest-value 20 minutes you have — it's the only rehearsal that catches "I don't actually know how to end that sentence" before a mic does.

**1:50–2:00 — Logistics, then stop.** Water nearby, phone on silent, quiet room booked, mic levels checked if you're supplying your own audio. Then close the laptop. An exhausted 6am-thinking guest is worse than an under-rehearsed one.

---

## The 45-minute flight plan

| Time | Segment | What it's for |
|---|---|---|
| 0–3 min | Cold open / who you are | One line on Tarnhelm, one line on how you personally ended up staring at a 40TB cluster. Do **not** lead with the product. |
| 3–12 min | "What breaks first" — vacuum & bloat | Your autovacuum/wraparound story. This is the single most universal pain at this scale; it'll resonate hardest with hands-on engineers. |
| 12–20 min | "The backup lie" — RTO/RPO at scale | The gap between "we have backups" and "we have a restore we've actually timed." Your PITR number goes here. |
| 20–28 min | "The planner doesn't know what you know" — stats & query plans | Cardinality estimation degrading at scale, extended statistics, the query that flipped plans overnight. Your P1 story goes here. |
| 28–36 min | "Replication is a capacity problem, not a feature" | WAL volume vs network/disk bandwidth, replica lag under bulk writes, logical replication's limits for zero-downtime upgrades at this size. Your hardware-math story goes here. |
| 36–42 min | "What I'd do differently" | Your undo-with-hindsight answer — partitioning strategy, schema decision, upgrade cadence. This is the reflective, honest moment; it's usually the clip that gets pulled for the trailer. |
| 42–45 min | Close / where to find you | One sentence on Tarnhelm *only if she asks directly or opens the door* — see below. |

You don't need more than six real stories for 45 minutes. Trying to cover more than that is how guests end up shallow on everything instead of sharp on a few things.

---

## Playing the host, not just the topic

Priya ran SRE at a logistics company — she will pull you toward **incidents, on-call, and capacity planning**, not schema aesthetics. Bias your answers that direction:
- Frame technical facts as "here's what the pager said" rather than "here's what the docs say."
- She'll likely ask a version of: *"What's the earliest warning sign, before it becomes an incident?"* — have a real leading-indicator metric ready (bloat ratio trend, replica lag trend, transaction ID age), not a generic "monitor everything."
- She may ask *"what would you have needed at 2am that you didn't have?"* — this is your best chance to sound like a practitioner, not a vendor. Answer with a missing runbook or missing metric, not a product name.
- Logistics = physical-world stakes. If you have any story where a Postgres slowdown had a real-world consequence (missed SLA, delayed shipment-adjacent process), that's gold for this specific host — lead with it if you have one.

## The conflict-of-interest landmine

You work at a company that sells a Postgres tuning product. Hands-on backend engineers have excellent pitch-detectors, and a 45-minute infomercial will get zero replays. Rule for tonight:

- **Don't name Tarnhelm until minute 40+, unless she asks directly.** If she asks what you do day-to-day, one sentence: *"I spend my time helping teams find the tuning knobs on Postgres that don't show up until you're already in pain — which is most of what we're talking about today."* Then pivot straight back to a technical answer. No feature list, no pricing, no "check us out" mid-episode.
- If she asks "so is this basically a pitch for your product" — welcome it, don't deflect: *"Fair question — I'll let you and the listeners judge that from what I actually say. Everything I'm describing today are things that happened before or independent of any tool, including ours."* Confidence here reads better than defensiveness.
- Save the actual mention for the close, and make it a *resource*, not an *ad*: "If any of this is live for you right now, the stuff I wish I'd had is [free thing — checklist, runbook, blog post], not a sales call."

## Two answers to have loaded before you sit down

1. **"What's the single biggest myth about running Postgres at scale?"** — almost certainly asked in some form. Have your one-sentence thesis above ready as the answer, then one story that proves it.
2. **"Should people just use [Citus/Spanner/CockroachDB/sharding] instead?"** — someone in an audience of backend engineers is thinking this. Don't dodge it: give one honest sentence on when horizontal solutions genuinely win, then one sentence on why 40TB single-instance Postgres is still common and what makes it viable (hardware got absurd, most of the pain is operational not architectural). Sounding evenhanded here buys credibility for everything else you say.

That's the full prep. You have real material — the job tonight was organizing it into a spine and stress-testing the two moments (the product mention, the "just use X instead" question) where you could accidentally sound like a vendor instead of a practitioner. Get through the 1:30–1:50 read-aloud and you're ready.