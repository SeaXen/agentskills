# Docs/content measurement for Cinderbank's board meeting — a 3-week build plan

**The reframe:** you can't build attribution in 3 weeks with no engineering and no data team. You *can* stand up honest leading indicators from every channel you already fully own, and show the board a gap you found and are actively closing. That's a credible board story; a stretched causal chart isn't.

Four tracks, running in parallel:

---

## Track 0 — Zero engineering, start today

None of this needs a ticket. Some of it has a shrinking window, so sequence it first.

1. **Verify Google Search Console today** (DNS TXT record or an HTML file upload — a 5-minute favor from whoever holds DNS, not a sprint item). GSC does not backfill — every day you delay is data you never get back. This is likely your single biggest channel for docs/dev content and right now you have zero visibility into it.
2. **Start polling GitHub's Traffic API today** (`GET /repos/{owner}/{repo}/traffic/views` and `/traffic/popular/referrers`) and save the output somewhere durable. GitHub only retains 14 days of traffic data, so the moment you start is the moment your history begins. Check if your blog domain shows up as a referrer to the repo — that's a direct content→engagement link, no product data needed.
3. **Pull npm downloads now** via `https://api.npmjs.org/downloads/range/<start>:<end>/<package>` — free, unauthenticated, full history since the package's first publish. Plot it against your content calendar and release dates.
4. **Pull your GitHub star history** for free via star-history.com, or `GET /repos/{owner}/{repo}` daily — instant, no setup, no ticket.
5. **Create a Discord bot** via the free Discord Developer Portal (self-serve, no eng needed) and log `guild.member_count` and daily message counts. If you're short on time this week, just record member count twice a week manually starting now.
6. **Check your hosting platform's built-in analytics before assuming you have "nothing."** If docs/blog run on Cloudflare Pages, Vercel, or Netlify, log into that dashboard — these often surface pageviews, top pages, and referrers at the infrastructure layer with zero code and zero ticket, because you're already paying for the proxy. Do this check first; you may already be sitting on weeks of unused data.
7. **Pull Ahrefs data** if you have it (backlinks, referring domains, keyword rankings) — it already has historical data, no setup required.
8. **Start UTM-tagging every outbound link you control** — blog CTAs, npm README links, Discord invite links, social posts. Keep a one-tab spreadsheet as the log. This is free and it's the only way to later see which content a click came from, even before a destination tool exists to catch it.
9. **Add one open-text "how did you hear about us?" field** somewhere you already control — your Discord bot's welcome flow, or a lightweight Google Form linked from the docs footer. This is self-reported attribution, and it's the only way to catch word-of-mouth/dark-social signal that no pixel will ever see.

---

## Track 1 — Spend the one ticket here, and only here

Ask engineering for exactly one thing: **add a single analytics snippet (GA4, or a privacy-first tool like Plausible/Fathom) to the docs site and blog templates.**

Frame it explicitly as *DevRel-owned marketing-site analytics on public pages*, separate from the product team's existing PostHog/Amplitude/Mixpanel. That framing is also why it should clear where "give me access to product analytics" didn't: it's a new, small, unrelated thing, not a request to share their system or their data.

Before filing the ticket, **check the page source for `googletagmanager.com` or an existing `dataLayer`** — if GTM is already installed, you may not need a ticket at all; you can add tags yourself through the GTM UI.

Once live, mark "docs → signup CTA click" and "blog → signup CTA click" as conversions. That gets you funnel data going forward without needing the product team to confirm what happens after the click.

---

## Track 2 — Turn your own repos into your own data team

No data team doesn't mean no pipeline — you own two repos and their GitHub Actions minutes outright, so this needs no ticket at all.

**Add a scheduled GitHub Actions workflow** (`schedule: cron: '0 6 * * *'`) in a repo you control that calls the npm downloads API, GitHub traffic/stars API, and your Discord bot once a day, and appends the results to a Google Sheet via a service account (Sheets API) or commits a CSV back to the repo.

Bolt on the **free GSC Sheets/Apps Script connector** and, once Track 1 lands, the **official GA4 Sheets add-on**.

End state: one spreadsheet that updates itself every night with npm installs, GitHub traffic/stars/referrers, Discord growth, GSC impressions/clicks, and GA4 docs/blog traffic — the analytics stack you're missing, built from parts that need nobody's permission.

---

## Track 3 — Reframe the product-team ask (parallel, doesn't block the board deck)

Don't ask a third time for "analytics access" — same request, same likely answer, and it costs you credibility. Ask for something narrower and cheaper to grant:

> "Can the signup form capture `utm_source`/`utm_medium`/`utm_campaign` as hidden fields, and can I get a weekly CSV of `{signup_date, utm_source, utm_medium, utm_campaign}` — no other fields, no dashboard access?"

That's a data question, not an access question — an hour of engineering work, not a policy decision a team has to defend twice. Position it as useful to them too: closing the loop on whether DevRel-sourced signups convert is information product benefits from, and you're offering to own the analysis.

Run this once you have 4–6 weeks of your own numbers (post board meeting) — "here's what we already found on our side, this one field would close the loop" lands better than an open-ended ask.

---

## What to actually show the board in 3 weeks

1. **Name the gap plainly:** "Until three weeks ago we had zero instrumentation on content — no docs analytics, no tagging, no attribution." One sentence, no defensiveness.
2. **What's live now:** docs/blog analytics, GSC verified, an automated tracker across npm/GitHub/Discord/GSC, UTM discipline, a self-reported source field.
3. **Directional signal from channels you fully own** (the only place you have real history): npm install trend with content/release dates marked on it; GitHub star curve and whether your blog shows up as a repo traffic referrer; Discord growth; GSC's first 2–3 weeks of impressions/clicks for target technical queries, honestly labeled as a short window.
4. **Say what this doesn't answer yet:** whether any of this converts to signups or revenue — that needs either the product-side field (Track 3, in flight) or a full quarter of GA4 conversion data (Track 1, in flight). Naming the limit yourself is more credible than implying the correlation charts are causal.
5. **The ask, if any:** nothing is needed to keep this running — it's automated — but flag that a real content→revenue view is gated on the Track 3 field landing.

---

## 90 days out

- Once GA4/GSC have a full month of data, build a **free Looker Studio dashboard** on top of the same sources — no engineering, pulls straight from GA4, GSC, and your Sheet.
- Revisit Track 3 once you have your own 4–6 weeks of numbers — the pitch gets stronger with evidence in hand.
- If the npm-installs-vs-content correlation looks real, consider skipping a content push for one release cycle and watching whether the install bump disappears — a cheap, self-run test that gives you your first real (small-N) causal signal without needing product data at all.

---

## What not to do

- Don't spend the one ticket on anything beyond the analytics snippet — a bigger ask is more likely to get scoped down to nothing before the board date.
- Don't re-ask product for the same broad access a third time.
- Don't present npm/GitHub/Discord trend lines to the board as proof of causation — call them "leading indicators from channels we fully own" and let the honesty carry the credibility.