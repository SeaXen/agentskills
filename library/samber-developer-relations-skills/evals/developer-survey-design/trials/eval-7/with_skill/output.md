# Privacy pack: Hollowmere Developer Survey

**Not legal advice.** Have your data-protection contact sign off before launch. The Netherlands, GDPR and the Autoriteit Persoonsgegevens (AP) are the anchor because you are a Dutch company. I couldn't check anything outside the skill's references.

## 1. Five problems in the brief

| # | Problem | Fix |
|---|---|---|
| 1 | You plan to send your newsletter list to Kestrelworks. Passing a list to another organisation needs consent for that specific transfer, and a generic "third parties" clause doesn't cover it. | Don't send it. You email your own list yourselves. Kestrelworks emails its own 60k. Each link carries a source tag (`newsletter`, `partner_kestrel`). |
| 2 | Your draft says "you may request access to or deletion of your answers at any time." That promise is false for this design. | Use the rights text in section 4. Without identifiers, nobody can find a row after submission. After a CC-BY release, nobody can pull the data back. |
| 3 | You want to release the full dataset, free text included. Free text can't be anonymised reliably, and the skill's rule is to never publish raw open text. | Release closed-question data only, coarsened. Publish coded themes and vetted quotes for the free text. |
| 4 | Disability is Article 9 health data. Gender identity is treated as sensitive by this skill's policy. Both need explicit, separate, unticked consent and an "optional, prefer not to say" design. | See the consent block in section 4. Neither goes into the open dataset at row level unless it passes the anonymity tests in section 6. |
| 5 | Some students are 15. The default age floor is 16, and 18 when sensitive items are asked. Under GDPR Art. 8 the consent age is 16 unless a member state lowers it. I believe the Netherlands keeps 16, but confirm with your data-protection contact. | Age gate at 16+. Gate the identity block at 18+. See section 5. |

**Re-ranking block (answer 9):**

```
Answer 9 (Dutch organisation, worldwide respondents, partner co-running): Step 7 promoted to release blocker.
Answer 9 (partner list request): list import deleted; partner-sent invitations only.
Answer 9 (no incentive stated): none assumed; prize draw stays last on compliance cost.
```

## 2. Legal basis per purpose

| Purpose | Basis | Notes |
|---|---|---|
| Core survey, aggregate results | Legitimate interest (Art. 6(1)(f)), with a written balancing test and an opt-out | The opt-out is "stop at any time". The test must weigh the 16–17 year-olds. Your data-protection contact may prefer consent instead. Then withdrawal must be as easy as giving it. |
| Gender identity and disability | Explicit consent (Art. 9(2)(a)) | Separate unticked box. Skipping the block jumps past it. 18+ only. |
| Results email or follow-up contact | Consent | Separate form, separate store. |
| Open dataset | None needed if truly anonymous | You must pass the three tests in section 6. Any row-level release of sensitive or verbatim data needs per-row consent. I don't recommend that. |
| Kestrelworks receives data | Aggregates and the public dataset only | Raw rows stay with you. See the controller arrangement in section 7. |
| Fraud hash of IP | Not collected | No public incentive. Switch IP logging off in the tool. |

## 3. Data map

| Store | Contents | Who reads | Deleted when |
|---|---|---|---|
| Response table | Answers, source tag, timestamps, random receipt code. No name, email or IP. | 2 named analysts | Raw rows by `<close + 60 days>`. Anonymised extract kept. |
| Contact form (optional) | Email and purpose (results or follow-up) | 1 named person | After the mailing or follow-up |
| Platform logs | IP, user agent | Processor | Per the DPA. Switch IP storage off. |
| Invitation tokens (calibration group, if used) | Token, used or unused. No answers. | 1 named person | At close |
| Open dataset | Coarsened closed answers. No free text, no receipt code. | Public | Never. It is irrevocable. |

There is no join key between the response table and the contact form. The receipt code is the only link. It lives with the respondent and in the response row, and you drop it at release.

## 4. Deliverable: texts to paste

### Age gate (right after the notice, before Q1)

> This survey is for people aged 16 or older. How old are you?
> ( ) Under 16  ( ) 16–17  ( ) 18 or older  ( ) Prefer not to say

- Under 16 or "prefer not to say": show "Thanks for stopping by. This survey is for people 16 and older. We stored nothing about you." plus a link to the community page.
- Use the answer for routing only. Don't store it.

### Privacy notice (page 1)

> **Who runs this survey.** Hollowmere `<legal name, address>` and Kestrelworks `<legal name, country>` run it together. We decide jointly why and how your answers are used. Contact for everything: `<privacy@…>`.
>
> **Why.** To decide `<decisions in plain words>` and to publish aggregate results in `<month>`. We also release an anonymised dataset (see below).
>
> **Legal basis.** Our legitimate interest in understanding our community. You can stop at any time. Incomplete answers are deleted. The identity questions near the end rely on your explicit consent instead.
>
> **Who can answer.** People aged 16 or older. The identity questions are for people aged 18 or older.
>
> **What we collect.** Your answers and the link you came from. We don't ask for your name or email, and we don't store your IP address. Free-text answers can contain personal details, so please leave out names and employers. `<Survey tool>` stores the data in `<EU region>` under a data-processing contract. It sets no tracking cookies.
>
> **Who sees it.** `<Two analysts>` at Hollowmere. Kestrelworks receives aggregate results and the public dataset, not individual answers. `<Kestrelworks>` sent you this link from its own mailing list. We never received that list.
>
> **What we publish.** Charts of totals. Groups under 10 people are merged. We quote free-text answers only after removing names and identifying details. We release an anonymised dataset of closed-question answers under CC-BY 4.0, with ages, regions and similar details grouped into bands. It contains no free text and no identity answers. **Once released, it can't be recalled.**
>
> **How long.** Raw answers are deleted by `<date>`. Anonymised statistics and the open dataset are kept indefinitely.
>
> **Your rights.** We don't know who you are, so we can't look you up by name. At the end you get a random receipt code. Until `<deletion deadline>`, send us that code and we will show you or delete your answers. After that date your answers become anonymous statistics and we can no longer find them (GDPR Art. 11). You can also object to the processing or complain to your data-protection authority, in the Netherlands the Autoriteit Persoonsgegevens. We don't use your answers to sell anything or to market to you.

### Identity block (18+ only, last section)

> The next two questions are about your identity. They help us see whether the community reaches everyone. They are optional. We report them only as totals for groups of 10 or more. They are never in the open dataset at individual level.
>
> `[ ]` I agree to answer these questions *(unticked; skipping jumps past the block)*
>
> Gender: Woman / Man / Non-binary / Prefer to self-describe `[ ]` / Prefer not to say
> Disability or long-term health condition that affects your work: Yes / No / Prefer not to say

- Self-describe text is never released.
- Withdrawal works through the receipt code, before the deletion deadline.

### Thank-you page

> Your receipt code: `<random code>`. Keep it if you might want to see or delete your answers before `<date>`.
> Want the results? `<separate email form>`.

## 5. Students and the age gate

- You lose 15-year-olds. Say so in the bias sentence: "under-16s are not represented."
- 16–17 year-olds answer everything except the identity block. Outreach measurement among young students is therefore blind. Name that gap in the report.
- The gate is a self-declaration and easy to bypass. That's acceptable if you don't push people to lie. Don't reward completion.
- If you want to include under-16s, that is a separate youth track. Parental consent, no identity questions and no open data would apply. It's a larger project than a gate, so I recommend against it for this edition.
- Reading the skill's "18 when sensitive items are asked" as a block-level gate is my interpretation. Confirm it with your data-protection contact.

## 6. Open-data and suppression rule

**Suppression rule.** Merge or suppress any published cell, chart slice or dataset combination under 10 respondents. This is a defensible convention, not a regulator's number. Your analysis minimum (self-set, higher) applies to subgroup comparisons.

**Before release, test three things on the coarsened dataset:**
- Can someone single out a row?
- Can someone link it to another dataset?
- Can someone infer a sensitive value?

Coarsen bands until all three fail. Apply the 10-person floor to every combination of country or region, age or experience band, role, organisation size and gender.

**Decision for you.** Gender × disability × region × role × org size will almost certainly fail on a few thousand respondents.
- Default: keep both identity answers out of the dataset and publish them as aggregates only.
- If you want them in, coarsen until the test passes, then ask your data-protection contact whether per-row consent is also needed.

**Free text:**
- Release coded themes plus vetted quotes.
- Read every quote for names, employers, products and incidents.
- Don't release verbatim text, even for respondents who opt in. Search engines defeat redaction.

**Licence.** CC-BY 4.0 on the dataset and a data dictionary. The notice already warns that release is irrevocable.

## 7. What else you need

1. **Decision-table rows for gender and disability.** Name the decision, the owner and the answer that would change it (skill Step 1). If there is no row, cut the questions. An outreach goal can sometimes be measured differently, for example through partner-channel reach.
2. **Controller arrangement with Kestrelworks.** They co-design the questionnaire, so treat them as joint controllers (Art. 26) unless your data-protection contact says otherwise. Write down who answers rights requests (one contact point), who publishes what, and that raw rows stay with you.
3. **Kestrelworks' mailing basis.** Get written confirmation that their list permits a research invitation, and that the email carries no promotion.
4. **Your newsletter list.** Check the original signup wording. Send the invitation yourselves, with no promotion and a working unsubscribe.
5. **Impact assessment screening.** Sensitive items, microdata release and 16–17 year-olds make a DPIA likely. Ask your data-protection contact.
6. **Written legitimate-interest balancing test.** It must weigh the 16–17 year-olds and the open-data release.
7. **Processor contract with the survey tool.** Use an EU region, switch off IP logging, set no analytics cookies, and confirm it can route and carry hidden source fields. If any processor sits outside the EEA, document the transfer mechanism.
8. **Worldwide respondents.** Other regimes may apply (for example UK GDPR, Brazil LGPD or Canadian rules). Ask your data-protection contact which ones, and whether you need a representative anywhere. I haven't verified this.
9. **Records of processing (Art. 30), a breach procedure and a rights-request log.** Add deletion dates to a calendar for the receipt-code deadline, the raw-data deletion and the contact-form deletion.
10. **Language.** A notice nobody can read isn't informed consent. Translate the notice and the survey, or name the language gap in the bias sentence.
11. **Dates.** Fill in the close date, deletion deadline, release date and raw-data deletion date. A workable sequence is close → +30 days (receipt-code deadline) → +45 days (dataset release) → +60 days (raw rows deleted).
12. **Pilot checks.** Test the age gate on a phone, confirm under-16s leave nothing stored, confirm the identity block skips cleanly, and check that no IP or cookie appears in the export.

## 8. Open questions I assumed

- No incentive, no sales lead capture, and Kestrelworks gets aggregates only.
- Your legal entity name, survey tool and hosting region are placeholders in `<…>`.
- The opt-in for the receipt code is automatic, not optional. Tell me if you'd rather drop the code and say plainly that answers can't be retrieved.

The next artefact in the skill's order is the analysis and publication plan. It carries the cleaning rules, the chart caption template and the methodology draft.