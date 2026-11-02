## Where to start: don't start with the constitutional assembly

The instinct — "we need real governance, let's write a charter and elect a committee" — is right long-term, but doing it first is how these processes fail. Three competing Matrix rooms means you don't have one community with one story yet; you have three factions who each think they know what happened. A charter drafted or ratified before that's resolved doesn't settle the dispute — it becomes a fourth thing to fight about, and whoever's the most organized *right now* (often whichever faction is angriest) writes the rules that bind everyone else.

Sequence matters. Rough order:

1. **Stop the bleeding** (this week)
2. **Establish facts and hear grievances** (2–4 weeks)
3. **Draft governance options, not a finished charter** (4–8 weeks)
4. **Public comment + ratification vote**
5. **First election under the new rules**

December for a steering-committee election is achievable if you start now, but only if the charter isn't the *first* thing — it's the *product* of the first three phases, not a shortcut past them.

---

## Phase 0: Stop the bleeding (this week)

- **Name an interim moderation setup immediately**, even a bad one — two or three trusted maintainers, explicitly labeled "interim, until governance process concludes." A vacuum in the mod seat is what's letting three Matrix rooms compete for the "real" conversation.
- **Pick one canonical channel** for the governance discussion itself (a GitHub Discussions category or a single pinned Matrix room). Announce it everywhere else. Don't shut the others down by force — just stop treating them as legitimate venues for decisions.
- **Publish a short, factual timeline** of what happened (resignation, departures, the sponsor thread) with no spin. Ambiguity is what's fueling three competing narratives. You don't need to litigate who was right — you need one agreed set of facts about *what occurred*.
- **Say publicly that a governance process is starting**, with a rough timeline, and that no permanent decisions (especially about the sponsor) get made until it concludes. This alone de-escalates a lot, because people stop fighting over who has the temporary power to decide.

---

## Phase 1: Fact-finding before drafting (2–4 weeks)

Before anyone writes a charter, find out what the actual disagreement is. "Corporate sponsor" is the trigger, but it's rarely the whole disease. Common underlying splits in projects that reach this point:

- Was the objection to *this sponsor's conduct*, or to *having sponsors at all*?
- Was the resignation about the sponsor, or about how moderation decisions get made generally (unilateral vs. consulted)?
- Do the two maintainers who left in solidarity agree with each other on what "real governance" means, or did they just agree the status quo was broken?

Get this by:
- **A neutral person runs 1:1s or a written call-for-input** with the resigned lead, the two who left, active maintainers, and a few long-time non-maintainer contributors. Neutral means not a current decision-maker and ideally not someone who took a public side already.
- If nobody in the project is neutral enough, borrow one — ask a maintainer from an adjacent project, or use a paid facilitator for a few hours. This is the single highest-leverage $ you can spend here.
- Write up themes, not attributions ("concerns about sponsor influence on moderation," "concerns about decisions being made by one person," "concerns about transparency") — not "X said, Y said."

This step is what a December-elected committee actually needs to exist for. Skip it and you'll elect people to fix a problem nobody agreed on the shape of.

---

## Phase 2: Draft *options*, not a finished charter

Have a small, visibly diverse drafting group (not just whoever's still standing) produce **2–3 concrete governance models**, not a single take-it-or-leave-it document. Ground them in projects that have actually been through this transition rather than designing from scratch:

- **Single steering council, term-limited, elected by contributors** (Django Software Foundation board model, or Rust's team-based leadership council) — good if the core issue was "too much power in one person."
- **BDFL/lead + advisory council with defined veto points** — lighter-weight, good if the project is small and the real ask is "check the lead's power on specific decisions" rather than replace them entirely.
- **Foundation-style separation of trademark/sponsor relationships from technical/moderation decisions** (this is the CNCF/Python-Software-Foundation pattern) — worth strongly considering given *your specific trigger was a sponsor dispute*. Moving sponsor relationships and funding into a body that is structurally separate from day-to-day moderation is often the actual fix, more than who sits on a committee.

For each option, spell out concretely: who can vote, how members are chosen and removed, how conflicts of interest (including sponsor relationships) are declared and recused, and what decisions require the committee vs. what stays with individual maintainers.

Publish this as a discussion document with an explicit comment period (2–3 weeks). This is also where you surface and defuse objections from the three-Matrix-rooms factions *before* a vote, not after.

---

## Phase 3 & 4: Ratify, then elect

- **Ratification vote on the governance model itself** (not the charter's every clause — the structure) before electing anyone into it. Voting eligibility should be defined narrowly and stated up front — typically "contributors with N merged commits or N months of activity as of [date before the crisis started]," so the electorate isn't gerrymandered by people who just showed up because of the drama.
- **Then run the steering committee election** under the ratified rules. Use a simple, auditable method (single transferable vote or approval voting over a published candidate list) — not informal "who has the most support in the loudest room."
- Publish the full charter text only after both the structure vote and the first election are done — it should describe what was actually ratified, not what a small group hoped would be ratified.

---

## The sponsor clause specifically

Since this is what lit the fire, don't leave it implicit. The charter needs an explicit, named answer to:

- Who can accept sponsorship on the project's behalf, and what's disclosed publicly when they do (amount ranges are fine, opacity is not).
- Whether sponsors get any input on moderation, roadmap, or personnel decisions — the answer most projects converge on is **no**, full stop, and that sentence being written down explicitly is often the single line that would have prevented this blow-up.
- A recusal rule for any steering committee member who is employed by or funded by a sponsor, on votes involving that sponsor.

## Pitfalls to watch for

- **A drafting group that's just "whoever's left"** will look like the winning faction writing the rules — even if their intentions are good. Actively invite at least one person from each of the three rooms, including people who were critical of the resigned lead, into fact-finding and drafting.
- **Rushing to December because it's a round deadline.** If fact-finding surfaces something bigger than the sponsor dispute (e.g., a long-standing power concentration issue), a rushed charter will re-litigate this again in six months. Better a real charter in February than a contested one in December.
- **Treating "elect a committee" as the fix** without separating sponsor/funding decisions structurally — you can elect a committee and still have this exact fight again next time a sponsor deal comes up, if the charter doesn't actually change who has authority over that specific decision.

If you want, I can help draft the Phase-0 public announcement, the fact-finding call-for-input, or a first-draft options document once you've picked which governance models to compare.