Using the developer-case-study skill's source-interview-guide to prep this — your three-question plan (how it went, happy with performance, would they recommend us) would only fill the headline/results/advice slots. That reads as a testimonial, not a case study: no before-state, no alternatives, no architecture, no cost/limitations, which is exactly the gap a technical reader spots and discounts. Here's the call set up properly.

## Before you dial in

- Skim your own side first if you have five minutes: support tickets Fairhaven filed, migration PRs/issues if any touched a shared repo, usage telemetry (when did their volume/error-rate shift). Anything you find here is a number to *confirm* on the call rather than ask cold.
- Have one person dedicated to capturing quotes verbatim — paraphrase reads as vendor copy later. If your Zoom setup can record, ask for consent in the first minute and say so out loud on the recording. If not, verbatim note-taking on the two or three best lines is the minimum.
- Confirm each attendee's exact name and title spelling before you hang up — reviewers correct this late otherwise.

## Agenda for the 45 minutes (3 attendees)

Direct implementation and numbers questions at the two backend engineers by name — in a joint call with a VP present, the hands-on voice defers unless you ask it directly, and it's the hands-on voice a reader trusts. Reserve the manager-scope and approval questions for the VP.

| Time | Topic | Ask |
|---|---|---|
| 0–3 min | Status check (gate) | Confirm this is live in production today, not still rolling out — if it's still partial, say so, it changes what you can publish. |
| 3–10 min | Before-state | What was in place before, who built it, how did it fail and how often. Draw/describe the old shape. |
| 10–15 min | Cost of before-state | Engineering time spent keeping it alive, what it blocked on the roadmap, any incident/revenue/SLA hit. What made this worth fixing *now* rather than last year. |
| 15–23 min | Alternatives | What else you evaluated, including building it yourselves — and what each alternative did better. This is the section that makes the story credible; don't skip it. |
| 23–33 min | Implementation | Walk through what you built, component by component, in what order, who worked on it, what surprised you, what you had to change around it. |
| 33–39 min | Numbers | What did the key metric read before vs. now, which dashboard/log/bill it's from, over what window, who can confirm it if we quote it. |
| 39–43 min | Cost + what's unsolved + advice to a peer | Engineer-weeks spent, parallel-running period, what broke, what you deliberately didn't move, what still doesn't work, who shouldn't copy this setup. Then: if an engineer at a similar company asked you about this over coffee, what would you tell them? |
| 43–45 min | Approval chain (to the VP) | Who signs off on naming your company, quoting these two engineers, and clearing the technical detail — and roughly how long each takes? |

That's the full ladder compressed into 45 minutes — tight, so if alternatives or implementation run long, let numbers/cost/unsolved slide to a follow-up email rather than rushing every rung shallowly. A short async follow-up beats a rushed live answer you can't quote.

## Exact questions, phrased so they produce numbers instead of compliments

Ask about specifics that already happened — never "was it much faster," always "what did it read before and what does it read now."

**Before-state**
- What was running before this, and who built it?
- How did it fail, and how often? Who got paged, and what did they do about it?
- How much engineering time went into keeping the old thing alive? Did it ever cost you an incident, a customer, or an SLA?
- What made this worth fixing now rather than six months ago?

**Alternatives**
- What else did you evaluate, including building it yourselves?
- Why did each option lose — what did it do better than what you picked?
- What almost made you choose differently?

**Implementation**
- Walk me through what you built, piece by piece.
- What order did you build it in, and how long did each phase take?
- What surprised you, good or bad?
- What did you have to change in the systems around it?

**Numbers**
- What did the key metric read before, and what does it read now?
- Which dashboard, log, or bill is that from?
- Over what window — and is it still moving or has it settled?
- Who on your team could confirm that number if a reader asked?

**Cost and limitations**
- How long did the migration take, in engineer-weeks?
- Did you run both systems in parallel — for how long, and what did that cost you?
- What broke during rollout?
- What did you deliberately leave on the old system, and why?
- What still doesn't work the way you want? Who should *not* copy this setup?

**Advice to a peer** (your "would they recommend us" question — this is the sharper version of it)
- If an engineer at a similar company asked you about this over a coffee, what would you actually tell them?
- What do you wish someone had told you before you started?

**To the VP specifically**
- What did this change about how the team operates?
- How did you justify the time/spend internally?
- What would've happened if you'd done nothing?
- Who signs off on naming Fairhaven and quoting [the two engineers] publicly — you, comms, security/legal? Roughly how long does that take?

## Right after the call

- Write the evidence ledger the same day — one line per number: claim, before/after value, instrument, window, who can re-derive it. Do this while it's fresh; it's much harder to reconstruct from notes a week later.
- Send a short thank-you that restates every number you captured and asks them to correct anything wrong — cheaper to fix here than in a legal review later.
- Ask for their architecture diagram if one exists internally — redrawing from memory is where most technical inaccuracies creep in.
- Note whether "production, not pilot" actually got confirmed — if it didn't, that's the one gate that can still kill the story regardless of how good the rest sounds.