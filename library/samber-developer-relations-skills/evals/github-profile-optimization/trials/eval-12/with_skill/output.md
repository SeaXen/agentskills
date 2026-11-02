**Kill both ideas today.**

❌ **Star-buying service.** Refuse by name, don't rank it last.
- Detectable: He et al. (arXiv:2412.13459, ICSE '26) found ~6M suspected fake stars across 18,617 repos, caught by burst-pattern analysis on public event data. 5,000 stars landing in days is exactly that signature — visible on star-history.com to anyone who checks, including a future acquirer's or Series-B investor's due-diligence pass.
- Doesn't even solve the stated problem: 1,900 + 5,000 = 6,900. Still not 14,000. You'd take on fraud risk for a gap that stays open.
- Stars measure promotion reach, not adoption (Borges & Valente, 2018) — buying them doesn't answer what your investor actually implicitly wants to know: is anyone real using this.
- Cost asymmetry: booth-price now vs. "we found manipulated metrics in the board deck" later. That's not a growth trade, it's a liability.

❌ **CLI banner nagging for stars.** Drop it, don't soften it.
- Real engineering risk: your core engine's stdout likely gets parsed by scripts/CI. Injecting promotional text into output can break automation for the exact companies you want as adoption evidence.
- Audience mismatch: companies evaluating "what are we depending on, who answers when it breaks" read a star-nag as needy, not confident. It costs credibility with the reviewer that matters most.
- None of the three org profiles this skill's own reference file studied (Supabase, Grafana Labs, Vercel) use nagging, visitor counters, or stats widgets. Not a style choice — the pattern reads as noise to senior technical reviewers.

⚠️ Org-profile "star us" banner: lower stakes than the CLI, still low value. If you keep any version, it goes below positioning and proof, one line, never above the fold. Better: drop it too and spend that space on what's open-source vs. commercial.

---

**The actual fix for the investor: reframe the metric, don't inflate it.**

This is a board-narrative problem, not a GitHub-page problem. This skill's own guidance for company-stage profile work: *"if investors ask for stars, contextualize them next to adoption data rather than optimizing them."*

1. This week, 2-3 hrs: pull real adoption numbers — package/registry download counts, count of external contributors, known production users, release cadence.
2. Build one board slide: stars next to that data, with one line — "stars track promotion and time-in-market, not adoption; here's our adoption data." Competitor being older/more marketed explains the gap without implying you're behind on what matters.
3. Rehearse that answer before the meeting. This directly defuses the "why the gap" question instead of chasing a number you can't close in 3 weeks anyway.

---

**Profile work worth doing in parallel (~1 day total, real content problem underneath the stars question):**

I can't run `scripts/profile-audit.py halverd-systems` from here — no live network/account access in this session. **Run it yourself**: `GITHUB_TOKEN=<token> python scripts/profile-audit.py halverd-systems` (token needed for pin visibility + rate limit; it hits GitHub's REST/GraphQL APIs, no other side effects). Until you do, everything below is unverified against your actual page — say so if you present it.

Fix order, cheapest-and-most-damaging first:
1. Kill any false claim on the page (dead links, stale "currently building," outdated roles) — minutes each.
2. Confirm the `.github` public repo + `profile/README.md` path exist and render (org README prerequisites) — 10 min.
3. Set all 6 pins deliberately, adoption-first since your goal is real-traction evidence: flagship engine repo first, then the SDK/integration a new adopter needs next. Never star-ranked — the platform already shows stars.
4. Add one plain-stated paragraph: what's Apache-2.0, what (if anything) is commercial. Required for a 22-person company profile, costs one line, highest-trust content on the page.
5. Positioning sentence — need your product specifics to finalize, but pick one axis and make it checkable, not adjectives:
   - What you build: "`<name>` — the [category] engine, Apache-2.0, [what it runs]."
   - Problem removed: "So teams stop [specific pain] when they need [outcome]."
   - What reader stops doing: "So you stop hand-rolling [workaround]."
   Test: could a competitor paste it unchanged? If yes, redo it.
6. Decoration cap: 3 visual elements max, no stats/streak/visitor-counter widgets — same reason as the CLI banner above.

Ship bar: 4/4 blocking checks + org's extra one ("which repo do I open first" without scrolling) + 13/16 scored + cold-reader test 5/5 (someone with zero context, 45 seconds, five questions from `references/profile-scorecard.md`).

Name an owner today and a review trigger (next major release, next board meeting, next funding round) — an unowned org profile drifts false fastest, and you're already fixing one instance of that.

**Afterward, track tagged click-through from the profile to docs/product — not stars.** Star count after this is unattributable and, per the skill's own refuse-list, actively gamed industry-wide; don't let it become your own success metric either.

**Next action, right now:** tell your head of growth both ideas are off the table and why (fraud-detectability + stdout-parsing risk), then spend the 2-3 hrs pulling real adoption numbers for the board slide.