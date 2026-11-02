**Verdict: mostly workable. Two parts break at your numbers — fix before launch.**

## What breaks

| Gate | Status | Why |
|---|---|---|
| Candidate pool (need 2-3x cohort) | ❌ | 25 champions from pool of 30 = 1.2x. Not selection, near-universal. Other 5 will notice exact exclusion in a tight 30-person group. |
| Owner hours | ❌ | Skill's own rule of thumb: 1-2 hrs/champion/month for high-touch = 25-50 hrs/month. You have 3. Off by 10-15x. Design must be near-zero-touch, not "high-touch, lightened." |
| Something only you can give | ✅ | You're the only maintainer — roadmap/RFC input and repo permissions are real, free perks. |
| Feedback capacity | ✅ | You are the product decision-maker. Just block time to actually read it. |
| Conduct baseline | ⚠️ | Not mentioned. Need one paragraph minimum before handing out a title that implies authority. |
| Budget for hoodies | ❌ | Math below. $480/year run rate, hoodies for 25 cost ~$1,000+. |

Both self-set thresholds (2-3x pool, 1-2hrs/champion) — no published benchmark exists for solo-maintainer OSS scale, these are this skill's own defaults, sized for vendor programs. Flagging the gap size matters more than the exact threshold.

## Fix 1 — stop targeting a headcount

Don't pre-commit to "25." Publish criteria (below), induct whoever clears it. Could land at 18, could land at 28. Removes the "why not me" problem for whoever's left out — they weren't cut, they didn't clear a stated bar yet.

## Fix 2 — redesign for 3 hrs/month, not "lightened vendor program"

Skip: application intake forms, scoring committees, monthly calls, quarterly cadence, points ledger (no engineering time — delete this option outright). Use **award/recognition shape**: you already know these 30 people from Discussions, so selection is you picking against published criteria, not a review process. One annual pass, not quarterly.

## Fix 3 — hoodie math

$40/month = $480/year gross (check: is that net of any hosting/domain costs, or does something else already eat it?). A print-on-demand hoodie (Printful/Printify, so you never touch shipping) lands around $28-33 base + $6-25 shipping depending on country — call it $40-55 landed per person for a global OSS crowd. 25 people ≈ **$1,000-1,375**. That's 2-3x your annual budget on one line item.

Options, pick one:
1. Universal cheap token now (sticker/pin, ~$3-5 landed, ~$100 total for 25) + badge + access perk. Hoodie later as opt-in stretch goal, openly tied to a donation milestone.
2. Hoodies for a smaller first batch (say 10), badge+access for all 25, expand hoodie batch next year.
3. Separate, explicitly-labeled one-time "Champions swag" donation drive — don't fund it from the ongoing $40/month operating line.

Recommend 1. Never promise a perk before checking the actual bank balance can cover it — a partially-delivered hoodie promise costs more goodwill than no hoodie ever did.

## Charter — libcaldera Champions

1. **Purpose** — self-set, pick one: recommend *retaining and recognising the people already doing unpaid support work* (this fits "genuinely great regulars" better than feedback or reach — you're not chasing growth, you're keeping who you have).
2. **Room** — GitHub Discussions regulars, no orbit newcomers. No region/language targeting needed at this scale.
3. **Archetype** — award/recognition (maintainer-selected against published criteria, not open application). Chosen because: no eng time (kills points ledger), 3hrs/month (kills application-cohort review load), you personally already know every candidate (skill's own condition for promoting this shape).
4. **Size** — not fixed. Induct everyone clearing 2-of-5 below. Self-set expectation: likely 15-25.
5. **Criteria** — any two of:
   - Answers other people's questions in Discussions/Issues, sustained 6+ months (self-set floor, shorter than CNCF's 12 — smaller project, shorter track record still meaningful).
   - Filed reproducible, high-quality bug reports (recurrence-rule edge cases, timezone bugs) that led to a fix.
   - Helped a newcomer land their first issue report or PR.
   - Created non-paywalled content about libcaldera.
   - Direct code contribution, merged.
   Anti-signals: reach with no engagement depth, activity starting the week you announce this, condescension to beginners, asking for the title as payment.
6. **Obligations** — follow conduct norms, be constructive with newcomers, give honest feedback including criticism. May not: speak for the project on licensing/legal, promise features or timelines, act as an obligated support SLA.
7. **Perks**, in order:
   - **Access** (free, one beat serves everyone): private Discussions category where you preview RFCs/breaking changes before release and ask for input.
   - **Platform/repo permission** (free, reduces your own load): "Triage" role — label issues, close duplicates, flag things for you. Genuine value to them, genuine time saved for you.
   - **Status**: dated badge — a `CHAMPIONS.md` list + "Champion 2026" next to their name, credit in release notes when their input shaped something.
   - **Swag**: sticker/pin for all now; hoodie per Fix 3 above.
8. **Term** — 12 months. Renewed against same criteria at term end, not past reputation. 1 month notice (skill's stated floor — quarter is generous but your hours don't support running that). Pause available, no reason required.
9. **Exit** — no visible activity for 9-12 months → not renewed, moved to alumni. Conduct removal decided by you (no moderation team exists — name this as a real single-point-of-failure, not hidden). Alumni keep dated title, get asked to help nominate next cohort (this offloads your work next year for free).
10. **Compliance** — light at this scale: no cash value on any perk, gift limits unlikely to bite (hoodie/sticker are low-value), no formal NDA needed (ask nicely: don't screenshot the private channel pre-release), no employer-approval gate needed for a non-commercial OSS project.
11. **Operations** — owner: you, 3 hrs/month. Budget: per Fix 3. Beats: one private-channel post per RFC (as needed), one annual renewal pass, one annual public recognition post. No recurring call.
12. **Bar** (self-set, all annual not quarterly — your cadence, not the skill's vendor default): active share ≥50%, renewal acceptance ≥70%, you reply to a champion within 10 business days, ≥1 decision/year traceable to champion input. Kill criteria: if your own hours drop below ~1/month with no replacement, freeze new intake and let the cohort run to term end rather than announce a shutdown.

## Public page draft

> **libcaldera Champions**
> Recognising the people who already make this project work — answering questions, filing sharp bug reports, helping newcomers, writing about libcaldera.
>
> **Criteria** (any two, sustained, last 6+ months): answering others' questions in Discussions/Issues · reproducible bug reports that led to a fix · helping a newcomer land their first contribution · non-paywalled content about libcaldera · merged code contributions.
> Not counted: activity that starts the week nominations open, reach without depth, condescension to beginners.
>
> **What it isn't**: not a job. No quotas, no obligation to answer every question, no speaking for the project on licensing.
>
> **What you get**: early input on RFCs and breaking changes in a private channel, Triage permissions on the repo, a dated Champion badge and listing, a small thank-you gift.
>
> **Term**: 12 months, renewed against the same criteria. No longer active for 9-12 months → moved to Alumni, title kept, dated.
>
> **How it starts**: maintainer-selected from known Discussions activity — no open application yet given project size.

Next: decide Fix 1's criteria wording and Fix 3's swag tier — once picked, I can draft your announcement post.