# Fernhollow localized docs: status report and what to do with ko

**Recommendation:** keep ko live, but don't report it as healthy. Report it as unowned and at risk, label the pages, and set a decision date. Keeping a page visible is different from calling it a success.

## 1. What to report to leadership

"Locale success metrics" shouldn't be one blended number. Averaging ja and ko would hide the problem. Report per locale, with four dimensions and a status.

| Dimension | ja | ko |
|---|---|---|
| Owner | Aiko + Ren (Tokyo support) | None. Volunteer unresponsive since June |
| Pages | ~60 | 45 |
| Coverage (% of English pages translated) | *need English page count* | *need English page count* |
| Freshness (last edit, and % of pages whose English source changed since the last translation) | *need data* | Last touched April, so ~6 months stale |
| Usage (pageviews and share of locale traffic) | *need data* | "Still gets traffic" (*need number*) |
| Outcome (helpfulness votes, search exits, support tickets from that locale) | *need data* | *need data* |
| Status | Likely green, pending freshness data | Red: unowned and stale |

Notes on the table:

- **Don't fill the blanks with guesses.** I don't have your analytics, so every *need data* cell has to come from your tooling. If you can't get a metric, show "not measured" rather than a number.
- **Freshness matters more than page count.** For each locale, diff pages against the English source and count how many changed after the translation date. That count is the real measure of whether the docs are still true.
- **Treat traffic as context, not success.** Traffic to stale pages isn't a good outcome. Pair it with outcome signals. Two good ones are helpfulness votes and the share of Korean support tickets that cite a doc page.
- **ja is probably fine, but don't assume it.** Two owners and a team that sees real customer questions is a strong setup. Still, ownership by two people on one support team is a bus-factor risk, and you don't yet have freshness data. Report ja as "owned, freshness pending" until you do.

Suggested status rubric, so ko's color is a rule and not an opinion:
- **Green:** has an owner, and under 10% of pages are stale.
- **Yellow:** has an owner, but staleness is higher or there's no backup owner.
- **Red:** no owner, regardless of traffic.

## 2. What to do with ko

Your instinct is half right. Pulling ko would remove something users still use, and it would be hard to undo. The risk of leaving it unchanged is that Korean readers act on instructions that stopped matching the product in April. Both can be handled.

**This week (about 2 to 3 hours):**
1. Check what changed in the product since April (changelog or release notes). Note anything that affects setup, auth, pricing, limits, or breaking changes.
2. List the top ko pages by traffic and diff each against its English source. Mark each one as accurate, minor drift, or materially wrong.
3. Add a banner to every ko page: "This translation was last updated in April 2026 and may be out of date. See the English version for the latest." Link to the English page. Pages that are materially wrong get a stronger warning. If they're dangerous (security or data loss), unpublish those pages specifically, not the whole locale.
4. Make one more attempt to reach Minjun through a different channel, such as email or the community platform. Thank them for the work and ask whether they want to hand it off. Don't assume they've left.

**Next 30 days: find an owner.** In rough order of cost:
- Ask Korean-speaking customers or community members for a successor. Offer credit, swag, or a named maintainer role.
- Check whether anyone at Fernhollow reads Korean well enough to review.
- Use machine translation plus paid human review, limited to the top-traffic pages.
- Only fall back to a shared Tokyo-team arrangement if someone there reads Korean. ja ownership doesn't transfer to ko by default.

**Decision date (suggest 60 days out):**
- **Owner found:** restore ko to yellow, then green once freshness is fixed.
- **No owner:** shrink ko to the pages that are both high-traffic and accurate, keep the banner, and redirect or retire the rest. Retire in stages, with redirects to English, and don't delete everything at once.

Write the decision date and the rule into the dashboard note. A rule agreed in advance is much less likely to feel like giving up than a quiet removal later.

## 3. How to present ko to leadership

A red cell on the dashboard is the strongest argument you have for resourcing ko. Suggested wording:

> **ja:** Owned by the Tokyo support team (~60 pages). Freshness being measured; first reading due [date].
>
> **ko:** 45 pages, no active owner since June, last updated April. Still receives [X]% of docs traffic from Korea, so we are keeping it live with an out-of-date notice while we recruit a maintainer. Decision on scope by [date, ~60 days].
>
> **Ask:** [a named owner, or a small budget for translation review].

This is honest, shows you know the risk, and ties the red status to a request leadership can approve.

## 4. What I need from you

1. English page count, so I can compute coverage.
2. Pageviews for ja and ko over the last 90 days, plus any helpfulness or ticket data.
3. Whether anyone on the team reads Korean.
4. Last-updated dates for the ja pages.

With those I can turn this into the filled-in dashboard table.