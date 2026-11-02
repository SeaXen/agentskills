# What to tell your CFO about seven months of build-in-public

## The reframe, first

She didn't ask "is engagement good." She asked what it *returned* — a revenue or pipeline question. Follower count and engagement rate don't answer that, and you're right to feel stuck: **no attribution tool will hand you a clean number for content like this, because the mechanism it works through is largely invisible to tracking.** A developer reads your post on X, mentions it in a team Slack three weeks later, a colleague Googles "Corvid Labs" and signs up. Every analytics tool logs that signup as "organic search" or "direct." The post gets zero credit, even though it caused the conversion.

That's not a reason to give up on measuring it. It's a reason to measure the right things and be explicit with her about what's provable versus what's a reasonable read.

## What's actually happening to your funnel, in order

| Stage | What it looks like for build-in-public | Where it hides from you |
|---|---|---|
| Reach | Impressions, followers, engagement | Visible — but this is the vanity layer, not the return |
| Recall | Someone remembers the brand later | Shows up as **branded search** and **direct traffic**, not "social" |
| Word of mouth | Screenshot in a Slack, mentioned on a call | **Dark social** — invisible to any tool |
| Conversion | Signup, demo request, trial | Only visible if you **ask** at the moment it happens |
| Revenue | Deal closes | Only visible if the source survives into your CRM |

The honest structural problem: you have a top-of-funnel motion (content trust-building) being judged by a bottom-of-funnel yardstick (revenue return), with none of the connective tissue instrumented. Fix the connective tissue before you try to answer the question again.

## What to measure — three tiers

**Tier 1 — Cost (you likely haven't priced this at all)**

- Hours per post × posts published (≈2/week × 30 weeks) for both of you, at fully-loaded cost. This is your real "spend" — there's no media line item, but the CFO will respect that you quantified the opportunity cost instead of pretending it was free.
- Any tool/scheduling costs on top (usually near-zero).

**Tier 2 — Leading indicators (pull these today, no new instrumentation needed)**

- Branded search volume trend for "Corvid Labs" / product name (Search Console) over the 7 months. This is the single best proxy for "did people start remembering us" — it's the recall layer showing up as a number.
- Direct traffic trend to the site (GA4/Plausible). Rising direct alongside flat/rising branded search = the content is building recall that isn't tagged to any channel.
- Referral traffic from each platform to site (you have this already, just isn't framed as ROI — frame it as top-of-funnel volume, not conversion).
- Follower/engagement trend by platform, but present it as a *leading* indicator only, never as the headline.

**Tier 3 — Revenue signal (the part that's actually missing, and the part she cares about)**

- **Self-reported attribution.** Add "How did you hear about us?" to your signup/demo form now — open text plus a pick-list with "other." This is the highest-leverage fix you can make this week, and it's the only instrument built to catch dark social.
- **CRM notes forensic pass.** Search existing deal/signup notes for "Twitter," "X," "LinkedIn," "saw your post," "following your build in public." Free, retroactive, and gives you real anecdotes for this week's conversation even before new instrumentation lands.
- **First-touch capture on signup.** If you're not already stamping `utm_*`/referrer on first visit and carrying it through to the CRM record at signup, that's the gap between "we have Google Analytics" and "we can attribute a deal." Fix this once, it pays out every quarter after.
- **A natural experiment.** You have 7 months of posting cadence that wasn't constant. Overlay weekly signups against post publish dates and any weeks you skipped or doubled up. Not causal proof, but a defensible directional read — and cheap, since the data already exists.

## What to tell her this week

Don't present a number you can't defend. Present this instead:

> "Standard attribution tools will under-credit this by design — a lot of what build-in-public drives shows up as 'direct' or 'organic search' because people act on it later, or tell a colleague instead of clicking a link. Here's what we can show today: [branded search trend], [direct traffic trend], [X CRM notes explicitly citing our posts as the reason they signed up]. Here's what it cost us: [hours × loaded rate]. Here's the fix — I'm adding a 'how did you hear about us' field and first-touch tracking this week, so next quarter I can give you an actual pipeline-dollar number with a confidence level, instead of a vibe."

That's a CFO-credible answer: it names the measurement problem instead of hiding behind it, gives her real (if partial) numbers now, and commits to a specific, dated fix rather than a vague promise to "look into analytics."

## 30-day plan to have a real number next time she asks

1. **This week** — add the self-reported field to signup/demo forms; run the CRM notes search; pull branded-search and direct-traffic trends.
2. **Week 2** — wire first-touch UTM/referrer capture through to the CRM record (if using HubSpot/Salesforce, this is a form-field mapping, not a rebuild).
3. **Week 3** — tag every post-driven link with consistent UTMs going forward (you likely have none today — check).
4. **Week 4** — build the one dashboard that matters: self-reported source × signups × (if traceable) pipeline value, shown next to branded-search/direct trend as the "can't self-report, but converging" signal.
5. **Ongoing** — revisit quarterly, not monthly. Content-driven recall moves slower than paid — judging it monthly will make it look flat when it isn't.

## One thing to say if she pushes on "just tell me the ROI"

There isn't a single true number — every attribution model is an opinion about which touch gets credit, and yours is a channel that mostly shows up as *absence of a channel* (direct, branded search). What you can commit to is a **consistent, improving measurement**, not a perfect one. That's a normal, fundable answer. What's not fundable is continuing to publish for seven more months without being able to say anything more specific than "engagement looks fine."