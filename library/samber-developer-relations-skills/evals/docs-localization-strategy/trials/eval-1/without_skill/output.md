# Decision: Japanese docs for Ironvale

## Answer for Friday

**No to the plan as written** (translate all 800 pages once with an LLM, publish under `/ja/`, fix on complaints).

**Yes to a 6-week pilot** of about 15 pages with a native-speaker reviewer, and a go/no-go on the full set at the end.

## Why the data doesn't justify 800 pages yet

1. **Japan readers already succeed in English.** Quickstart completion is 41% in Japan against 44% for English-browser readers, a 3-point gap. Translation can't recover much from a gap that small.
2. **Most Japan traffic doesn't want Japanese.** Japan is 38% of sessions but only 12% of sessions have a `ja` browser. If every `ja` session is in Japan, about two thirds of Japan sessions read English by choice.
3. **The real gap may sit in one segment.** If Japan's non-`ja` sessions complete at 44%, the `ja`-browser sessions complete at about 35%. That is roughly a 9-point gap on 12% of total sessions.
   - Closing that gap fully would add about 1 point to overall completion.
   - That figure is an upper bound. It rests on my assumptions that all `ja` sessions are in Japan and that Japan's non-`ja` sessions match English readers. Pull the real numbers to confirm.
4. **The 38% may not mean demand.** Sessions are not users, signups or revenue. Bots, crawlers, one large customer's team, or a post-trip spike can all inflate it. The data says nothing about whether Japan produces API keys or paid accounts.

## Why the plan's execution is the bigger problem

- **We can't detect errors.** Nobody on the team reads Japanese, so we can't review the output or triage complaints written in Japanese.
- **"Fix when people complain" fails here.** Developers who hit a wrong parameter description or mistranslated error explanation don't file tickets. They leave, or they ship a bug.
- **Wrong docs are worse than English docs.** For an API gateway, a translation error in auth, rate limits or config semantics causes production incidents. A reader of the English page at least gets the correct text.
- **Search risk.** Publishing 800 unreviewed machine-translated pages at once can look like scaled low-quality content to search engines. That can hurt the site, not just `/ja/`.
- **Drift.** Hugo content changes weekly. Without a sync process, `/ja/` goes stale within months and contradicts English. The LLM run is the cheap part. Review and ongoing maintenance are the cost.

## Before the pilot (about 1 to 2 days, no spend)

Pull these from analytics:

1. Quickstart completion for `ja`-browser sessions alone, against English and against Japan non-`ja`.
2. Japan share of sessions over the last 6 to 12 months, with bots filtered. Is it flat or a spike?
3. Japan share of signups, API keys created and paid accounts. This is the number that matters.
4. The top 20 pages by Japan sessions.
5. Search-console impressions and clicks from Japan, split by query language if possible.

**Stop rule:** if `ja`-browser completion is within about 5 points of English and Japan is under about 10% of signups, close the project. Revisit in two quarters.

## Pilot (about 6 weeks)

- **Scope:** quickstart, authentication, and the top 10 to 15 Japan-traffic pages.
- **Translation:** LLM first draft, then a paid native technical reviewer (contractor or agency). This is the only cost that matters and it is small at 15 pages.
- **Rules for the draft:**
  - Leave code, identifiers, endpoints, error strings and config keys untouched.
  - Use a glossary the reviewer approves.
  - Tell the model to flag uncertain passages.
- **Publishing:**
  - Use Hugo multilingual mode with `hreflang` set.
  - Put a banner on each page: "Translated. English is authoritative."
  - Link back to English.
  - Leave unreviewed pages unpublished. English-only pages fall back to English.
- **Drift control:** record the English commit each translation was made from. CI flags any translated page whose English source has changed.
- **Support:** add a visible feedback link on `/ja/` pages and route it to the reviewer, so complaints get read.

## Pilot success measures

Use `ja`-browser sessions as the target segment, compared before and after:

| Metric | Expand if | Stop if |
|---|---|---|
| Quickstart completion, `ja` browser | Up 5+ points | No change |
| Signups and API keys from Japan | Up measurably over baseline | Flat |
| Japan organic search clicks | Growing on `/ja/` pages | Flat after 6 weeks |
| Reviewer correction rate | Under about 5% of sentences | Over about 15%, so the draft isn't usable at scale |

If the pilot passes, scale in tranches ordered by Japan traffic, with the same review and drift checks. Don't do one bulk publish.

## Cheaper options if the CEO wants a visible signal now

- Add a Japanese landing page and quickstart summary, reviewed by a native speaker.
- Show a banner on English pages for `ja` browsers that points to the translated pilot pages.
- Don't ship browser auto-translation as a substitute. It can't be controlled or reviewed.

## What I'd tell the CEO in one line

"Japan is a real share of traffic, but those readers are completing our English quickstart at nearly the same rate. We'll test Japanese on the pages that matter with a native reviewer for six weeks, then decide on the rest with data."

## Open questions for you

- Is there any Japan-specific revenue, customer or sales pipeline you know of? That would override the stop rule.
- What budget is available for a native reviewer? I assumed a small contractor line, not a headcount.