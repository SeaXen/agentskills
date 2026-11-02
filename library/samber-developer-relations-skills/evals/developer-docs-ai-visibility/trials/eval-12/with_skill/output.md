**Not good as planned.** Two of the three actions destroy owned assets the skill's cheapest fixes need, and the third uses the wrong tool.

**Next action (2 min):** paste the 3.0 replacement for `Oakspire.session({ store: 'memory' })` and the exact error a 3.x user sees when calling it. Every template below needs both.

## 1. Verdict

- **Where answers go wrong:** assistants cite three stale sources for "oakspire session setup". Two are yours, one is a third-party tutorial.
- **Pipeline:** all three show up as citations, so likely search-grounded retrieval (practitioner inference). The code in those answers may still come from training recall. Run the search-off test before assuming otherwise.
- **First two levers:** fix your owned stale copies (starter repo, `oakspire-legacy`), then put version identity in your docs page text.

## 2. Your plan, item by item

| Plan | Call | Why |
|---|---|---|
| Takedown to the blog | **Drop** | A "takedown" has no basis for an old, accurate-for-2021 tutorial. Send a short note with the exact replacement code instead. Many authors update, none owe you. This is the lowest-value lever, so do it last. |
| Delete the starter repo | **Replace** with: keep it archived, edit the README | Deleting breaks every inbound link and loses the page that could name the replacement. Forks and scraped copies stay up, so the citation likely moves to one of them (practitioner inference; nobody has measured mirror share). |
| Unpublish `oakspire-legacy` | **Replace** with: final patch | Unpublishing breaks builds that pin it. It can also free the name for someone else to take, which is a real risk for an auth library. npm limits unpublishing a package that has dependents or downloads (check the current policy). A final patch whose README opens with the replacement is rated `++` value and `+++` durability. |

Deleting the starter repo or unpublishing the package can't be undone. Don't do either until the baseline in section 4 exists.

## 3. Access check (unreviewed, I have not seen your rules)

- Confirm `robots.txt` and any CDN "block AI bots" preset do not block `OAI-SearchBot`, `Claude-SearchBot`, `PerplexityBot` or `Googlebot`.
- Do not disallow `Google-Extended`: it also gates Gemini grounding.
- Fetch your session-setup page with a plain HTTP client and no JavaScript. Body text and code blocks must be in the HTML.
- Check for `nosnippet` or `data-nosnippet` on code blocks.

## 4. Baseline before any change (~6 h by hand, estimate)

- Minimum panel: 10 prompts × 5 runs × 2 assistants, search-on. Add search-off on the 5 worst prompts, one assistant. That is 125 answers at about 3 min each.
- Prompt families: task ("oakspire session setup"), error string, migration ("upgrade oakspire 2 to 3"), status ("is `store: 'memory'` still supported").
- Answer key per prompt, written before any run:

```
P01 | must contain: <3.0 replacement> ; oakspire@^3 | must not contain: store: 'memory' ; oakspire-legacy | /docs/v3/sessions
```

- Score each answer for cited source, version-correct, deprecated API and invented API.
- Report rates with n and a Wilson interval, pooled by family. Never report a rank.
- Agree the targets now (section 6), so the re-run has a fixed finish line.

## 5. Lever plan

Track 1 (ships now):

1. **`oakspire-legacy` final patch (~1 h).** Release it, run `npm deprecate` naming the replacement, and open the README with:

```
Deprecated: oakspire-legacy is no longer maintained. Use `oakspire` v3.
`Oakspire.session({ store: 'memory' })` was removed in 3.0; use <3.0 replacement>.
Migration: <migration guide URL>
```

2. **Starter repo (~15 min).** Unarchive, put the same opener as the first README line, link the current starter, then re-archive. Check that no docs page links to the old repo as current.
3. **Version identity on your docs (~1–2 h, one template edit).** Put the version after the searched term in the title, the first heading and the opening line: "Session setup (Oakspire v3)". Open any superseded page with the replacement symbol and a link to the current page. Make the banner server-rendered text, not JavaScript.
4. **Symbol map in the migration guide (~half a day).** One row per removed symbol, in the exact old spelling:

```
| 2.x (removed in 3.0)                | 3.x replacement     | Notes |
| Oakspire.session({ store: 'memory' }) | <3.0 replacement>   |       |
```

5. **Note to the blog author (~20 min), disclosing your affiliation:**

> Hi, your 2021 Oakspire session tutorial ranks well and assistants cite it. `Oakspire.session({ store: 'memory' })` was removed in 3.0. The 3.x equivalent is `<3.0 replacement>` (migration guide: `<url>`). A version note at the top would help readers. Happy to send a PR-style diff.

Track 2 (starts now on the SDK cycle, since you hold release access):

- **Runtime deprecation warning.** Ship it in the last 2.x release and as a clear error in 3.x:

```
OakspireDeprecation: store: 'memory' was removed in 3.0.
Use <3.0 replacement>. Migration: <docs URL>/migrate#session-store
```

- This is the only lever that reaches answers written from training recall.

Lever notes:

- **Steering:** keep banners, READMEs and warnings to version facts. Do not mention the hosted plan there; that reads as steering.
- **Deleted:** `llms.txt` as a citation lever, FAQ or statistics rewrites, date bumps, and any noindex on versions people still run. Say so if anyone asks for a "GEO plan".
- **Feedback reports:** file them in each assistant's UI for repeatable wrong answers. Log the date; no turnaround is published.

## 6. Measurement

- **First-party data:** at least 14 days of AI referrers (`chatgpt.com`, `perplexity.ai`, `claude.ai`, `gemini.google.com`, `copilot.microsoft.com`) on the docs path. Add server logs by bot role and docs version path with `scripts/ai-bot-log-summary.py`. Add support tickets tagged "code from an assistant".
- **Re-run:** same panel, 4–8 weeks after the last page change goes live.
- **Control:** prompts whose owning page you did not touch. A template edit touches every page, so roll it out to one section first and use the rest as control. Otherwise compare against the logged baseline and void it if a model release lands in between.
- **Targets (self-set, agree before the baseline):**
  - Zero deprecated-API answers on the three highest-traffic docs tasks, search-on.
  - Version-correct rate above baseline, with intervals that separate.
  - Owned-page citation rate above baseline on prompts whose answer lives in the docs.
- **Outcomes:** citation and ranking results stay pending. Page changes are verifiable today, but re-indexing runs on each vendor's schedule.

## 7. What no docs change fixes quickly

Search-off answers come from released model weights. Only a later model, and the runtime warning, shrink them. Set no search-off target until a new model ships.

## ASSUMED (correct me)

- No hard deadline, and this becomes a standing practice for each major.
- The two assistants that matter are ChatGPT and Claude.
- You can edit the docs template and the SDK release.