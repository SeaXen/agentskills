Do not show "AI citations up 31%, on track for +40%". Three things break it:

- The 31% counts **ChatGPT clicks**, not citations.
- The Copilot figure has **no baseline**.
- The +40% has **no evidence behind it**. The skill lists "promised lift" as a failure mode.

Below are a slide and a report section that stay defensible if someone checks them.

## Slide

**Title:** Every docs page now states its version. Early AI signals are positive, not yet attributed.

**What shipped (2026-10-19):** The version now appears in the title and H1 of all 900 docs pages, from one template change.

**Early signals (first-party and vendor reports):**
- ChatGPT referrals to `/docs/` are up 31% over the prior 5 days. These are clicks only, so they undercount.
- Copilot cited docs 140 times this week (Bing Webmaster). This is the baseline week.
- Google reports no AI-specific figure. It folds AI Overviews and AI Mode into Web search totals.

**Not yet known:**
- Whether the template change caused the lift.
- Whether assistants now answer with current-version code.

**Next:**
- 2026-11-05: 14-day read-out.
- 2026-11-16 to 2026-12-14: re-run of the same prompt panel.
- Targets are set before the baseline run: version-correct answers up, zero deprecated-API answers on the top 3 tasks, owned-docs citations up. No percentage is promised.

**Speaker line:** "ChatGPT referrals to docs rose 31% in the first week after the change. We will confirm cause and answer quality by mid-November."

## Quarterly report: measurement section

### 1. What is measured
Three signals measure different things. Never add them together or call the total "citations".

| Signal | Measures | Source label | Limit |
|---|---|---|---|
| `chatgpt.com` referrals to `/docs/` | Clicks from ChatGPT answers | first-party | Lower bound. Apps strip referrers and developers copy code without clicking. |
| Bing Webmaster AI report | Copilot citations and grounding queries | vendor-documented | No clicks. This week is the first data point; prior weeks not yet pulled. |
| Search Console | AI Overviews and AI Mode inside Web totals | vendor-documented | AI traffic cannot be separated. "Nothing AI-specific" does not mean zero. |

### 2. Results to date
- ChatGPT referrals: +31%, 5 days against 5 days.
- Copilot: 140 citations in one week.
- Quality: not measured. A citation can point to correct code or deprecated code, and the counts cannot tell which.

### 3. Why the 31% is not yet attributable
- **Window too short.** The skill's floor is 14 days of data before quoting a share. Thursday is day 17 since ship, so refresh with the full post-ship window against an equal pre-ship window.
- **Probably too early for re-indexing.** Retrieval changes take days to weeks to reach an assistant's index. A lift in the first days may not come from the change.
- **No control.** The template touched all 900 pages, so no untouched section exists. Controlled comparison is lost for this change.
- **Small counts.** With an assumed 100 referrals before and 131 after, the 95% interval on the ratio runs from about 1.01 to 1.70. With 20 and 26 it runs from about 0.72 to 2.36. The second case includes "no change". This is arithmetic on assumed counts, so replace them with the real ones.
- **Unlogged confounds.** Check for model releases, launches or press in the window, and for weekday mix.

### 4. Method
1. **Referral comparison.** Compare daily `chatgpt.com` referrals, including `utm_source=chatgpt.com`, over the post-ship window against the equal pre-ship window. Add `perplexity.ai`, `claude.ai` and `copilot.microsoft.com`. Log any model release inside either window. A release voids the comparison.
2. **Partial control.** Compare `chatgpt.com` referrals to non-docs paths (blog, marketing). If they rose too, the cause is ChatGPT-wide. This is practitioner inference, not a clean control.
3. **Bot logs.** Run `ai-bot-log-summary.py --path-prefix /docs/` with vendor IP ranges. Split by bot role and version path.
4. **Bing history.** Pull earlier weeks from the AI report. If none exist, label 140 a baseline.
5. **Prompt panel.** Minimum viable size is 10 core prompts × 5 runs × 2 assistants, search-on, plus search-off on the 5 worst prompts: 125 answers.
   - Write the answer key first: symbols, version range and deprecated forms per prompt.
   - Score cited source, version-correct, deprecated API and invented API.
   - Report pooled rates with n and Wilson intervals.
6. **Panel baseline caveat.** The template is already live, so no pre-change panel baseline exists. The panel baselines quality from now on. The pre/post referral and log comparison judges the template change itself.
7. **Access check.** Fetch three pages with a plain HTTP client. Confirm the new titles and H1s, body text and code blocks are in the HTML without JavaScript. Review `robots.txt` and the CDN bot rules, including `Google-Extended` and `OAI-SearchBot`. Until reviewed, access stays unreviewed.

### 5. Targets (to agree before the panel runs)
- Zero deprecated-API answers on the 3 highest-traffic docs tasks, search-on.
- Version-correct rate above baseline, with intervals that separate.
- Owned-docs citation rate above baseline on prompts whose answer lives in the docs.

Citation and ranking outcomes stay **pending** until the re-run.

### 6. Calendar
| Date | Event |
|---|---|
| 2026-11-02 | Panel baseline starts; Bing history pulled |
| 2026-11-05 | 14-day-plus referral and log read-out |
| 2026-11-16 to 2026-12-14 | Panel re-run (4 to 8 weeks from ship) |

### 7. What no docs change fixes quickly
- **Released model weights.** Answers written from training recall stay stale until a later model trains on a corpus where the current version dominates.
- **Vendor index schedules.** Re-crawl timing is theirs to set.

If the panel shows uncited deprecated answers inside coding agents, the next levers are runtime deprecation warnings in the SDK release and version-matched docs delivered to those agents.

## Open items
- Real daily referral counts: with them I can compute the interval.
- Why only 5 days of analytics when ship was 11 days ago. Use all 11 days if the data exists.
- Answer-key inputs: published versions, removed symbols and their replacements.

**Next, under 2 minutes:** export daily `chatgpt.com` referrals to `/docs/` from 2026-10-05 to today and send them to me.