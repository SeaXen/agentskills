# Cinderpath Conf startup showcase: application form

**Verdict:** your list is about half right. Keep the deck and the "why you" box. Change revenue, and cut the cap table. Add the basics you'll need to contact and assess people.

## Changes to your list

| Your field | Verdict | Why |
|---|---|---|
| Company name | ✅ Keep | Required. |
| Deck upload | ⚠️ Keep, add a link option | Founders often host decks on Docsend or Notion. Accept a PDF (max 20 MB) or a URL. Require one of the two. |
| Revenue, last 12 months | ⚠️ Change | Many early-stage startups have $0, and an exact figure asks for something sensitive. Use a stage and revenue band instead (below). |
| Cap table summary | ❌ Cut | This is diligence data for investors. It doesn't help you pick stage speakers. It deters good applicants and leaves you holding sensitive data you must protect. Ask for it later, only if you run an investor-facing track. |
| "Why you" box | ✅ Keep, add a word limit | 150 words max. Without a limit you get essays. With one you get signal. |

If investors in the audience want cap-table data, say so, and I'll adjust. Even then, ask finalists only, after selection.

## Final form

**Intro copy (replaces the current site text)**
> Building something early-stage and exciting? Apply for a slot on the Cinderpath stage. It takes about 10 minutes. We review applications on a rolling basis and reply to everyone by [date].

**Section 1: You**
1. Your full name *(required)*
2. Email *(required)*
3. Your role, such as founder or CEO *(required)*
4. LinkedIn or personal link *(optional)*

**Section 2: Company**
5. Company name *(required)*
6. Website *(required)*
7. One-line description, max 140 characters *(required)*
8. Country and city *(required)*
9. Founded in (year) *(required)*
10. Team size, as a dropdown: 1–2, 3–5, 6–10, 11–25, 26+ *(required)*

**Section 3: Traction**
11. Stage, as a dropdown *(required)*: Idea or prototype / Building the product, no users yet / Launched, early users / Paying customers / Scaling
12. Revenue over the last 12 months, as a dropdown *(required)*: None yet / Under $10k / $10k–$100k / $100k–$1M / Over $1M / Prefer not to say
13. Funding to date, as a dropdown *(optional)*: Bootstrapped / Pre-seed / Seed / Series A or later / Prefer not to say
14. Best proof of traction, max 50 words *(optional)*. Examples are users, pilots, growth, or notable customers.

**Section 4: Pitch**
15. Pitch deck *(required)*: PDF upload (max 20 MB) **or** a link
16. Why you? Why should Cinderpath's audience care about your startup now? Max 150 words *(required)*
17. What would you show or say on stage? Max 100 words *(optional)*
18. Can you present a live demo? Yes / No / Maybe *(required)*

**Section 5: Consent**
19. ☐ I confirm I'm authorized to submit this on behalf of the company. *(required)*
20. ☐ I agree that Cinderpath may store my application for selection and contact purposes. *(required)* Link your privacy policy and state how long you keep applications.
21. ☐ Contact me about future Cinderpath events. *(optional, unchecked by default)*

**Confirmation message**
> Thanks, we've got your application. You'll hear from us by [date], whether it's a yes or a no.

## Build notes

- **Store data minimally.** Decks and revenue bands are business-sensitive. Restrict access to the selection committee and delete rejected applications after the event cycle.
- **Validate on the server.** Check file type and size, and run a malware scan on uploads. Rate-limit submissions and add a honeypot field or CAPTCHA.
- **Auto-reply.** Send a confirmation email with a copy of the answers.
- **Score consistently.** Rate each application against the same rubric: problem clarity, traction for the stage, audience fit, and stage-worthiness. Fields 11–14 and 16 feed it directly.
- **Open items for you:** the application deadline, the notification date, and the reviewer workflow (a spreadsheet, Airtable, or your CRM).

I can turn this into the actual implementation (HTML, a framework component, or Typeform/Tally config) if you tell me your stack.