# Docs localization plan: Fernhollow, 2026-10-30

I didn't run the interview one question at a time, because you asked for the full answer now. Every unconfirmed point is marked `ASSUMED` and listed below. I also didn't run the drift check, since I have no access to your docs repo. The command is in the plan.

## Short answer

- **ko:** freeze it read-only today, with an outdated banner and a link to the English page. Keep it visible for 30 days while you look for two named reviewers. If you don't find them, retire it with redirects to English. Keeping ko visible without an owner is the failure the skill calls an orphan locale.
- **ja:** report it as `gated` until the drift check and the launch-gate items below are confirmed. It has the two reviewers the gate requires, which puts it far ahead of ko.
- **Dashboard:** report four metrics per locale (adoption, outcome, freshness, quality), each against a control. Don't report page views as success. They show where readers are, not that the translation serves them.

## Stored context

- Locales: ja (owners Aiko, Ren; about 60 pages), ko (no owner; 45 pages, last touched April).
- Pin fields: `source_path`, `source_commit`, `translated_on`, `translation_method`, `reviewed_by`.
- Drift check: `python3 scripts/translation-drift-check.py --source docs/en --locale ja=docs/ja --locale ko=docs/ko --format csv`. Set `--far` from your commits per release.
- Kill rule (baseline): freshness or adoption below target for two consecutive quarters retires the locale.

## Assumptions

- ASSUMED: Aiko and Ren are both fluent enough to review each other's work, so neither approves their own change.
- ASSUMED: reviewer hours for ja are unknown. A support team does this alongside tickets.
- ASSUMED: neither locale has `source_commit` pins today. If they do, ko's status could differ.
- ASSUMED: the ko traffic you mention is page views or sessions by country, not browser-language or engagement data.
- ASSUMED: Minjun's silence since June is unreachable, not a pause. A single direct message with a deadline costs nothing and settles it.

## Decision summary

| Locale | Decision | Reason | Unlock or reopen condition |
| --- | --- | --- | --- |
| ja | `gated` (becomes `launch` once the gate items close) | Two named owners. Pins, glossary and retirement threshold unverified. | All six gate items confirmed (table below) |
| ko | Freeze now, then `retire` unless an owner is found | Last reviewer gone for about 4 months. Pages untouched for about 6 months, behind every source commit since April. | Two fluent, named reviewers, then the full launch gate. Not by unfreezing the old pages. |

## ko: what to do

1. **Today:** run the drift check on `docs/ko`. Expect most pages to be `no-pin` or `far`. That output is your evidence, so no one has to take "it's stale" on trust.
2. **Today:** add the outdated banner to every ko page. It sits in the first line, in Korean, with a link to the English page:
   > This page was translated from an earlier version of the English page. The English page has changed since. Read the current English version →
3. **Today:** send Minjun one message with a date. Say you will freeze the locale, and ask whether they want to hand it over or help find a successor.
4. **Today:** fall back to the English page for any critical-path ko page that is `far` behind: quickstart, install, auth. A stale procedure fails the reader in the middle of a task, which is worse than an English page.
5. **Next 30 days:** look for two fluent reviewers. Ask the Korean-speaking users who file tickets or post in your community, and ask Aiko and Ren whether support has any Korean speakers. Without two, a single person approves their own work.
6. **Day 30:** if two reviewers are named, run the full launch gate (below), starting with a critical-path pack. If not, retire the locale. Redirect every ko URL to its English page and remove ko from the language switcher.

Your threshold already says this. The retirement rule reads: "Last named reviewer leaves, no replacement within one quarter → freeze read-only with banner, then retire." June to October is more than one quarter.

### Why this is not giving up

- **Retirement is a decision with a reopen condition.** The reopen condition is two named reviewers.
- **MDN did this at scale, and the traffic cost was small.** In 2021 it stopped displaying 21 locales that had no community lead, with an estimated traffic loss under 2%. Those URLs redirect to English. This figure is MDN's own estimate, not your data.
- **ko traffic is not evidence the translation is needed.** Country or page-view traffic says where readers are, not that they need a translation. The skill's Step 1 tests this with browser language, an engagement gap, and tickets in Korean. Run those tests on ko. If Korean readers complete the quickstart like English readers, the barrier isn't language.
- **Leaving stale pages up carries a risk.** Pages that misstate parameters, quotas, deprecations or security steps do real harm, and a banner reduces that harm without removing it.
- **Source hardening still serves Korean readers.** Plain English, one term per concept, a glossary and `translate="no"` on code help every non-native reader. Browser translation then handles code and terms better.

If you want to keep ko beyond day 30, tell leadership the cost: two reviewers, standing hours per release, and the pin and drift check enforced in CI. Compare that cost with what ko traffic is worth to you.

## ja: gate status

The skill requires every item below before a locale counts as launched. I can't see your repo, so I haven't checked any of them.

| Item | Status | Closing action |
| --- | --- | --- |
| Two named fluent reviewers | ASSUMED met (Aiko, Ren) | Confirm both are fluent and neither approves their own change |
| Critical-path pack and all site UI strings translated and reviewed | Unknown | Check quickstart, install, auth, top task pages and navigation strings |
| Glossary with "do not translate" decisions | Unknown | Create one: owner, file location, decision log |
| Pin on every page, drift check running | Unknown | Run the drift check. Add `--fail-on no-pin,unknown-pin` for new pages. For the existing backlog use `--since <ref>`, so only pages added or edited after that ref can fail the build. |
| Written retirement threshold and a named person allowed to pull the locale | Unknown | Adopt the thresholds above and name the person |
| Published owner names and a contact for translation problems | Unknown | Add them to the ja pages and the status page |

Three things to check on ja:

- **Capacity.** Two support staff review 60 pages on top of their ticket work. Use the Step 3 arithmetic. Changed pages per release × re-review hours per page must not exceed their reviewer hours per release. The baseline pace is 15-30 minutes per changed page; replace it with their real pace after one release. If the check fails, shrink ja to the critical-path pack and fall back to English for the rest.
- **Backlog.** Pin the existing 60 pages. Expect many `no-pin` results the first time.
- **Single point of failure.** If either of them leaves, you are one reviewer short of the gate.

## Dashboard: what to report

"Locale success metrics" should mean outcomes against a control (the same pages read in English by the same market). It should not mean page views.

| Metric | ja | ko | Control | Type |
| --- | --- | --- | --- | --- |
| Adoption: share of Japanese/Korean-language sessions staying on locale pages vs switching to English | Pull from analytics | Pull from analytics | English-page readers in the same market | measured |
| Outcome: quickstart completion or time to first API call | Pull from analytics | Pull from analytics | English readers | measured |
| Freshness: % of pages `current` by pin (target ≥ 80% of the critical-path pack at every release) | Run the drift check | Run the drift check | None; the target is a baseline | measured |
| Quality: translation-problem reports per 1,000 views | Needs a report link on the page | Same | None | measured |

- **Don't invent numbers.** I have none of these values, and the dashboard shouldn't show targets for ja that nobody has measured. A new locale has no adoption figure yet, so record the control and the pre-launch figure, then set the first target after one release.
- **Show ko as it is.** The row shows ko frozen, freshness near zero, retirement decision due on day 30. A dashboard that hides the stale locale would make the other numbers harder to trust.
- **Show the kill rule on the dashboard.** The rule is freshness or adoption below target for two consecutive quarters, and it is a baseline you replace with your own cadence. ko already fails the rule on freshness.

## Rollout schedule

| When | Milestone | Owner |
| --- | --- | --- |
| Today | Run the drift check on ja and ko. Add the ko banner and the English fallback. Message Minjun. | You |
| Within 1 week | Confirm the ja gate items. Adopt the retirement thresholds and name the person who can pull a locale. | You, Aiko, Ren |
| Within 2 weeks | Run Step 1's tests on ko (browser language, engagement gap, Korean-language tickets). Ask for Korean reviewers. | You |
| Day 30 (about 2026-11-29) | ko decision: two named reviewers go to the launch gate; otherwise retire with redirects | You |
| After the next release | First ja dashboard readings. Replace the baseline pace and targets with measured ones. | Aiko, Ren |

## Questions that would change this answer

1. What do browser-language share and the engagement gap say for Korean readers?
2. Do the ko pages carry any `source_commit` pin?
3. How many reviewer hours per release can Aiko and Ren give?
4. Is the product UI, CLI output and support available in Japanese and Korean? A translated quickstart that ends in an English-only console makes the reader switch languages mid-task.