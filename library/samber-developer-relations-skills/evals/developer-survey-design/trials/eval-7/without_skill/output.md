# Hollowmere Developer Survey: privacy pack

I'm not a lawyer. Have Dutch privacy counsel review this before launch, especially sections B and C.

Three of your plans can't go ahead as described:

1. **Sending Kestrelworks your newsletter list.** Don't do it.
2. **Publishing the full dataset, free text included, under CC-BY.** Don't do it.
3. **The "access or deletion at any time" sentence.** It's false once data is published.

I've written the notice around the safer version of each. Section C explains why and what to decide.

---

## A. The notice

Placeholders are in [brackets]. I've assumed the design recommended in section C.

> ### Hollowmere Developer Survey 2026: how we handle your data
>
> **1. Who is responsible**
> Hollowmere [legal name, KvK no., address, the Netherlands] decides why and how your answers are used. Contact: [privacy@…]. [Data Protection Officer: name/contact, if appointed.]
>
> Kestrelworks [legal name, country] helped design the questions. If you received the invitation from them, that is because they mailed it to their own list. They did not give us that list, and we did not give them ours. Kestrelworks receives only aggregated results, never individual answers.
>
> **2. Who can take part**
> You must be 16 or older. The first question asks your age band. If you are under 16 the survey ends and we keep nothing.
>
> **3. What we collect, why, and on what basis**
>
> | Data | Why | Legal basis (GDPR) |
> |---|---|---|
> | Role, tools, experience band, country, other core answers | Understand the developer community and publish findings | Our legitimate interest in community research (Art. 6(1)(f)). You can object. |
> | **Gender identity** (optional) | Measure who is represented in our community and plan outreach | Your explicit consent (Art. 6(1)(a), 9(2)(a)) |
> | **Disability status** (optional, health data) | Same | Your explicit consent (Art. 6(1)(a), 9(2)(a)) |
> | Free-text answers (optional) | Understand answers in your own words | Legitimate interest. Please do not write names, employers or other identifying details. |
> | Email address (only if you enter the prize draw or ask for results) | Contact you once | Consent. Stored apart from your answers and deleted [30] days after [draw date]. |
>
> Every question except [age band] is optional. You can skip any of them. You can also answer "prefer not to say" on gender and disability.
>
> **4. What we publish**
> After [publication date] we will publish a de-identified dataset under CC-BY. It contains no names, emails, IP addresses or free text. Age, country and experience are grouped into broad bands. Gender identity and disability status appear only as aggregate figures, in groups of at least [10] people, never as columns in the public file. We test the file for re-identification risk before release. Free-text answers are quoted only if you tick the separate quote box, and only after we remove anything identifying.
>
> A fuller version for researchers [is not offered / is offered under a data-use agreement that forbids re-identification].
>
> **5. Who receives your data**
> - [Survey platform, country]: hosts the survey for us under a data processing agreement.
> - [Email tool], only for the prize draw.
> - Kestrelworks: aggregated results only.
> - The public: the de-identified dataset in section 4.
>
> **6. Transfers outside the EU/EEA**
> [State where the platform stores data. If outside the EEA: name the safeguard, e.g. EU Standard Contractual Clauses or an EU–US Data Privacy Framework certification.]
>
> **7. How long we keep it**
> Raw responses: until [date, e.g. 12 months after publication], then deleted. Email addresses: see section 3. The published de-identified dataset stays online.
>
> **8. Your rights, and their limits**
> You have the right to access your answers, correct them, delete them, restrict their use, object to their use, and receive them in a portable format. You can withdraw consent for gender, disability, email and quotes at any time. Withdrawing does not affect what we did before.
>
> Practical limits:
> - The survey is anonymous, so we can only find your answers if you give us the **response code** shown at the end of the survey. Keep it.
> - **Until [publication date]** we will act on any request using that code.
> - **After publication** we can no longer tell which row is yours, so we cannot remove it from the public dataset or from copies others have made. Your raw answers, gender and disability included, are still deleted on request until the retention date above.
> - Requests: [privacy@…]. We answer within one month.
>
> **9. Complaints**
> You can complain to the Dutch Data Protection Authority (Autoriteit Persoonsgegevens, autoriteitpersoonsgegevens.nl) or to the authority in your own country.
>
> **10. Other**
> We make no automated decisions about you. Taking part is voluntary. We will date any change to this notice and say what changed.

**Consent screen for the sensitive questions.** Use this exact pattern: unticked box, shown before the gender and disability questions, separate from everything else.

> ☐ I agree that Hollowmere processes my answers about **gender identity** and **disability status**, which are sensitive data, for the purposes in section 3. I can withdraw this before [publication date] using my response code. These questions are optional, and I can skip them with no consequence.

**Age gate (first screen, nothing else collected before it):**

> This survey is for people aged 16 or older. How old are you? ○ Under 16 ○ 16–17 ○ 18–24 ○ …
>
> Under 16 → "Thanks for your interest. This survey is not open to under-16s." End the session, store nothing.

---

## B. Your draft sentence, fixed

| Draft | Problem |
|---|---|
| "you may request access to or deletion of your answers at any time" | False after open-data release. Erasure isn't absolute under GDPR. You can't locate answers in an anonymous survey without a key. It omits the other rights, the right to withdraw consent, and the right to complain. |

Section 8 of the notice replaces it. It makes two commitments you can keep: a response code, and a hard cut-off date before publication.

---

## C. Why I changed your plan, and what you still need

### 1. Newsletter list to Kestrelworks: don't

- Subscribers signed up for your newsletter. Handing their addresses to a third party for a different purpose is a new purpose (Art. 5(1)(b), 6(4)). It needs fresh consent or a compatibility case you can't make for a third party.
- Mailing them also triggers ePrivacy and Dutch Telecommunications Act rules on unsolicited electronic messages. Survey invites that promote your organisation can count as direct marketing.
- **Instead:** Kestrelworks mails its own 60k list. You mail your own newsletter list yourself, and only if your newsletter notice and consent cover "community research". If they don't, send a plain newsletter item linking to the survey instead of a targeted invite.
- Kestrelworks owns the lawfulness of its own mailing. Get that in writing, and ask where its list is based.

### 2. Open data under CC-BY: release a de-identified file, not the full one

- **Free text is the biggest risk.** People write names, employers, projects and health details. Combined with country, age, gender and disability, it makes many respondents identifiable. Disability data is special-category (Art. 9).
- **Publication can't be undone.** CC-BY puts no limit on reuse. You can't honour withdrawal or erasure once copies exist, and "anonymised" is a legal conclusion you must be able to defend (recital 26; WP29 Opinion 05/2014).
- **What to do:**
  - Drop free text from the public file, or release it only as reviewed, opt-in quotes.
  - Band quasi-identifiers (age, country, experience).
  - Keep gender and disability out of the public file at individual level.
  - Run a k-anonymity check and suppress small cells.
  - If you want a fuller file, offer it to vetted researchers under a data-use agreement.
- Document the re-identification test. If the file isn't truly anonymous, GDPR still applies to it and your notice would be wrong.

### 3. Gender identity and disability

- Disability is health data, so you need **explicit consent**, and that consent has to be freely given and withdrawable. Gender identity isn't named in Art. 9, but treat it as sensitive in practice. Its risk is high, and other jurisdictions treat it as sensitive.
- Check data minimisation. If the outreach goal only needs aggregates, don't link these answers to anything else. Ask the questions optionally, with "prefer not to say".

### 4. Children aged 15

- The Dutch consent age for children is 16, and it is the highest in the EU. A 15-year-old would need parental consent (UAVG art. 5, and GDPR Art. 8 for online services). Adding to that, you would be asking for special-category data and publishing a minor's answers.
- **Recommendation:** make the survey 16+, with the age gate above. If students under 16 matter to you, run a separate survey with parental consent, no sensitive questions and no free text. Treat it as its own project.
- Outside the EU, minors' rules differ. India's DPDP Act, for example, defines a child as under 18. Check where your respondents are, and consider restricting the survey to those regions or ages if you can't comply.
- Write the notice at a reading level a 16-year-old can follow. Section A is already close to that.
- Ask Kestrelworks whether its list includes under-16s.

### 5. Kestrelworks: controller roles

- Co-designing the questionnaire means that if they get individual-level data, you are **joint controllers** and need an Art. 26 arrangement, with its essence summarised in the notice.
- If they get aggregates only, you are sole controller. That's the version I wrote.
- Decide now, then paper it. Either way, sign a short written agreement covering: who sends invitations, who answers rights requests, who handles a breach, and what Kestrelworks may do with the results.

### 6. Worldwide respondents

- GDPR applies because you are established in the Netherlands (Art. 3(1)), whatever the respondent's country.
- Other laws can apply as well: UK GDPR, Brazil's LGPD, India's DPDP, California's CCPA and China's PIPL. Ask counsel which realistically apply to you. Geo-restricting is a legitimate option.
- Any non-EEA processor (survey platform, email tool) needs a transfer mechanism. Collecting from respondents directly is not a transfer. Hosting in the EU avoids the issue.

### 7. Documents to produce before launch

1. **DPIA (Art. 35).** Required: special-category data, minors in scope, public release, large scale. Do this first, because it drives the other decisions.
2. **Legitimate-interest assessment** for the core answers.
3. **Records of processing (Art. 30).**
4. **Processor agreements** (Art. 28) with the survey platform and email tool.
5. **Art. 26 / data-sharing agreement** with Kestrelworks.
6. **Re-identification risk assessment** for the public file.
7. **Retention and deletion schedule**, including the email list.
8. **Rights-request procedure** (response-code lookup, one-month deadline) and **breach procedure** (72-hour notification to the AP).
9. **DPO decision.** Probably not mandatory for you, but write down why.
10. **Security measures:** access control, encryption, no raw data in shared drives.
11. **Prize-draw terms,** if there's an incentive.
12. **Cookie check** on the survey page. Prefer a platform with no tracking.
13. **Ethics review,** if you want academic reuse of the data.

### 8. Survey design changes

- Generate a random response code at the end of the survey, and store the data against it. Don't store IPs.
- Collect emails in a separate form, not linked to answers.
- Add a free-text warning: "Don't include names or employers."
- Add the separate consent box for quotes.

### 9. Questions I need answered

1. Does Kestrelworks get individual responses, or aggregates only?
2. Where is Kestrelworks based, and what does its list's privacy notice say?
3. Which survey platform will you use, and where does it host data?
4. Is there a prize draw or any other incentive?
5. Does your newsletter's current privacy notice mention surveys or research?
6. Do you want the under-16 audience badly enough to run a separate parental-consent survey?