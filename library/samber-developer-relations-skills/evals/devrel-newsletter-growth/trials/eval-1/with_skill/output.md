# hmig changelog digest growth plan

**Answer:** Do one of your three steps as written (monthly reporting, with a different number). Reshape the other two. The 10k target can't be forecast yet, so the plan fixes consent and tagging first and sets the number after two tagged issues.

- **Step 1** (prompt after `hmig migrate`): refused. Use `hmig --help` and an opt-in `hmig community` subcommand.
- **Step 2** (import the 14,000 trials): refused. Use one in-product invite with an unticked box.
- **Step 3** (report total list size): replace it with confirmed growth per source.

⏳ This is an estimate, not a forecast. Reaching 10k from 2,300 by 2027-06-30 means about 960 net confirmed per month, about 7.5× the historical average of about 128 per month (2,300 over 18 months, gross). I assumed Q2 is calendar Q2, so please confirm that date.

## Refusals applied

| Your move | Label | Why | Instead |
|---|---|---|---|
| Prompt after every successful `hmig migrate` | Trust | Developers read an unrequested terminal prompt the same way in every ecosystem. `migrate` also runs in CI, where the extra line pollutes logs and any scripts that parse output. | One line in `hmig --help` ("News and breaking changes: <url>"). An opt-in `hmig community` subcommand that prints the newsletter, chat and docs links. A link on the docs page the CLI points to. |
| Bulk-import 14,000 trial accounts | House rule, plus law where the ToS argument applies | Account signup is not newsletter consent. Consent bundled into terms is invalid in the EU, UK and Canada, and you must prove consent per person. The import would also bury the per-source numbers. | One in-product invite on the cloud dashboard, with an unticked box. |
| Report total list size monthly | Measurement rule | Gross size keeps unconfirmed and inactive addresses. The import would "hit" 10k (2,300 + 14,000 = 16,300) with nothing real behind it. | The metric sheet below. |

- **Import exception:** if the trial accounts are US-only, or a UK/EU soft opt-in was offered at signup, the import can be lawful. That is the privacy owner's call per segment. The house rule still says no import. Where do the 14,000 live, and who owns privacy at Driftmoor?
- **Already done?** If anyone ran a test import, suppress that segment. Don't send a "do you want to stay?" email, because that email is itself marketing.

## Growth gate

| Condition | Status | Evidence / first task |
|---|---|---|
| Programme holds | **Unproven** | You are owner and Dario is backup. You say every issue shipped on time this year. Still unconfirmed: a written charter, and that the issues went out without padding. Task: confirm both, 15 min. |
| Consent known | **Unproven** | Nothing says how the 2,300 were collected (forms, imports, opt-in type, countries). Task: classify each segment and suppress any with no recorded source before counting the list. |
| Sources distinguishable | **Unproven** | Nothing says subscribers carry a source. Task: add a hidden source field to every form. |

No channel opens until the three tasks are done. Target: 2026-11-13.

## Churn reading

**Blocked.** I have no unsubscribe or complaint numbers. Please send the last six issues' unsubscribes, complaints and sends, split by subscriber tenure and source if you have it, and say what changed and when.

- **Owner:** you. **Re-check:** 2026-11-13.
- **What to read:** unsubscribes and complaints together, split by tenure, source and issue.
- **Why it matters:** 18 months in, some of the 2,300 are likely inactive. Growth sent to a list that already churns early only adds complaints.

## Signup contract (every form)

- **Promise:** "Monthly, from the hmig team: releases, breaking changes, one deep dive." Link the latest issue and the privacy notice. Write the cadence your charter holds, which is monthly.
- **Choice:** a separate, unticked box or a dedicated form. Never a condition of an account or a download.
- **Confirmation:**
  - Public forms (docs, README, changelog) use double opt-in. Expect many never to confirm.
  - The dashboard form sits behind a verified login, so use single opt-in with the full record.
- **Guard:** honeypot field and a per-IP rate limit.
- **Record:** timestamp, source tag, form version, the consent text shown, and the confirmation click.
- **Welcome:** the latest issue, and how to unsubscribe.
- **Suppression list:** unsubscribed and suppressed addresses stay on it, so no later import re-adds them.
- **Unsubscribe:** no login and no required field. An optional reason field comes after it completes.

## Ranked channels (efficiency order)

I'm recommending the first four rows. Please confirm or change before I treat them as the plan.

**Kept**

| # | Channel | Owner | Surface | Source tag | Date | Done when |
|---|---|---|---|---|---|---|
| 1 | Owned surfaces | You | Quickstart end, changelog and release-notes footer, docs footer, README, `hmig --help` line plus `hmig community` | `docs-quickstart-end`, `changelog-footer`, `docs-footer`, `readme-line`, `cli-help` | First 3 by 2026-11-30, the rest by 2026-12-31 | Forms live with tags and the contract above |
| 2 | In-product invite | You (brief), dashboard team (build) | Cloud dashboard settings, off by default | `in-product-invite` | Brief by 2026-12-15 | Toggle live, single opt-in, consent text and record stored |
| 3 | Archive and share line | Dario | Every past issue public, one share line per issue | `archive-issue-page` | 2026-12-31 | All issues public, subscribe form above the fold |
| 4 | Item pitches | You | One pitch per real hmig release, to curated Postgres and database-tooling newsletters | `pitch-<curator>-<version>` | At the next release with real news (date open) | The linked release page ends with a tagged signup line, then the pitch goes out |

- **Item pitches:** curator rules change, so use the newsletter-curators reference in `tech-press-relations` and check each curator's current page.
- **Talk end cards** (`talk-<event>-card`): add if you have a talk booked this half. Cost: 1 h per talk.

**Deleted**

- **Republishing:** a standing hour per issue that your ceiling can't carry next to the setup work.
- **Swaps:** about a week of coordination each.
- **Unpaid recommendations:** the platform feature is unconfirmed. Re-add if your sending tool has it and audiences overlap.
- **Referral programme:** weeks of setup, then a standing fraud job, on a small list.
- **Paid acquisition:** no budget stated. Re-add only with a budget and a screening rule at least as strict as your organic first-month behaviour.

**Hours (6 h/month ceiling, my estimates)**

- **Nov:** about 2.5 h for the gate fixes and contract, plus 3 h for quickstart end, changelog footer and docs footer.
- **Dec:** about 1 h for the README, 1.5 h for the CLI help line and `hmig community`, 1 h for the in-product invite brief, and 1 h for the archive (Dario). The rest is buffer.
- **From Jan:** about 2–3 h per month for pitches and the report.

Surfaces with little traffic return little. Check docs analytics and the repo traffic page to see which ones matter.

## Metric sheet (per source, confirmed only)

| Metric | Baseline | Target |
|---|---|---|
| Net confirmed growth (new confirmed minus unsubscribes, bounces, removals) | Next two issues | Set 2027-01-31, labelled a house rule |
| Confirmation rate, per form | Next two issues | Same |
| First-issue click (human click, bot clicks filtered) | Next two issues | Same |
| Activation (human click in first four issues) | Next two issues | Same |
| Early churn (gone within three issues) | Next two issues | Same |
| Unsubscribes and complaints per send | Last six issues (needed from you) | Same |
| One outcome signal, such as cloud trial signups from newsletter links | Needs your answer on what the digest is funded for | Same |

- **Rule:** never rank a source on fewer than about 30 confirmed signups.
- **Never a target:** gross list size, form submissions, open rate.
- **What to tell your VP:**
  1. "10k gross is reachable by import and worthless."
  2. "From 2027-01-31 I'll report confirmed growth per source and commit a number then."
  3. Ask what the 10k is for. If the answer is trial signups, report that.

## Open questions

1. Where do the 14,000 trial accounts live, and who owns privacy? (Decides whether any segment may join without an invite.)
2. How were the 2,300 collected, and is there a charter, a source field, and a bot-click filter?
3. Do the 6 hours also cover writing each issue? If so, nothing past the first row fits.
4. Which surfaces can you edit, and can the dashboard team build the toggle?
5. Is there a talk booked, a paid budget, or a legal review required on every new form?
6. Can Dario take the archive work?
7. What are the last six issues' unsubscribes and complaints?

## Pass-threshold check

- ✅ Every move checked against the refusal table, labelled, and given a replacement.
- ⚠️ **Blocked:** the churn reading needs question 7, owner you, re-check 2026-11-13.
- ⚠️ **Unproven:** all three gate conditions need your answers or the three tasks above. They are the first work.
- ✅ Contract, channel rows (owner, tag, date, done-when) and deletions are named.
- ⚠️ Metric baselines can't exist until two tagged issues have shipped.