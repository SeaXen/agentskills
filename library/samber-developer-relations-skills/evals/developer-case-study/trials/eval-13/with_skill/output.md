**Verdict: her plan breaks the skill's own rule. Don't split revenue across studies.**

Skill (Measurement section) states it directly: "Do not attribute revenue to a single case study. Overclaiming attribution is the same credibility failure the artefact exists to avoid." Splitting closed-won revenue across every study a deal touched is still revenue attribution, just multi-touch instead of single-touch. Same failure, more decimal places.

**Why the split-revenue model fails, concretely:**

1. **No counterfactual.** A deal that read a case study would often have closed anyway — enterprise buyers who request a peer reference are usually already late-stage and leaning yes. Crediting the study for the whole deal (or a slice of it) assumes causation you can't prove.
2. **The split itself is arbitrary.** Equal-split across N studies touched has no basis — a study read once in passing gets the same weight as one the champion forwarded to their VP. Any allocation rule you pick is defensible-sounding, not true.
3. **It invites exactly the dispute finance/sales ops will raise.** First question back: "how do you know it was the study and not the rep, the demo, the free trial?" TrustRadius's B2B buyer data (in the skill's sources) puts vendor case studies at 28% impact — behind demos (71%), free trial (67%), prior product experience (67%). Case studies are one input among several stronger ones; a revenue number implies they're the deciding one.
4. **Customer-facing risk.** The named engineer in your case study consented to a quote and a metric about their own system — not to their name being tied to a dollar figure of revenue you closed because of them. If that number ever surfaces (board deck leak, a rep misquoting it to a prospect), it's a consent violation on top of a bad number.
5. **It doesn't survive scrutiny at scale.** Six studies this year, presumably more next year — the split gets messier as studies compound on the same accounts (a prospect who read three of your six studies before closing). The number becomes less meaningful exactly as the program grows, which is the opposite of what a program metric should do.

**What to show the CMO instead**

Give her *influence*, not *attribution* — a number that says "these studies are in the room when deals close" without claiming they caused the close. The skill's own measurement signals, mapped to a dashboard:

| Metric | What it is | Source |
|---|---|---|
| Deals influenced | Count + $ value of closed-won deals where a study was sent/referenced by sales during the cycle — reported as "touched", never split | CRM engagement notes, one per send, tagged to the study |
| Stage sent | Early (evaluation) vs late (post-verbal, as reassurance) | Same note, logged at time of send |
| Read-through / click-through | Opens, time on page, clicks to linked docs/repo/architecture page | Web analytics on the case study page |
| Inbound reference requests | Prospects asking to talk to that customer | Sales/AE-reported, logged as a note on the account |
| Customer self-amplification | Did the customer share it themselves (their own post, retweet, conference mention) | Manual tracking, checked quarterly |
| Coverage | Which adopter-type × use-case cells the 6 studies fill, and which are empty | Static matrix, updated per new study |

Six rows (one per study published last year), those columns. "Deals influenced" is the number closest to what she's asking for — report it as **"$X in closed-won pipeline touched by this study"**, explicitly labeled non-causal, never **"$X attributed to this study."** That wording distinction is the whole point: it's defensible in a board deck, the split-revenue number isn't.

**One gap to flag to her before this dashboard can populate:** none of this works unless sales is already logging "sent case study X" as a CRM touchpoint. If that's not happening today, the dashboard ships empty for six months while you backfill instrumentation. Check now whether reps currently log case-study sends as a note on the deal — if not, that's the actual next step, not the dashboard itself.