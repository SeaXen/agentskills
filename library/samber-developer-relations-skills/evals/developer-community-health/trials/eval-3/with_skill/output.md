## Review: Pelago Q3 community sentiment numbers

Short version: neither number is QBR-ready as stated. The Discord score shouldn't go in at all. The survey score has the right shape but the wrong sign, and the sample is too small to report as a score.

### 1. Discord sentiment: 78% positive → don't use it

This is the textbook failure mode for community sentiment measurement: **sentiment inferred from a text classifier instead of asked directly.** Developer chat is full of blunt bug reports, sarcasm, and dry humour — automated scoring reliably reads "this is broken again" as anger and "lol nice" as positive, in both directions that don't track how people actually feel about the community. There's no published or practitioner instrument anywhere in this space that runs sentiment through a classifier; every one of them (CHAOSS Recommendability, the pulse survey below) asks people, then optionally checks whether their behaviour agrees.

Two more problems even if you set that aside:

- **No baseline.** 78% against what? A single-quarter number with nothing to compare it to fails the "so what" test — if it had come back 65% or 90%, would anything in the QBR read differently? Right now, no.
- **It's the negative example, almost verbatim.** "Discord sentiment: 78% positive (auto-analysis)" is the literal example of what not to publish in this framework — the diagnosis there applies word for word: no survey behind the number, no owner, no threshold, nothing anyone can act on.

**What to do instead:** pull it from the QBR. If you want a real sentiment number for Discord, run the two-item pulse survey (recommendability + "what's most frustrating") and report *that* — you already have the raw material, see below, you just fielded it as a one-off instead of on the community itself. Keep the classifier, if at all, only as a triage tool for support routing — never as a health metric.

### 2. NPS from the recommend survey: -22 → this is actually +22

Two separate errors stacked here, and they partially mask each other.

**Sign error.** NPS is **% promoters − % detractors**, not the other way round. (This mistake is common enough that CHAOSS's own published Recommendability page states the subtraction backwards — so you're in good company, but it's still backwards.) Recomputing:

- Promoters: 4/9 = 44.4%
- Detractors: 2/9 = 22.2%
- Passives: 3/9 = 33.3%
- **NPS = 44.4 − 22.2 = +22**

That's not a small correction — it flips the finding. "-22" reads as a community actively souring on you. "+22" reads as net-positive, more promoters than detractors. Whatever narrative you were about to write around the negative number is the opposite of what the data says.

**Sample size.** At n=9, don't report this as a score at all — that only holds once you clear roughly 30 responses. Below that, a single-digit sample swings a "score" by 11 points per person who answers differently (this one person moving from detractor to passive is a 22-to-33 to 33-to-11-point swing on its own). The honest way to present this in the QBR: *"4 promoters, 3 passives, 2 detractors, out of 9 responses"* — raw counts with dates, not a headline number.

**Response rate.** 9 responses out of a 2,600-member Discord is roughly 0.35%. That's not a random sample of the community — it's whoever happened to see a one-off ask and cared enough to answer, which skews toward either your most engaged fans or your most frustrated users (often both, which is part of why it landed near-neutral). Flag that self-selection risk next to the number rather than presenting it as "how the community feels."

### What to actually put in the QBR this quarter

| Metric | This quarter | Baseline | Note |
|---|---|---|---|
| Discord automated sentiment | *omit* | — | Not a valid instrument for this pillar; see above |
| Recommendability (survey) | 4 promoters / 3 passives / 2 detractors (n=9, ~0.35% response rate) | baselining | Too few responses for a scored NPS; report as raw counts with the caveat stated |

Both rows are honestly labeled "baselining" — you have one reading, and the framework's own minimum is three periods before a threshold means anything.

### Fixing it going forward

1. **Field the pulse survey on a cadence, not as a one-off.** Two items, quarterly: the recommend question above, plus "what's the most frustrating thing about participating here?" (free text, optional). Send to a stable population definition each wave (e.g., "members active in the last 90 days") — otherwise a swing in the score just means you sampled different people, not that sentiment moved.
2. **Corroborate the survey with behaviour**, not a classifier: responsiveness (median time to first human response, % of questions with zero replies) and contribution/adoption signals from the same period. If the survey says +22 but response times are also trending down, that agreement is what makes either number credible. If they disagree, the survey probably reached a different slice of the community than the one doing the day-to-day answering.
3. **Decide whether Pelago's community is B2B or individual-adoption before reading the next wave.** If Discord members mostly represent customer accounts rather than individuals, the unit that matters is "accounts with at least one active, positive member," not raw response counts — worth settling before you build a repeatable sheet around this.
4. **Get the response rate up or stop scoring it as NPS.** Either survey a random sample large enough to clear ~30 responses, or keep reporting raw counts with the response-rate caveat until it does. Don't let a low-n score quietly become "the number" the QBR tracks quarter over quarter — it will whipsay on sample noise alone.
5. **Never publish this below the aggregate.** With 2 detractors in a 9-person sample, any further slicing (by channel, by tenure, by anything) risks identifying who they are. Keep it aggregate-only, always.