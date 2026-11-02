# Before the script: is this worth doing as asked?

**Read:** unpaid, "fresh" video, requested *before* the first round, when you already have 4 published videos + a conference recording — mildly extractive, but not disqualifying. For a demo-facing role (DevRel / Developer Advocate / Solutions Engineer / Sales Engineer — which "so the panel can see your style" strongly signals), showing presentation chops live or on tape is a legitimate part of the bar, not a scam. The tell isn't the ask itself, it's *how the recruiter reacts if you push back a little* — that reaction is free signal about the company.

**Cheap move before you spend 3+ hours scripting/recording:** offer your existing catalogue first, and float a lighter-weight alternative. Costs you one email, five minutes.

> Hi [name] — happy to bring the demo energy to the panel. I've got four published product demos and a conference talk already out there [links] that show my style pretty directly — want me to send those over instead of producing something new? If the panel specifically wants something fresh, I can do a quick unscripted screen-recording (5 min, no editing) rather than a polished production — let me know which is more useful, and I'll turn it around by [date].

If they insist on a fully new, produced video anyway — fine, that's the answer below. If they get cagey or pile on more unpaid asks after this, that's the real signal, independent of the video.

**Also ask this in the same email, plainly:** "Could you share what the rest of the loop looks like after this — number of rounds, who's on each panel?" Normal question, always safe to ask, and it directly solves your "no idea what else is in the loop" problem better than me guessing.

---

# 1. The 5-minute demo script

You have ~8 days before the loop starts (today's the 20th, loop starts Monday the 28th). Script tonight, record within 2 days, leaves you a buffer for a re-shoot.

Target: **650–750 spoken words** for 5 minutes at a natural pace. Structure below — timing first, then the beat-by-beat with `[BRACKETS]` for Voretti-specific content you drop in.

| Time | Beat | Purpose |
|---|---|---|
| 0:00–0:25 | Cold open — who has this pain | Hook, no logo-slide throat-clearing |
| 0:25–1:00 | The problem, in the user's words | Show you can frame a problem before pitching a fix |
| 1:00–3:30 | Live walkthrough, 3 beats | The actual demo — this is what's being judged |
| 3:30–4:15 | Why it matters (business/dev impact) | Shows product sense, not just feature-narration |
| 4:15–5:00 | Close | Confident wrap, ties back to *you* |

### Script skeleton (fill the brackets)

**[0:00–0:25] Cold open**
> "If you've ever [specific, concrete moment of pain — e.g. 'shipped a change on a Friday and spent the weekend babysitting logs because you had no idea if it actually worked'], this is for you."

Start mid-scene, not "Hi, I'm going to show you." No intro slide. Screen already on the problem state (an error, a slow dashboard, a broken build — whatever's real).

**[0:25–1:00] Problem framing**
> "Here's what usually happens: [status quo, 2–3 sentences, concrete]. That costs [team/person] [time/money/trust]. [PRODUCT] exists because that shouldn't take more than [X]."

Keep this to 3 sentences max. This section is where most homemade demos ramble — don't.

**[1:00–3:30] Live walkthrough — exactly 3 beats, no more**
Pick three moments, each with its own micro-arc (do a thing → show the result → say why that result matters):

1. *[~1:00–1:50]* "Watch this: [first action, e.g. run a command / click a button]. [Result appears]. That's [why this specific result is non-obvious/impressive]."
2. *[~1:50–2:40]* "Now here's the part most tools get wrong: [second action]. [Result]. Notice [detail a careless demo would skip]."
3. *[~2:40–3:30]* "And last — [third action, ideally the 'wow' moment]. [Result]. That's the whole loop, [X minutes/seconds] instead of [old way]."

Narrate what you're doing *before* you do it (viewers get lost if the cursor moves before the words explain it). Never read UI labels aloud — explain what they mean.

**[3:30–4:15] Why it matters**
> "The reason this matters isn't [the feature itself] — it's [second-order effect: fewer incidents, faster onboarding, less context-switching, whatever's true]. For a team like [target user], that's the difference between [bad outcome] and [good outcome]."

This is the sentence that separates "I can click buttons" from "I understand what I'm selling." Panels weight this beat heavily.

**[4:15–5:00] Close**
> "That's [PRODUCT] — [one-sentence restatement of the value, not a feature list]. [Optional: one sentence on what you'd build/fix/demo next if this were a real onboarding call]."

End on a decision or opinion, not "thanks for watching." An opinion ("if I were pitching this to a skeptical platform team, I'd lead with X, not Y") is what shows *style*, which is literally what they asked to see.

### Production notes
- One take beats ten perfect ones. Panels calibrate for "can this person think on camera," not editing skill.
- Record audio separately if your only mic is a laptop mic — voice quality reads as competence in a demo review more than people expect.
- Don't use Voretti's own product as your demo subject unless they gave you access/asked for that explicitly — demoing *your* project is safer and still shows the same skills.
- Cut your first 10 seconds in the edit. Almost everyone's real hook starts there, not at 0:00.

---

# 2. What's probably still in the loop

You weren't told, so plan for the common shape of a demo-facing loop at a ~120-person dev-tools company:

1. **Recruiter screen** — sounds done already.
2. **Hiring manager conversation** — "why us, why now," role-fit, not technical.
3. **Live technical/product deep dive** — likely a *second*, live version of what you're pre-recording now (walk through a project of your choosing, or pair on their product). If it overlaps heavily with the video, that's worth quietly noting — you can even ask the recruiter directly ("does the onsite also include a live demo, or does the video replace that step?").
4. **Cross-functional panel** — usually eng + PM + one of sales/CS/support. Behavioral questions dominate here — this is where the STAR bank below gets used.
5. **Values/culture conversation** — often with someone outside your reporting line.
6. **Exec or founder close** — short, vision/motivation-checking, not deep technical.

Prep priority given your week: script + record the video first (concrete deadline), then STAR bank (below), then a light pass on Voretti's product/market/competitors so you're not walking in blind to the deep-dive round.

---

# 3. STAR bank to memorize

Memorize the **bullet skeleton**, not prose — recite the shape, fill live detail from memory of the real event. Each one below is a *draft scaffold* built on the real anchors in your background (samber/lo, samber/do, samber/oops, samber/hot as OSS Go libraries; organizing France's largest GenAI meetup, an annual hackathon, Startup Weekend Nantes, and a GenAI conference under a community non-profit). Swap in your actual numbers, dates, and outcomes before you say any of these out loud — don't recite a placeholder as if it were a fact.

**1. "Explain something technical to a non-technical audience."**
- S: [Meetup/conference talk or onboarding a non-Go-fluent contributor to `samber/lo` or `samber/do`]
- T: Needed them to grasp [generics / DI / a specific concept] without the jargon
- A: Used [analogy/live example], checked understanding before moving on, cut the slide deck in favor of live code
- R: [concrete outcome — they shipped a PR / adopted the pattern / audience retention]

**2. "A live demo or talk that went wrong — what did you do."**
- S: [specific conference/meetup moment — a live-coding failure, a question that broke your flow, a tooling crash]
- T: Recover without losing the room / stakeholder trust
- A: Named the failure out loud instead of hiding it, pivoted to [backup plan / explained the bug live as content], kept pace
- R: [audience reaction, what you changed for next time]

**2b. "Handling harsh public feedback."**
- S: [a GitHub issue, PR review comment, or post-talk critique that stung]
- T: Respond without getting defensive, extract the signal
- A: Separated tone from substance, [fixed the root cause / opened a follow-up issue / changed the API], replied publicly
- R: [relationship/reputation outcome — contributor stayed engaged, issue closed, pattern now documented]

**3. "Influence without authority / got engineering to prioritize something."**
- S: [a recurring community/user pain point surfaced repeatedly in `lo`/`do`/`oops` issues]
- T: No authority to force a fix, needed someone else's time
- A: Built the case with [evidence — issue count, a minimal repro, a benchmark], proposed the smallest viable fix, made it easy to say yes
- R: [merged, shipped, adopted]

**4. "Built something from zero with limited resources."**
- S: [starting the GenAI meetup / hackathon / Startup Weekend Nantes under a community non-profit]
- T: Grow it from nothing, no budget/team at first
- A: [first 10 people, first sponsor, first speaker lineup — whatever's true], iterated on format
- R: [current scale — "one of the biggest French GenAI meetups," attendance, recurring cadence]

**5. "Prioritizing under competing demands."**
- S: [maintaining multiple OSS repos + running community events simultaneously]
- T: Limited hours, all demands legitimate
- A: [explicit tradeoff you made — e.g. triaged issues by impact, batched community work into fixed weekly blocks]
- R: [what shipped, what you deliberately let slip and why that was fine]

**6. "Learn something fast to teach/demo it."**
- S: [a new Go feature, library, or infra tool you had to get fluent in fast — e.g. adopting a new stdlib package or db tech]
- T: Needed working fluency in days, not weeks, to [ship / present / unblock others]
- A: [how you actually learned it — read source, minimal repros, benchmarked against known behavior]
- R: [shipped feature / talk delivered / bug found because you went deep instead of skimming docs]

**7. "Disagreed with a decision and handled it."**
- S: [a design/API/positioning call on one of your libraries or at an event you helped run]
- T: You saw it differently, decision wasn't yours alone
- A: Made the case once, with evidence, then [committed to the decision / got it revisited with new information]
- R: [outcome + what you'd do differently]

Delivery tip: keep each spoken answer to **60–90 seconds**. Panels penalize rambling STAR answers more than short ones — say the Result, then stop talking.