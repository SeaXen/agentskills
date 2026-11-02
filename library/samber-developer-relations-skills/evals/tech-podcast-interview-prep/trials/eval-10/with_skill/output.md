# Panel prep review — DevConf Amsterdam, "The Future of Platform Engineering"

Working from what you gave me: 5 panellists, 75 minutes, moderated, three messages, one 10-minute story about your internal developer portal rollout. I don't have the actual text of the messages or story, so this is a structural review against the skill's frameworks, not a line edit. Flag the biggest problem first, then the rest in priority order.

## Fix this first: the story is too long by roughly 8x

75 minutes ÷ 5 panellists = 15 minutes of raw slot each, before subtracting the moderator's intros, framing and wrap-up. Realistic speaking budget per panellist on a 5-person panel: **10-13 minutes total, delivered in fragments of 1-2 minutes across 6-10 turns** — never as one block.

A 10-minute story is not a *long* turn on this panel, it's *almost your entire airtime budget spent in one go*. Two consequences:

- A moderator running a 5-person panel will not hand you an uninterrupted 10-minute block. You'll get cut off mid-story, lose the payoff, and read as someone who didn't read the room — the panel skill names this exact failure as **domination**: visible disengagement from the other four panellists while you talk is as costly as talking over them.
- Even if you somehow got the full 10 minutes, you'd have nothing left for the three messages, the hard questions, or any cross-talk.

Restructure into three sizes, not one:

- **One sentence** ("we learned this the hard way rolling out our internal portal — short version: adoption didn't move until we killed the wiki-style docs and enforced a golden path"). This is what you actually use most turns.
- **60-90 seconds** — the core version, keeping the five-second moment (the flip: "we thought X, then this happened") and one real number. This is your default when the moderator or a fellow panellist invites the story.
- **Full detail** held in reserve for a direct follow-up question or audience Q&A only — never scheduled.

Split the story into 2-3 separable beats tagged to different questions rather than one continuous narrative. A story built to survive being cut off is stronger on a panel than one built to be told start to finish.

## Angle check: "future of platform engineering" is a topic, not an angle yet

Five people will get asked this exact framing. The failure mode for a "future of X" panel is that all five give some version of "it'll get more automated, more AI, more self-service" — indistinguishable, forgettable, AAA-shaped (fact, fact, fact, no tension).

Your portal rollout is your evidence for a specific, defensible, possibly contrarian claim — use it. Test: could a different platform-engineering panellist, with no portal rollout behind them, say your message and sound equally credible? If yes, it's still a topic. Sharpen until the claim only survives because you lived the rollout.

Build the spine explicitly — you don't seem to have one yet:

> "We had X, **and** it worked, **but** Y broke, **therefore** Z."

Everything else — the three messages, the story, the hard-question answers — should be re-derivable from that one sentence. If a message doesn't trace back to it, cut it or fold it in.

## Messages: three is the ceiling for a panel, not a comfortable default

The skill caps panel messages at two to three. You're at the limit, which is fine only if each one passes the **one-sentence answer test**: state it in 15-20 seconds, point first, before any context. Run this test on all three out loud. Any message that needs a run-up before the claim lands will get lost the moment the moderator moves on.

For each, check the shape is claim → evidence → so-what:

- **Claim**: one falsifiable sentence, no adjectives.
- **Evidence**: a number, a named constraint, an incident — not "it's better."
- **So-what**: what a listener does differently on Monday.

Since four other people are talking about the same broad topic, also check for overlap risk: if another panellist is likely to make a similar point (predictable on "AI's role" or "is this just DevOps rebranded"), have a one-line bridge ready — "building on what [X] said, but the part that surprised us was..." — rather than repeating a point that's already been made.

## Predicted hard questions for this specific panel

Built from the skill's question bank, mapped to "future of platform engineering" panels specifically:

| Class | Likely question here | Concede first | Bridge to |
|---|---|---|---|
| AI-hype scepticism | "Isn't 'platform engineering' just DevOps + AI rebranding?" | Name the part that is rebranding — say it plainly | Your message on what actually changed operationally |
| Why not just use X | "Why build a portal instead of just giving teams a Backstage template / direct cloud access?" | For a small enough team, direct access is fine — say where the line is | The message backed by your rollout evidence |
| Competitor/adjacent comparison | A fellow panellist's company does something similar — moderator may ask you to contrast | Where their approach is genuinely the better fit | The one workload where your trade-off flips |
| Roadmap/futures | "What's your boldest prediction for the next 3-5 years?" | This is the panel's premise, not a trap — but stay to what's defensible, not embargoed roadmap | A specific, falsifiable prediction, not vague optimism |
| Who is this not for | Rarely asked directly — volunteer it | — | When a portal is overkill; this is your highest-trust line on this panel |
| Own failure/incident | "What didn't work in your rollout?" | The real number: low adoption, wasted months, whatever the actual miss was | The so-what from your story |
| Lightning round | "hottest take" / "worst advice you've heard" | — | Prepare one genuine hot take, one non-self tool recommendation, one piece of common advice you disagree with |

Roadmap/futures is the one to watch: enthusiasm, not hostility, is what leaks things you shouldn't say on a "future of X" panel. Answer with what's already public plus the problem you're actually thinking about — never a date, never an unannounced feature.

## Depth calibration

DevConf panel audiences for a "future of" session skew toward staff engineers, architects and engineering managers more than pure hands-on ICs (deep technical dives pull the IC crowd to breakout talks, not panels). Anchor at **staff/architect level** — trade-offs, invariants, what breaks at scale — and drop line-level implementation detail. Keep one framing per point that also lands for the EM/buyer layer (operational cost, risk, adoption), since panels draw decision-makers.

Round every number and pair it with a comparison. "Adoption went up" tells the room nothing; "adoption went from 20% to 70% of teams in a quarter, without a mandate" is a sound bite.

## Disclosure and what you can actually say

You're clearly representing your employer here (it's *your* internal portal). State that plainly and early — "I run the platform team at [company], we shipped our internal developer portal about a year ago" — rather than letting it surface mid-answer. This is B2B-flavoured: any adoption number, cost figure or ROI claim you use can get quoted back into someone's own internal business case, so use only numbers you're cleared to say publicly. If the 10-minute story includes anything not yet publicly shared (exact costs, headcount, an unannounced next phase), clear it before the stage, not after.

## Panel mechanics, since this is live with no retakes

- **Jump in unasked.** Waiting to be addressed on a 5-person panel reads as invisibility, the mirror failure to domination.
- If the moderator asks something vague or leading, rephrase it out loud before answering it — "what I think you're asking is..." — rather than answering the weak version of the question.
- Pre-decide one recovery line for when an answer collapses mid-sentence — moves to firmer ground rather than stalling.
- Slow down under pressure rather than speeding up; it's the single highest-leverage on-air correction and it also kills filler words.

## Recording-day card

- One-sentence version of each of the 3 messages, one-sentence version of the story, memorised well enough to survive an interruption.
- One open loop to plant early on your first turn ("there's a mistake in our rollout I'll come back to"), closed by name if asked to expand, or in a closing round.
- Disclosure line ready for your first substantive answer.
- Water within reach, phone silenced, note the moderator's name.
- Don't read from a script — bullets only. A memorised paragraph that gets interrupted has nothing underneath it.

## What I'd need to sharpen this further

I can do a line-by-line pass on the actual three messages and the story once you paste them — checking the so-what test, the five-second moment, and whether the claims survive being read cold. Also useful to know, if you want the rest of the brief filled in: prep time you have before DevConf, whether the session is recorded/streamed, and whether the other four panellists or their companies are known yet (changes how sharply you can pre-empt the competitor-comparison question).