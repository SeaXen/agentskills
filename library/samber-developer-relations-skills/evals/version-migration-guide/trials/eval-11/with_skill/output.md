**Next action:** start recording per-major npm downloads weekly today. Nothing else on the dashboard can be backfilled, and you are already at day 42.

I read the skill and its references (`validation-and-adoption-metrics.md`, `deprecation-timeline-patterns.md`) and applied them to this case. I skipped the interview. I'm assuming the open-source/self-serve audience, because the CLI is open source and the deadline is a support end date, not a contract. The assumptions are listed below so you can correct them.

## 1. Assumptions and open questions

| # | Assumption | If wrong |
|---|---|---|
| 1 | Self-serve users who upgrade when they choose to | Contractual customers need account-level stragglers instead (see below) |
| 2 | v3 shipped without an interim v2 release that emits deprecation warnings | If v2 did warn, add the warning-telemetry row, which is the best leading indicator |
| 3 | The CLI sends no version telemetry today | If it does, that becomes the primary source and npm becomes a cross-check |
| 4 | A migration guide exists, or is being written, at a stable URL | Without one, the docs rows below measure nothing |
| 5 | Nettlefold keeps CI/CD pipelines and Docker images that pin versions | Pinned pipelines inflate v2 download counts; see the caveat on npm |

Questions only you can answer:
- Did v2→v3 have a predecessor curve (v1→v2)? Without one you have no baseline, so the first 90 days become the baseline.
- Who owns the dashboard after launch? Without a named owner, the telemetry join below will not get built.
- What does "working" mean to leadership? Agree on this before the first chart goes out (see section 4).

## 2. The dashboard

Tier 1 holds the headline. Tiers 2 and 3 explain why the headline moves. Tier 4 is explicitly not proof.

### Tier 1: the adoption curve (the only number that says "working")

| Panel | Definition | Source | Cadence |
|---|---|---|---|
| **v3 share of downloads** | v3 downloads ÷ all downloads, weekly | npm per-version stats | Weekly |
| **v2 absolute downloads** | Weekly v2 downloads, not share | npm | Weekly |
| **Curve vs. the previous major** | Share at day 30 / 60 / 90 against the v1→v2 curve | npm history, if you have it | Day 30 / 60 / 90 |
| **Active installs on v3** | Share of active CLI installs on v3, not downloads | CLI version ping (see section 3) | Weekly, once built |

Show v2 in absolute numbers next to the share. Share can rise only because v1 and new installs grow, while v2 usage stays flat. Leadership will ask about that.

**Caveat on npm.** Downloads are not installs. A single CI pipeline pinned to v2 can generate thousands of downloads a day. Mirrors and bots add more. Label the panel "downloads", never "users". At about 200k installs, one large pinned pipeline can distort the share noticeably.

npm exposes per-version counts through its downloads API, but as far as I know only for a trailing window. Check the current endpoint, then snapshot weekly into your own store. This is why starting now matters.

### Tier 2: the deprecation-warning signal (the leading indicator)

- **Distinct installs seeing a v2 deprecation warning, per week**, trending toward zero before the removal date. This needs the version ping from section 3, or a staged v2 release that emits warnings.
- **Warning level per deprecated item**, as a table with a removal version and a replacement for every row. A row with no replacement is an unfinished deprecation.
- **Rule:** if the warning count is flat one month before removal, the date is wrong or the guide is not reaching people.

### Tier 3: friction (where the migration is breaking)

| Panel | Source | What it tells you |
|---|---|---|
| **Tickets per 1,000 upgrades quoting an upgrade error** | Zendesk, using a tag or macro on every v3-upgrade ticket. Denominator is v3 weekly downloads. | Which breaking change generates the most tickets. Rewrite that entry first. |
| **Top 5 error strings in tickets** | Zendesk | Entries to add to the troubleshooting section, keyed on the literal error text |
| **Guide page: views, scroll depth, exit rate** | Plausible, with custom events | Whether the guide is found and where readers drop off |
| **In-page and docs search queries on the guide** | Plausible custom event, or the docs search backend | Each query names an entry you failed to write |
| **Exits from the guide to the support channel** | Plausible outbound-link event | A signal of a missing or unfindable entry |
| **Rollbacks and pinning** | npm: v2 patch downloads spiking after v3 days | Abandonment, which a share chart hides |

Plausible tracks pageviews by path and is cookie-free, so it can't connect a docs visit to an upgrade. Treat these as directional, not as outcomes.

### Tier 4: stragglers (start tracking now, act later)

For an open-source CLI you can't list named accounts. The equivalent is **top dependents still on v2**:
- GitHub code search for v2 pins in CI configs, Dockerfiles, and `package.json` files.
- A list of the largest repos and organizations, which your DevRel and community team contact directly.

Plan to work the last ~15% as a list, not as a docs problem. Even an enforced transition like Chrome MV3 sat at over 85%, not 100%.

## 3. What to build, in order of value per hour

1. **Today:** weekly snapshot of per-version npm downloads into a sheet or table. Time: about one hour.
2. **This week:** a Zendesk tag or macro for upgrade tickets, plus a saved view. The ticket data already exists. Time: about one hour.
3. **This week:** Plausible custom events on the guide (search, support exit, entry anchor clicks). Time: about one hour.
4. **Next 2–4 weeks, a decision for the CLI owner:** a version ping, such as the CLI sending its version once a day. This is the only way to get real active installs, warning counts, and the straggler list.
   - It is a privacy decision: opt-in or opt-out, documented in the README, no identifiers beyond a random install ID, and GDPR reviewed.
   - It is also a trust decision for an open-source CLI. Many users disable telemetry.
   - Present the trade-off to leadership as "no ping means npm downloads only, with the caveats above". Don't build it quietly.

If the ping isn't approved, say so on the dashboard: "adoption measured by downloads, which overstate v2".

## 4. What "working" means (agree this before the first chart)

- **Target:** v3 share of downloads rising and v2 absolute downloads falling, week over week, with a gap to the previous major's curve you can explain.
- **No published benchmark applies to a CLI of this size.** The reference points I have (Chrome MV3 at over 85% for maintained extensions, Kubernetes 78% on supported versions, React 19 about 48% against 18 about 41% in a survey) are calibration only. Set your own checkpoints at day 90, 180 and 270, label them as your judgment, and revise them in public.
- **Hard enforcement waits for a flat curve.** Brownouts, forced removal, or ending v2 security fixes come only once the curve visibly flattens, not on the announced date. Published transitions of this kind take years, not months.
- **At nine months, expect a tail.** Plan for the named-dependent exercise from week one.

## 5. What not to put on the dashboard

- **"Was this helpful" thumbs.** Low signal and easily gamed. It measures whether a page satisfied a reader, not whether anyone migrated. If shown at all, put it on the guide page only, labeled as a satisfaction proxy.
- **Total docs pageviews.** They rise with any traffic, including v2 users reading v2 docs.
- **A single "migration success %".** It hides which of the four tiers is moving.
- **Any effort estimate ("migration takes 30 minutes").** Publish a duration only after a cold-run upgrade of a real project by someone who didn't write the guide. Otherwise publish none.

## 6. Honest status for leadership at day 42

- **You can show today:** current v3 share of npm downloads, v2 absolute downloads, and upgrade-error tickets from Zendesk if the tagging is retroactive.
- **You cannot yet show:** a 30/60/90-day curve (you have no history), active installs, or stragglers. Say that in the first review instead of presenting downloads as adoption.
- **Start the join now.** Begun after more weeks pass, the first 90 days are unmeasurable.

## 7. Verification and KPI summary

- **Cold run:** one person who did not write the guide upgrades a real project from v2 to v3 using only the guide. Record the elapsed time and any undocumented edit. Every undocumented edit is a defect in the guide.
- **KPIs, in order of build cost:** tickets per 1,000 upgrades (Zendesk) → deprecation-warning counts (version ping) → guide behavior (Plausible) → adoption curve (npm, then ping) → stragglers (code search, then ping).