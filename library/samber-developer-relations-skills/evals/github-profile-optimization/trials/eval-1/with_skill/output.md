## Correction before the plan

⚠️ Kill the "78% of recruiters check GitHub" number. Unsourced vendor-blog stat, no real methodology, on the explicit refuse-list of the skill I used. Do not repeat it, do not plan around it.

Real published data (only study with disclosed methodology, HackerRank 2018, 39k+ devs / 7k+ employers): portfolio weight concentrates at **small, founder-led companies**. Large employers screen mostly by resume first. Datadog, Stripe, Cloudflare are all large-employer hiring loops. For that target, GitHub is a **verification** surface, not a decision surface: an evaluator who's already interested checks it doesn't contradict your resume. It rarely creates the interview by itself. No study measures a rewrite producing more interviews — nobody promises you that, including me.

Practical result: this work does not need two full weekends. It needs **~9-10 focused hours**. Recommend running the plan below across one weekend (or spread it), and spending your second weekend on resume + interview prep instead — higher leverage for these three specific targets. You asked for both weekends planned on the profile though, so full plan is below; cut it short if you want the time back.

**Couldn't audit your account live** — no network access in this run, so no automated scorecard with real numbers. Step 0 below has you run the audit yourself; everything after assumes standard gaps (stale bio, weak positioning, pins unset or arbitrary) until you check.

**Assumptions I'm making** (correct me if wrong, but plan works either way): personal profile, goal = credibility for backend hiring loops, audience = recruiter first pass + engineer on your loop, you own the page, no legal/marketing sign-off needed.

---

## Weekend 1 — facts, kill false claims, positioning, pins (~5.5 hrs)

**1. Run the real audit (20 min).** From the skill folder:
```
GITHUB_TOKEN=<a personal access token> python3 scripts/profile-audit.py priya-nandakumar
```
Setting `GITHUB_TOKEN` matters — without it, pinned items don't show at all. This gives you real numbers for everything below: bio length, dead links, widget list, which repos show up if pins are unset.

**2. Kill false claims first (30-60 min).** Highest return per hour of anything here, ties with #3:
- Dead links (any 404 costs a blocking check).
- "Currently building X" where X is stale or archived.
- Old employer/role if `company` field is outdated.

**3. Fix render prerequisites (10 min).** All four must hold or the README shows nothing, silently:
- Repo name exactly `priya-nandakumar`.
- Repo public.
- `README.md` at repo root.
- File not empty.

**4. Toggle private contributions on (2 min).** Settings → Profile → **enable "include private contributions"**. Six years employed means most real work is private — your public graph likely looks dead and this is a setting fix, not new work. Do this before judging the graph at all.

**5. Draft 3 positioning-sentence candidates (30-45 min), different axes:**
- What you build: "I build [backend systems] for [domain], focused on [queueing / data pipelines / API reliability]."
- Problem removed: "I keep [system] from breaking under [load type] for teams running [context]."
- What reader stops doing: "Work touching this and you stop [firefighting outages / hand-rolling retries / debugging races]."

Test each: could a competitor paste it unchanged? If yes, rewrite it. Pick one, it propagates into your bio too.

**6. Pick and describe 6 pins (45-60 min).** For hiring/credibility, order by judgement shown, not stars:
1. Strongest original project, clearest outcome line ("handles N req/day", "used by X").
2. Second-strongest, different facet of your skillset than #1.
3. Something showing production judgement (an operational tool, not a toy).
4. A repo where tests/CI/docs quality is visible — Datadog and Cloudflare specifically hire for this discipline.
5-6. Only fill if you genuinely have 5-6 non-fork, non-archived, non-empty repos worth showing. **Fewer honest pins beats padding with forks you didn't substantially change.**

Every pin needs a description + topics before it counts — bare pins waste the slot.

---

## Weekend 2 — rebuild README, verify, ship (~4.5 hrs)

**7. Write the README (90 min).** Use this order (matches how a hiring-context reader evaluates you):
1. One sentence — your chosen positioning line.
2. 2-3 projects, each: `name — what it does — outcome`. No stars, they're already shown elsewhere.
3. **Contributions to other people's projects, linked to actual merged PRs.** This is your highest-leverage move specifically — for a credibility/hiring goal, merged PRs elsewhere outrank everything else on this page, and they're the one signal a reviewer can actually check. Find 2-3 and link them.
4. Contact route (email or LinkedIn — one line).

Skip stats widgets, streak cards, trophy rows entirely. They read as noise to the senior engineers on your loop and can't see your private work anyway — don't trade credibility for decoration.

**8. Humanize the prose (20 min).** Run it through a humanizer pass — generated-sounding copy undercuts the exact trust you're building.

**9. Re-score (20 min).** Self-check against these 4 blocking gates — all must pass:
- README renders.
- A stranger can name what you do from the first screen.
- Every claim on the page is true today.
- A next step exists (link to a repo, contact, etc).

Plus 8 scored checks (positioning, pins-as-editorial, pin descriptions, reading order, decoration ≤3 items, accessibility/alt-text, freshness, route to real destination) — 2 pts each, ship at 13/16.

**10. Cold-reader test (20 min).** Hand the URL to a friend, or open a fresh chat with no context. 45 seconds, then ask: What do you do? Which project first, and why? Is this active? What do I do next? 4/4 correct = pass.

**11. Ship (5 min).** Owner = you. Review trigger = next job search or role change — not a calendar reminder nobody honors.

---

## Do not do these (explicitly on the refuse list)

- No star buying, no backdated commits, no daily filler commits to "fill the graph." Reviewers who follow this space already discount all three, and they're checkable.
- No streak/trophy/visitor-counter widgets. Cost credibility with the exact senior audience you're trying to reach.
- Don't promise yourself interviews from this. Promise yourself a page that stops contradicting your resume — that's what this delivers.

**Next action:** run the audit command in step 1 this weekend, before anything else.