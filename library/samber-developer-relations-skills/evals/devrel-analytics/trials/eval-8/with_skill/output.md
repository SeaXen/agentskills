# Hollybrook: two attribution bugs, both diagnosable without new instrumentation

## Finding 1 — "Nearly every session shows source = our docs domain"

| Field | Value |
|---|---|
| Result | **fail** |
| Severity | critical (source field is being overwritten on the majority of sessions) |
| Confidence | high — matches a named failure mode exactly, and you've already identified the mechanism |
| Observation | Docs domain appears as the session source almost everywhere |
| Evidence | Internal docs→pricing links carry `utm_source=docs` |

**Root cause:** you are tagging an internal link. UTM parameters exist to identify a link a third party clicks *into* your site — putting one on a link between two pages you already own restarts the session and overwrites the real source with your own domain. This is the single most common self-inflicted attribution wound on a docs site, and it's why the number "can't be good news": a visit whose source is your own docs domain isn't a new visitor from docs, it's an existing visitor whose original source (search, social, direct, a conference link) just got clobbered by an internal click.

**Fix:**
- **Strip `utm_*` params from every internal link**, including docs→pricing. No exceptions — that's the rule, not a tuning knob.
- **Exclude your own domain(s) from source classification** so a stray internal tag can never resolve to an external-looking source again.
- Get the "which docs pages drive people to pricing" answer a different way: it's a path question, not a source question. Capture it as a **property on the pricing-page-viewed event** (e.g. `referring_path` or `referring_docs_page`, read from the actual internal referrer, not from a UTM tag) or as an internal click event (`pricing_link_clicked` with a `source_page` property). This keeps the real acquisition channel intact and still gives you the docs→pricing report you actually want.
- Owner: whoever owns the docs site templates (they're the ones who added the tag). Due: before the next reporting cycle — every day this runs, more real sources get relabeled "docs" and are unrecoverable after the fact.

## Finding 2 — "78% direct in launch week"

| Field | Value |
|---|---|
| Result | unknown — this is two things tangled together, not one bug |
| Severity | major (masks real source of conference + signup traffic) |
| Confidence | medium — the causes you named are known tag-killers, but nobody has traced a real conversion through them yet |

**Part A — some of this 78% is not a bug.** Expect "direct" to be the largest bucket regardless of instrumentation quality: aggregators, chat clients, privacy browsers, PDFs and slide decks all strip referrers, and roughly 70% of AI-assistant-driven traffic arrives with no referrer at all (Demand Curve #331). A large direct bucket in launch week is the normal case, not proof anything is broken. Don't let the CMO anchor on "78% is bad" — there's no industry benchmark for this number, and borrowing one would be worse than having no number.

**Part B — the two things you named are real, known tag-death points, and worth verifying before you decide how much of the 78% is "normal":**

- **Link shortener on conference links.** Redirect chains and shorteners must forward the full query string to the final destination, or the tag dies at that hop. Many shorteners drop query params by default unless pass-through is explicitly configured. **Check the shortener's redirect config** — click a real tagged short link and confirm the landing page URL still carries `utm_source`/`utm_campaign` after the redirect.
- **OAuth login before signup.** Same failure, different hop: the browser leaves your domain for the identity provider and comes back through a `redirect_uri` that has no reason to carry your UTM params unless you deliberately preserve them (e.g. stash the tagged landing context — or the `anonymous_id` it should have set — before the OAuth redirect, and re-attach it when the flow returns). If that context isn't captured *before* the OAuth hop, the signup event fires with no memory of the tagged conference link, and lands in "direct" by default.

**What to do:** run the actual trace, don't reason about it from the aggregate number.
1. Fresh browser, no cached session, click a real tagged conference short link.
2. Confirm the landing URL still has the query string after the shortener's redirect.
3. Go through the OAuth flow to signup.
4. Confirm the `signup_completed` event still carries the original source (via `anonymous_id` set on first landing, not re-derived from whatever URL the OAuth provider returns you to).

Whichever hop drops the string is your defect. Fix that hop, re-run the trace, then re-pull the launch-week number — until then, "78% direct" is a floor, not a measurement, and shouldn't be reported as either "fine" or "broken."

**One compounding risk to check while you're in there:** if a conference-tagged visitor loses their tag at the shortener or OAuth hop, lands as "direct," then clicks an internal docs→pricing link before converting, Finding 1's bug (once fixed) would have re-tagged them "docs" instead — same person, wrong bucket twice over. Fixing both in the same pass avoids chasing two explanations for what's really one broken conference-signup path.

**What to tell the CMO:** tracking isn't wholesale broken — direct traffic is expected to dominate launch week, and no clean number exists yet because two specific hops (the shortener and the OAuth redirect) are known points where tags die if not explicitly configured to survive them. That's a config check, not a rebuild, and you'll have a real number once the trace above is run.