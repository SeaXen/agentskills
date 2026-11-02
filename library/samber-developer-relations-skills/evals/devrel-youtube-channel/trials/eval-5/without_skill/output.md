# Kestrel Queue: $40k YouTube plan for the half

**Next action (15 min):** send your CMO the three questions in "Before you sign anything". Everything below assumes a 26-week half and one owner at about 8 h/week, roughly 200 h. Both are my assumptions, so correct them.

## Verdict

⚠️ Do not run the plan as written. Three parts break:

1. **Audience fit.** A general tech-news audience is mostly not the person who picks a message broker. That person is a backend, platform, or SRE engineer. This is unproven, not false, so the plan tests it before spending.
2. **Word-for-word script.** Scripted reads convert worst because the audience came for the creator's voice. A script also makes you the author of every claim, so you carry the legal risk.
3. **Promo code as the only measure.** An open-core broker is adopted by someone running `docker pull` and a quickstart. A code only catches a paid purchase, months later, often by a different person. Most of the impact would read as zero.

Also: the board approved "YouTube influencers", plural. One creator at $40k is a narrower bet than what they approved.

**Keep the CMO's pick, gated.** He stays in the plan as one test, capped and conditional. The rest of the money goes to niche creators and a reserve.

## Budget (all splits self-set, none industry figures)

| Line | Cash | What it buys | Hours |
|---|---|---|---|
| CMO's creator, 1 integration | up to $14k, only if the gate passes | 1 sponsor segment, brief-based | ~30 |
| Niche backend/infra creators (20k–300k subs) | $18k | 4–5 integrations at $3–6k each | ~90 |
| Paid amplification of the best performer | $2k | Creator content run as ads, if usage rights are signed | ~10 |
| Tracking and landing pages | $0 cash | One URL per creator, UTMs, "heard from" field | ~25 |
| Reserve (15%) | $6k | Second integration with the winner, or an unplanned opportunity | ~15 |
| Program ops and reviews | $0 cash | Vetting, contracts, 14-day and 45-day readouts | ~30 |
| **Total** | **$40k** | | **~200** |

- **Rate reality.** Generic rate guides put 500k+ creators at $10k–30k+ per post. That is a negotiation anchor, not a quote. Ask for his rate card first.
- **If his quote is above $14k**, he drops to the unfunded list. The money goes to niche creators and the reserve.
- **Whitelisting** is the $2k line. The right to run his video as your ad is often the highest-return clause, so negotiate it in every contract.

## Before you sign anything

Send the CMO these three requests for his creator:

1. **Audience analytics screenshot.** Ask for the share of viewers who are developers or backend and infra engineers. My proposed gate is at least 30% (self-set). Below that, he is out.
2. **Last 3 sponsor segments.** Check how the audience responded in comments and whether it looks like paid-reach noise. Also check for competitor conflicts and brand-safety issues in the last 3 months.
3. **Rate card and terms.** You need price, usage rights window (3–6 months), exclusivity against other brokers, how long the video stays up (12 months), and a make-good if it is pulled early.

## The brief replaces the script

The creator gets:

- **The why:** one sentence on the problem Kestrel Queue solves.
- **2–3 talking points, max.** Each one must be provable and tied to real benchmarks or user results.
- **One CTA:** a vanity URL, `kestrelqueue.dev/<creator>`, going straight to the quickstart.
- **Guardrails:** no claims about features that do not exist, no benchmark claims without a published method, and the disclosure requirement.
- **Creative freedom,** stated explicitly.

You get one review round, limited to factual accuracy and legal. You do not review tone or wording.

**Disclosure is non-negotiable.** The creator says "sponsored" aloud in the video, and uses YouTube's paid-promotion label. Put it in the contract and check it after the video goes live. Brand liability sits with you, not only the creator. If you sell in the EU or UK, have legal check local rules.

## Measurement

**Primary metric: activated developers per dollar.** An activated developer ran the quickstart and produced a first message. Choose that definition with your team before launch.

Set up before any video goes live:

1. **One vanity URL per creator,** with UTMs on every description link.
2. **Quickstart ref parameter** or opt-in telemetry tag, so activation ties back to the creator.
3. **Required "how did you hear about us" field** on signup and cloud trial. It catches what URLs miss.
4. **Promo code, as a secondary signal only.** Keep it for the paid conversions it can catch.
5. **Branded-search and direct-traffic lift,** compared against a baseline for the 14 days before each video.
6. **GitHub stars and docs sessions,** read as trends. They are not a verdict.

**Thresholds.** I don't have your baseline, so the first two creators are an experiment. Each gets a fixed window of 45 days. At the first readout, set the renew-or-drop bar from your own data, for example your current cost per activated developer from existing channels. A bar chosen after seeing results is a narrative, not a threshold. Write it down before video one ships.

## Timeline (26 weeks)

| Weeks | Do |
|---|---|
| 1–2 | Pull baseline: current activation numbers and cost per activated developer. Build the tracking. Shortlist 15 niche creators and vet each one's audience and past sponsor results. |
| 2–5 | Personalised outreach to 10, not a blast. Close contracts for the first 2 niche creators and the CMO's creator if he passes the gate. |
| 5–10 | First 2–3 integrations go live. Read each at 14 days and at 45 days, because YouTube is a long-tail channel. |
| 10 | **Mid-point gate.** Compare cost per activated developer across all live creators. Cut the weakest fit. Decide where the reserve goes. |
| 10–20 | Remaining niche integrations. A second integration with the best performer, since repeat posts usually beat the first. Whitelist the best video as a $2k ad test. |
| 20–26 | Final readouts. Write the verdict for the board: cost per activated developer, by creator, against the baseline you set in week 2. |

## Reallocation triggers

- A creator misses the bar twice, so you stop buying that creator.
- A creator's audience data fails the gate, so they never get a slot.
- A creator ships without the disclosure, so you invoke the kill/rework clause.
- A clear winner emerges, so the reserve funds a second integration with them.

## Cut list if the budget shrinks

1. **20% cut ($8k):** drop the amplification line and the fifth niche creator.
2. **40% cut ($16k):** also drop the CMO's creator, unless his quote and audience data are better than the niche options.

## Unfunded list

- **Large-creator sponsorship above $14k.** It would be funded if his audience data shows a strong backend share.
- **Affiliate or commission deals.** These come back if activation tracking proves reliable.
- **Ambassador program.** It needs the winners first.

## Five-sentence board narrative

1. We will test YouTube creators with a fixed budget and a rule to stop spending on those who do not deliver.
2. We chose engineers who build backends, not a general audience, because they pick message brokers.
3. We let creators speak in their own words, because scripted ads convert worst.
4. We count developers who run our quickstart, not views or promo codes.
5. In week 10 and week 26 you will see cost per activated developer by creator, against a baseline we set in week 2.

## Open questions (answer these to tighten the plan)

1. Which 26 weeks is "the half"? I assumed it starts now.
2. What is your current cost per activated developer, from any channel?
3. Who owns this program, and how many hours a week do they really have?
4. Does the CMO already have a quote or contract from his creator?
5. Which competitors (Kafka vendors, NATS, RabbitMQ) must you block via exclusivity?

⏳ **Next:** send the CMO the three requests above, about 15 minutes. Then tell me the answers to questions 1–3 and I'll set the thresholds and lock the timeline.