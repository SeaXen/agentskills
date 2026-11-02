**Kill two lines before you walk in. Both fail live, not just on principle.**

- "Widely misunderstood" on the licence question — audiences read that as calling *them* stupid. Skill's own failure list: guest calls it a misunderstanding → loses the room.
- "Can't comment, legal's involved" on the outage — flat non-answer. Clip outlives the episode. Ade will push exactly here because it sounds like a door closing.

Both are fixable without exposing you legally. Below: 8 predicted questions, each with the concession to say first, then the bridge. Concession before bridge, always — bridging straight from the question is the move a technical audience spots instantly.

| # | Question (Ade's likely phrasing) | Say first (concession) | Then bridge to |
|---|---|---|---|
| 1 | "You moved Fenwick Broker from Apache 2.0 to BUSL last March. Walk me through why." | Name the real cost, not the PR framing: "It broke a promise people built on — that's real, not a misunderstanding." Then state the actual forcing constraint (fill in: {hosting/cloud provider repackaging without contributing} or {funding runway}). Never call it "misunderstood." | What's guaranteed going forward — BUSL's change-date clause reverting to Apache/MIT (give the actual date if one exists). |
| 2 | "That announcement got a 900-comment pile-on. What did you get wrong?" | Concede the comms failure specifically — e.g. "we shipped it as a blog post with zero warning window." Specific beats vague. | What changed in how you announce changes now (RFC, notice period, whatever's real). |
| 3 | "What actually happened in the June outage?" | Impact in real units, whatever's already public: duration, what broke, data lost or not. | The mechanism + the fix, then the detection change made since. |
| 4 | "Legal's still involved — so what can you actually tell me?" | State exactly what you CAN confirm (from status page/public record), name why the rest is held ("root-cause report is in legal review before publishing"), give a date it lands. This is a scoped limit, not "no comment." | Point to the postmortem's publish date, then to what's shipping now. |
| 5 | "Since BUSL blocks competing hosted services, why not just run the last Apache fork?" | Concede it straight: for someone building a competing hosted service, the fork is the right call, by name. | What BUSL still guarantees everyone else — self-host, embed, modify, unrestricted. |
| 6 | "How do you make money, and what stops you pulling the rug again?" | Real tension, say it: you're paid by enforcing the licence against large hosters — that's the incentive, not hidden. | The written guarantee: the change-date clause, in plain terms. |
| 7 | "Who should NOT use Fenwick Broker now?" (offer this even if unasked) | Name it precisely: anyone building a competing managed/hosted broker on top of it. | Everyone else — self-hosters, internal teams, embedders — unaffected, full functionality. |
| 8 | "What's next for Fenwick Broker?" | This is your landing spot — lead with the new release, concrete numbers, no unpublished dates. | This is the bridge target for 1, 2, 5, 6 — not a replacement for answering them. |

Gaps in this prep, name them going in:
- Numbers in Q1–Q3 are placeholders — fill real figures (users affected, outage duration, licence forcing constraint) before recording.
- Confirm with legal exactly which outage facts are public vs. sealed. That boundary is what makes Q4's answer honest instead of evasive — get it in writing, not memory, before you're on air.

Rehearsal, tonight, 20 minutes: have someone ask you these 8 out loud, in Ade's likely tone, no warning. Time each answer — over 90 seconds means shorten the first sentence, not the story. If the bridge comes before the concession, redo that one immediately. Stop after these 8; more rehearsal starts sounding rehearsed.