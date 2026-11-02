Audit of Rivetline Q4 against devrel-content-calendar pass thresholds. Verdict: topics mostly fine. Plan fails on process — owners, slack, anchor support. Plus one content bug you may not have spotted.

## What's wrong, damage order

1. **Owner = "content team" on every row. Threshold requires named owner AND named reviewer, person not team.** "Content team" means nobody. Every piece stalls in review with no name to chase. Worst failure, cheapest fix.
2. **13/13 weeks filled = 100% capacity committed. Threshold: committed slots ≤ 80%, rest named slack.** "No gaps" reads as discipline, is actually the failure mode: first slip (v6 delay, Acme approval lag, December sick week) eats a slot and everything after slides. 80% of 13 weeks = 10 committed, 3 slack.
3. **v6 GA W7 — your only hard date — sits alone. Threshold: every anchor gets preparation slot AND follow-up slot.** No prep before (embargoed draft, docs, migration guide must start ~W5), no follow-up after (W8 is unrelated "hygiene tips"). Launch week is the one week audience already looks — unsupported anchor wastes it.
4. **One surface. Threshold: ≥ 3 surfaces, ≥ 2 journey stages.** Every row reads blog post. "Flag hygiene tips" is docs material. v6 GA needs changelog + release notes, not only blog. Acme spotlight = case study page for approvers, not blog.
5. **No evidence, no shelf-life labels. Threshold: every demand slot carries evidence, every bet a hypothesis.** "5 things you didn't know about feature flags" = exact no-evidence listicle anti-pattern from skill's negative example. "Future of progressive delivery" = bet with no stated hypothesis.

## Also verify

- **Version mismatch: W1 announces "Rivetline 4.0", W7 GAs v6.** Two major versions in one quarter, and 4.0 has no anchor behind it — you said v6 is the only hard date. Likely stale template row. If 4.0 already shipped, W1 announces nothing.
- **W12-W13 land mid/late December.** Holiday dead zone: reviewers gone, readers gone. "What's coming in 2027" needs product roadmap sign-off — hardest review to get, worst week to ask. Skill's worked example: W13 holiday gap, plan nothing.
- **External review chains uncounted.** W9 Acme spotlight runs on Acme's approval chain — weeks of latency. W10 pricing carries founder/legal veto, exercised late. W6 CNCF announcement runs on CNCF's own comms rules.
- **Evergreen = minority once anything is cut.** Quarter is launch-dominated (GA + CNCF + pricing + two year-end pieces). Legitimate shape — but declare the trade-off, and know the failure mode: v6 slips, takes quarter with it. Slack weeks are your only insurance.
- **Capacity never sized in review passes.** Count engineer review load W6-W10: CNCF note + v6 piece + v6 follow-up = 3 technical reviews in 5 weeks. If one engineer reviews, that fortnight binds. I could not verify team size — check this number yourself.

## Minimum changes, no re-planning

1. **Names.** Every row: named owner + named reviewer. W9 reviewer = Acme's approver. W10 reviewer = founder. ~30 min.
2. **Blank 3 weeks as named slack:** W13 (holiday), W2 (cut — fails novelty filter, no evidence), W5 or W11 (defer — pick W11 if adoption is the funding driver, W5 if employer branding matters). Name who may spend slack. 10/13 = 77%.
3. **Repurpose W1 → v6 prep slot:** embargoed v6 draft + migration guide started. Kills phantom 4.0, gives anchor its prep.
4. **Retitle W8 → v6 follow-up, docs surface:** "Upgrading to v6" or hygiene-for-v6 guide. Gives anchor follow-up, adds second surface.
5. **Add 3 columns:** surface, shelf-life (evergreen/timely), one-line evidence or hypothesis. Label W7 changelog+blog, W9 case study.

Whole edit ≈ 1 hour in spreadsheet.

## Validation after changes

- Owner + reviewer: pass.
- Slack 10/13 = 77%: pass.
- v6 prep (W1) + follow-up (W8): pass.
- Surfaces: blog, docs, changelog, case study = 4: pass. Journey stages: discover (announcements) + adopt (W8 docs): pass.
- Evergreen minority: fails baseline — passes only under declared launch-dominated quarter. Declare it in doc.
- Announcement count W6/W7/W10/W12 ≈ 4 of 10: no cap was ever agreed. Agree one; 3 suggested.
- Remaining risk: v6 slip consumes W7+W8. Slack absorbs one such hit, not two.

Next: email Acme contact for spotlight approval — 2 minutes, W9 is 9 weeks out and their review chain eats most of it.