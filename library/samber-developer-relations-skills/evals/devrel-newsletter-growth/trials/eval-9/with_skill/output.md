## Answer

Neither plan as proposed. Both are fast, but the first is a refused move and the second breaks a precondition. Here is what to do instead.

1. **Email wall on the Kubernetes cost tuning tutorial: no.**
2. **Exit-intent popup on the docs: no.**
3. **Paste every full issue into Medium and a LinkedIn newsletter: partly.**
   - On Medium, republish only with a canonical link back to your archive page.
   - On LinkedIn, post an excerpt of the lead item plus an archive link.
   - Treat both as a standing monthly job and start them after the first two channels below.

## Refusals applied

| Move | Label | Why | Replacement |
|---|---|---|---|
| Email form gating the tutorial | trust | Curators refuse gated links, and developers read a gate as lead capture. It would also cut the tutorial's reach to the curated newsletters that could send you new readers. | Keep the tutorial open and add a signup line after the final step. Suggested copy: "Got it running? One email a month on releases and breaking changes. Read the latest issue first." Source tag: `docs-quickstart-end`. |
| Exit-intent popup on the docs | trust and house rule | The skill's copy rules allow no popups on content pages, and developers dismiss them on sight. The skill gives no conversion rate for docs popups. | A one-line docs footer ("Monthly: what shipped, what broke, what's next. Latest issue ->"), tagged `docs-footer`. |

If the content marketer's real goal is feeding the newsletter, the quickstart-end line is the highest-intent surface in the skill. The reader has just succeeded.

## Medium and LinkedIn

This is row 6 of the channel menu, "republishing", and it ranks sixth of nine on efficiency. It costs about an hour per issue, every issue, with no end date.

- **Medium:** I believe Medium's story import sets a canonical link automatically, but I haven't verified that. Check Medium's current settings before relying on it. Without a canonical link, the full copy competes with your own archive in search.
- **LinkedIn newsletters:** I'm not aware of a canonical-link setting. If there isn't one, post an excerpt of the lead item plus the archive link, not the full issue.
- **Both platforms:**
  - End every copy with the signup line and its own source tag: `republish-medium`, `republish-linkedin`.
  - Republish only after the archive page is live.
  - A platform's own followers or subscribers are not your list. Only people who click through and confirm on your form count.
  - Check each platform's current terms and self-promotion rules before you post.

## Growth gate: unproven

I haven't asked you the interview questions, so none of the three conditions has evidence yet. Proving them comes before any new channel opens.

1. **Programme holds:** Is there a named owner and backup, and did the last three issues go out full and on cadence? If not, stop and route to `devrel-newsletter-program`.
2. **Consent known:** For each segment of the 2,700, which form or import did it come from? Any segment with no source gets classified and suppressed before we count the list.
3. **Sources distinguishable:** Does the form carry a source field? If not, add one before anything else. Without it, none of the channels below can be ranked.

## Recommended order

Wait for your decision before I write the runbooks.

| Channel | Surface | Source tag | Done when |
|---|---|---|---|
| Owned surfaces | tutorial end, docs footer, changelog footer, README | `docs-quickstart-end`, `docs-footer`, `changelog-footer`, `readme-line` | each form is live with its tag |
| Public archive and share line | every issue page | `archive-issue-page` | every past issue is public |
| Item pitch (only when there's real news) | curated developer newsletters, linking a page that ends with a tagged signup line | `pitch-<curator>-<release>` | page has the line, pitch sent |
| Republishing | Medium with canonical link, LinkedIn excerpt | `republish-<platform>` | archive live, canonical set or excerpt posted |

Republishing stays last. It only fits if your hours per month can carry a standing job, and I don't know your ceiling. Under about four hours a month, nothing past talk end cards fits, so republishing would be deleted.

## Signup contract

Every new form should state what arrives, how often, and who sends it. It should link the latest issue and the privacy notice, and it should say the cadence the charter holds. A public form needs double opt-in, a honeypot, a per-IP rate limit, and a record of timestamp, source tag, form version and consent text. Report confirmed signups, never form submissions.

## Metric sheet

Report these per source tag:
- net confirmed growth
- confirmation rate per form
- first-issue click
- activation (human click in the first four issues)
- early churn (gone within three issues)
- unsubscribes and complaints per send

Baseline comes from the next two months of your own data. Don't use gross list size or open rate as growth targets. Don't rank any source on fewer than about 30 confirmed signups.

## Open questions, with owner

- **Newsletter owner:** Who owns the newsletter and the backup? Did the last three issues go out on cadence?
- **Privacy owner:** How was the 2,700 collected, single or double opt-in, and where do the subscribers live? Any import or event list in there needs reviewing.
- **Content marketer:** Does the form capture a source value today?
- **You:**
  - Do you have a public archive?
  - What is your monthly effort ceiling in hours?
  - Is there a date the growth has to land by?
- **Anyone posting the issues:** Do Medium and LinkedIn currently allow a canonical link? Verify this before the first post.

I did not run the full interview, so the gate results and the ranking are provisional until these are answered.