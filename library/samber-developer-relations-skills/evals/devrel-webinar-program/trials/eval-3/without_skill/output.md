**Next action (10 min):** reply to Fjordline with the draft below. Send nothing else to anyone until the form and contracts change.

None of the three asks is a flat no. Each one needs a per-recipient consent checkbox, a contract clause, and a split of who sends what. The 1,900 old registrants can't be shared.

I assumed GDPR applies (EU or UK registrants). I haven't read your old privacy notice or either contract. Have counsel review the final wording. This is a setup plan, not legal advice.

## Rules behind every answer

1. **Each recipient is a separate party.** Fjordline and Northgate each get their own named, unticked, optional checkbox. One bundled "share with partners" box is not valid consent.
2. **Registration never depends on a box.** Only people who tick get shared.
3. **Old data keeps its old purpose.** The 1,900 registered under your notice only. A new recipient is a new purpose.
4. **After sharing, the recipient is an independent controller.** They send from their own domain, with their own unsubscribe. Their duties go in a contract.

## 1. Registration form

1. Keep required: name, work email, company, role. Purpose: run the episode and send logistics.
2. Add three optional, unticked checkboxes, each with a link to the recipient's privacy notice:
   - **Tidewater:** "Send me Tidewater product news and future episode invites."
   - **Fjordline:** "Share my name, work email, company, role, cloud provider and monthly cloud spend with Fjordline Cloud so they can email me about hosting."
   - **Northgate:** "Share my name, work email, company and role with Northgate Tooling so they can contact me about their products."
3. **Reveal the two new fields only when the Fjordline box is ticked.**
   - They exist for Fjordline, so collecting them from everyone is over-collection.
   - Make both optional, with a "prefer not to say" choice.
   - Use bands for spend (for example `<$1k`, `$1k–10k`, `$10k–50k`, `$50k+`), not free text.
   - Use a dropdown for provider, plus "Other" and "None / on-prem".
4. Put a short notice above the submit button. It names Tidewater and Fjordline as co-hosts, says the sponsor is Northgate, and links both privacy notices.
5. Store per registrant: each consent flag, timestamp, form version, and the exact checkbox text. You need this to prove consent and to filter exports.
6. Update your privacy notice. Add:
   - the recipients, the purposes, and the legal basis for each;
   - retention periods and the rights contact;
   - transfers outside the EEA, if Fjordline or Northgate sit outside it.
7. If your registration platform processes the data for you, confirm a data processing agreement (DPA) is in place.

**If you sell into the US:** sharing data with a partner for value can count as a "sale" under state privacy laws. That means notice plus an opt-out. Ask counsel.

## 2. Fjordline's three asks

| Ask | Answer |
|---|---|
| Add 'current cloud provider' and 'monthly cloud spend' | Yes, as above: optional, shown only after the Fjordline box is ticked, spend in bands. |
| Full registrant CSV 24h after the session | **No to "full".** Yes to the opted-in rows only, minimal columns, sent by secure link. Everyone else reaches them only as aggregate counts. |
| Fjordline runs the follow-up sequence | **Split it.** See below. |

**CSV columns for Fjordline:** name, work email, company, role, provider, spend band, consent timestamp, and attended yes/no. Include attended only if the Fjordline checkbox text mentions it. Never include the Tidewater-only or Northgate-only flags.

**Aggregates for the non-consenters:** for example, "62% of registrants use AWS". That keeps their partnership case without any personal data.

**Follow-up split:**
- **Tidewater** sends the event follow-up to all attendees: recording, slides, next episode. Send it from your own domain.
- **Fjordline** emails only the consenters. The email must come from Fjordline's domain, name Fjordline as the sender, say where they got the address (the episode), and carry a one-click unsubscribe.
- **Lowest-risk alternative:** you send Fjordline's content to the consenters yourself. No data transfer, so no transfer risk. Offer this if their paperwork lags.

**Contract with Fjordline (a co-hosting data clause):**
1. State each side's role. Both are likely independent controllers. If you jointly decide purposes, use joint-controller terms.
2. Fjordline uses the data only to contact those people about its hosting services.
3. Fjordline honors opt-outs, deletes on request, and passes erasure and unsubscribe requests back to you within a set number of days.
4. Fjordline deletes unused data after a fixed retention period, for example 12 months.
5. Fjordline does not resell or share the data, and secures it.
6. If Fjordline is outside the EEA, add standard contractual clauses (SCCs).
7. Say who bears the cost if either side's breach causes a claim.

Also check the co-host agreement for sponsor exclusivity before you sign Northgate.

## 3. Northgate ($6k sponsor)

"Sponsor receives attendee list" would promise every registrant's data. You can't deliver that. Replace it with this clause:

> Tidewater will provide Sponsor, within [X] business days after the episode, a CSV of the name, work email, company and job title of registrants who affirmatively opted in to sharing their details with Sponsor. Sponsor receives no other registrant data and no data from registrants who did not opt in. Sponsor will use the data solely to contact those individuals about [product category], acts as an independent controller, will honor opt-outs and applicable law, and will not sell or share the data further. Tidewater makes no commitment on the number of opt-ins.

Tell Northgate now that the list will be a fraction of registrants. A surprise on delivery day costs you the $6k relationship.

Offer them extras to make up the gap:
- a sponsor slide or short talk segment;
- their own link in the post-event page and email, so they collect their own leads;
- an opt-in giveaway entry;
- aggregate audience stats (roles, company sizes).

Never give Northgate Fjordline's columns (provider, spend). They are consented for Fjordline only.

## 4. The 1,900 previous registrants

**Do not give them to Fjordline.** Those people registered under your notice only. Sharing them with a hosting company is a new purpose they never agreed to. Because it is sharing, a quiet "we updated our notice" doesn't fix it.

1. **Check the old notice** first. Did it say you'd email about future episodes? Remove everyone who unsubscribed, bounced, or complained.
2. **Invite only those you are allowed to email.** Send the invite from Tidewater. Mention Fjordline as co-host, and link to the new form.
3. **Let them opt in on the new form.** Anyone who ticks the Fjordline box becomes shareable. Everyone else stays private.
4. **Expect a small share to opt in.** That is the point. It's the only version of this plan that holds up if a registrant complains.
5. If the old notice did not cover future-episode emails, get counsel's view before step 2.

## 5. Order of work

| # | Task | Time |
|---|---|---|
| 1 | Reply to Fjordline (draft below) | 10 min |
| 2 | Rewrite the form and notice, add consent logging | ½ day |
| 3 | Draft the Fjordline data clause | 2–3 h |
| 4 | Redline the Northgate clause and email them the opt-in caveat | 1 h |
| 5 | Clean the 1,900 and send the invite | ½ day |
| 6 | After the session, filter the CSV by consent flags, send two separate exports | 30 min |

Counsel review of 3 and 4 adds a few days of calendar time. Start it before the form goes live.

## Draft reply to Fjordline

> Thanks. We're glad to co-host and to add the two fields. To stay compliant, the form will show them only when a registrant ticks an opt-in to share with Fjordline, and spend will be a band. After the session you'll get a CSV of those opted-in registrants plus aggregate stats on everyone else. You can run your follow-up sequence to the opted-in contacts from your own domain, with your own unsubscribe. We'll cover roles, opt-out handling and retention in a short data clause. Can you send your privacy notice link and the name of your data protection contact?

**Next:** send that reply. Then tell me the two things I assumed: where Tidewater and Fjordline are based, and what your current privacy notice says about future-episode emails. With those, I can tighten the form text and the Fjordline clause.