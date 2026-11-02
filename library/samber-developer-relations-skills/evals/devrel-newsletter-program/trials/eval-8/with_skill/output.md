# Marrowgate developer newsletter: template and ownership

**Answer:** formalise it as a monthly own-surface digest. Cut nine sections to six, ban unplanned filler, move billing and security notices out, and give it an organisation-held domain, an archive, and a named owner, backup and reviewer.

I couldn't run the interview, so the supply count, the owner's hours and the list's consent history are open. Where an answer is missing, I say so and don't guess. The full charter has eight sections and I wrote only the two you asked for. The gate, shape, cadence and consent are stated only where the template depends on them.

## Assumptions the template depends on

| Item | Status |
|---|---|
| Shape | Own-surface digest, monthly. This is provisional: the shape and cadence are untested until supply is counted. |
| Gate (supply, owner and backup, demand for email) | ⚠️ **Unproven.** No supply count, no named owner, no click data. The next issue is the test (see "Gate test for the next issue" below). |
| Funding reason (interview question 2) | Not given. It decides the outcome metric, so it is open. |

## 1. Section template

Six sections, fixed order. Today's nine sections are replaced; I can't map them one by one because I haven't seen them. Any old section whose content isn't in this table is cut.

| Section | Source | Owner | Items | When empty |
|---|---|---|---|---|
| Shipped this month | Public changelog | Owner (backup: Backup) | 3-5 | Drop it. If it drops and fewer than three sections are filled, do not send (see "Empty-issue rule"). |
| Changes ahead | Changelog and deprecation tracker (runner image removals, API and config deprecations, pricing-page changes already public) | Owner | 0-3 | Drop it. |
| Built by the community | Forum, public repos, community chat | Backup | 1-2 | Drop it. This counts as external content even on your own forum. |
| One thing to try | Docs walkthroughs, tagged as a pipeline or config improvement | Backup | 1 | Run the next entry from the evergreen reserve (see below). If the reserve is empty, drop it. |
| Elsewhere in CI and delivery | External articles, talks, ecosystem news | Owner | 1-2 | Drop it. |
| Where we'll be | Events calendar, office hours, community calls | Owner | 0-2 | Drop it. |

**Rules that go with the template**
- **No filler.** Nothing is written to fill a gap. The "generic tips" practice ends.
- **Evergreen reserve.** "One thing to try" draws only from a pre-built backlog. An entry qualifies only if it links to the docs or a post, and will still be true two issues from now.
- **Reserve at launch.** The reserve must hold two entries before the restart issue, and the restart issue counts as the first.
- **Own versus external share.** Aim for at least one external item in "Built by the community" or "Elsewhere" every issue. This is a house rule. No published industry ratio exists.
- **Self-promotion.** Paid or partner placements are not accepted until someone decides otherwise. If they ever are, they carry a "sponsored" label, meet the same inclusion criteria, and have a per-issue cap.
- **Exclusions:** gated content, announcements with no usage example, unannounced features, named customers without sign-off, and competitor comparisons. Confirm the off-limits list with the owner. Interview question 9 is open.

### Empty-issue rule
- **Fewer than three filled sections:** do not pad. Send a one-line hiatus note, or merge into next month.
- **Two thin issues in a row:** drop to a slower cadence, or fall back to feed only.
- **Never skip a send silently.** Always announce a pause.

### Billing and security notices: out of the newsletter
- **Why:** they are transactional, and a newsletter unsubscriber would otherwise miss a security notice.
- **US rule:** under CAN-SPAM, mixing commercial and transactional content makes the message commercial unless the transactional part comes first.
- **UK and EU rule:** receipt-style consent does not cover marketing.
- **What to do:** send these on the transactional or account stream, never in the digest.
- **Cost:** a separate send, but a send you already need, so the "save a send" saving doesn't hold.
- **Allowed in the digest:** a public status or security-advisory link inside "Changes ahead", only if it is already public.

### Archive
- **Every issue gets a public URL.**
- **Location:** a page on the Marrowgate site or docs, not only inside the sending platform. A public archive outlives the list.
- **Backfill:** export the past year of sent issues from the sending platform. Post what you can. This is a one-off task for the owner or backup.
- **Per-issue step:** publishing the URL is a line in the send checklist.

## 2. Ownership and handoff

"The devrel team" is not an owner. No one is accountable, and no one is the backup.

| Role | Who | Status |
|---|---|---|
| Owner (assembles and sends) | A named person on the devrel team | **Blocked.** Name needed from the head of devrel. Re-check: one week from now. |
| Backup (can ship an issue alone) | A different named person | **Blocked.** Same decision. The backup assembles one issue per quarter to stay practised. |
| Reviewer (reads before send) | A named person outside the owner and backup, such as an engineer or product manager | **Blocked.** About 30 minutes per issue. |
| Section editors | Owner and backup split as in the template | Set once the two names exist. |
| Hours per issue | Planning figure: about 4 for the owner, 1 for the backup, 0.5 for the reviewer | House-rule assumption, not measured. The effort ceiling in hours per month (interview question 8) is open. |

Do not issue a charter with "devrel team" in the owner field. A newsletter owned by a group has no one to notice when it slips.

### Accounts, domain and list: held by the organisation

1. 🔴 **The sending domain is registered on an ex-contractor's registrar account. This is the most urgent item.** If that account lapses, is locked or is disputed, you lose the domain and the ability to send.
   - **First:** check the domain's expiry date and who the registrar lists as the registrant. Open question: do you know it?
   - **Next:** ask the contractor to initiate a transfer or push to a Marrowgate-owned registrar account. This needs their cooperation, so ask now.
   - **After the transfer:** at least two org admins, registrar lock on, auto-renew on a company card, and DNS records managed in an org account.
   - **If the contractor can't be reached:** go through the registrar's contact process, with legal or the domain's registrant records. Don't wait for the next send.
   - **Fallback, only if the transfer fails:** a new domain on an org account. This changes sender identity, so treat it as a last resort. Authentication setup is out of scope here.
2. **Sending platform account.** Confirm it sits under a company login with at least two admins. A personal account or a personal card does not count.
3. **List export.** A copy lives in an org-owned location, refreshed quarterly.
4. **Archive.** Hosted on org infrastructure, with the org holding the credentials.
5. **Running cost.** The platform tier, the domain and the editor hours need a named budget line. The cost and the line are open. Without a budget line, the sunset table says close or downgrade before anyone pays personally.

### Runbook and handoff checklist

Keep the runbook next to the release process, in a repo or wiki the whole team can edit. It lists:
- the template table above
- the send day, the checklist, and the reviewer step
- who holds each account (names, not "the team")
- the curation rule and the exclusion list
- the pause note wording and the empty-issue rule

**Handoff checklist (run at any owner change)**
- [ ] The new owner has admin on the sending platform, the registrar and DNS.
- [ ] The list export and archive credentials are confirmed.
- [ ] The evergreen reserve holds two entries.
- [ ] The next issue date is announced, or a hiatus note is sent.
- [ ] The old owner's personal access is removed.

If the owner leaves and the backup can't take over within one cycle, send a short hiatus note, then hand over with this checklist or downgrade to feed only.

## Gate test for the next issue

Each condition is unproven, so the next issue tests it against a threshold you set now.

| Condition | Test |
|---|---|
| Supply | The next issue fills "Shipped this month" and at least two other sections without filler. Count last quarter's releases, posts, forum items and events first. |
| Owner and backup | Two named people have agreed, with hours. |
| Demand for email | Clicks per delivered email and replies for the last six issues hold at or above their own earlier level. You haven't supplied those numbers. |

If any condition fails, move to feed only or pause until it holds, and say which one failed. Feed only needs a public changelog with a feed.

## Open questions

1. **Who owns it, who is backup, who reviews?** Owner: head of devrel. Re-check: one week from now.
2. **When does the domain expire, who is the registrant, and will the contractor transfer it?**
3. **How many items did you ship in the last three months** (releases, posts, forum items, events), split own versus external?
4. **Who holds the sending platform login, the list export and the billing card?**
5. **How and when was the list collected?** Include the consent wording, whether any product signups were added, and the last six issues' clicks, unsubscribes and replies.
6. **Why does the company fund it?** This picks the outcome signal.
7. **What is off-limits** (unannounced features, named customers, legal review)?
8. **What are your nine current sections?** I need them to map each to a kept, merged or cut section.
9. **What is the monthly budget line?**

## Pass-threshold result

| Threshold | Result |
|---|---|
| Template sections have source, owner, item range, empty rule | ✅ Pass |
| Owner and backup are named people, accounts held by the organisation | ⚠️ **Blocked** on names and the domain transfer (open questions 1, 2, 4) |
| Gate states three conditions with evidence | ⚠️ Unproven, needs questions 3 and 5 |
| Cadence derived from supply and owner hours | ⚠️ Blocked on question 3 |
| Consent provenance stated, newsletter out of transactional mail | ⚠️ Transactional separation is done. Provenance is blocked on question 5. |
| Curation share and criteria | ✅ Written, as a house rule |
| Measurement and primary metric | Not in scope here. Use clicks, not opens, when you write it. |
| Pause and sunset triggers with thresholds | Partly covered in the empty-issue rule and handoff. The full table is in the skill. |