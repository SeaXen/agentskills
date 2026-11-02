# Kelpwire developer call: scope card and question form

I made three calls that go against what was asked or implied. Each is flagged below, and each is yours to overrule.

1. **The form does not ask for log or config attachments.** It asks for a short redacted excerpt and request IDs. Configs hold API keys, and logs hold other people's data. Files that reach a form inbox are hard to un-send.
2. **The call does not carry the Enterprise pitch.** Details are in the "Sales" section below.
3. **Account-specific and security topics move to private channels.** That covers the invoice dispute and the rate-table issue.

Fill in the bracketed placeholders (`[...]`) before publishing.

---

## Part 1. Scope card (public, goes above the form)

**Kelpwire developer call, every second [weekday], [time] [timezone]**

A live Q&A for people building on the Kelpwire shipping-rates API. Bring a question about how the API works, how to use it better, or what you're seeing in your integration.

**Good fits for the call**
- How an endpoint, parameter, or response field behaves
- Rate-limit, caching, and pagination patterns
- Error codes: what they mean and what to do
- Choosing between approaches (batch vs. single, webhooks vs. polling)
- Why a specific request returned an unexpected rate
- Upcoming changes to the public API and deprecation timelines
- A short walkthrough of an integration problem, using a redacted excerpt

**Not for this call. Use these instead**

| Topic | Where it goes |
|---|---|
| Invoices, charges, refunds, disputes, plan changes | Billing support: `[billing contact]`. We can't discuss account-specific money on a group call. |
| Anything that looks like a security issue, such as seeing data that isn't yours or bypassing access limits | Private report only: `[security contact]`. Never post it in the form, the chat, or live. We acknowledge reports within `[SLA]`. |
| Live debugging of your production system with full logs | Support ticket, or request a 1:1 session at `[link]`. The call is a group setting. |
| Reviewing your own code, such as custom connectors or carrier integrations | Enterprise customers: your account team. Others: support ticket. |
| Contract terms, SLAs, custom pricing | Your account contact |

**Ground rules**
- Questions are taken in the order the host judges most useful to the whole group, not first come first served.
- We timebox each topic to about [5] minutes. If it needs more, we move it to a follow-up and say where.
- Nothing said on the call is a commitment. Product plans are not promises, and a contract is the only place a commitment lives.
- Never share API keys, tokens, or credentials, and never share another party's data. If it appears on screen, we stop and ask you to remove it.
- [Recording: state yes/no here and where recordings are kept.]

**Staying useful for everyone:** "No question too small" stays. "Ask us anything" goes, because the list above is what we can actually answer in the open.

---

## Part 2. Question form

**Title:** Submit a question for the Kelpwire developer call

**Intro text:** Your answers help us prepare an accurate reply. Don't paste secrets. See the "Before you paste anything" box below.

**1. What's your question?** *(required, long text, 600 characters)*
One question or problem per submission.

**2. What kind of question is this?** *(required, dropdown)*
- How the API works
- Unexpected result or error from the API
- Best practice or design choice
- Upcoming changes / roadmap
- Billing or invoice → *redirect message shown:* "Billing questions can't be handled on the call. Please contact `[billing contact]`. We'll answer you there."
- Possible security issue → *redirect message shown:* "Please don't submit this form. Report it privately to `[security contact]`. We take these seriously and reply within `[SLA]`."
- Something else

Selecting either redirect option disables the remaining fields and submission.

**3. Which endpoint or feature?** *(optional, short text)*
Example: `POST /v2/rates`

**4. Your plan** *(required, dropdown)*
[Free / Paid / Enterprise]
*Why we ask: so we can route plan-specific questions correctly. It isn't used for prioritising.*

**5. Details that help us reproduce it** *(optional, long text)*
- Request ID(s): `[format]`
- Approximate time of the request, with timezone
- HTTP status and error message you received
- What you expected to happen

**6. Redacted excerpt** *(optional, long text, 2,000 characters, no file uploads)*
Paste the smallest snippet that shows the problem: one request, one response, or one config block.

> **Before you paste anything**
> Remove or replace: API keys, tokens, and secrets; customer names, emails, and addresses; account IDs belonging to other parties; internal hostnames.
> **Never include data from another Kelpwire account.**
> We can't review whole log files or full config files through this form.

**7. I confirm that I removed secrets and other people's data from what I pasted.** *(required checkbox, shown only if field 6 is filled)*

**8. How should we handle your question on the call?** *(required, radio)*
- Read my question aloud, and use my name
- Read my question aloud, anonymously
- Don't answer it live. Reply to me by email.

**9. Would you like to show something on screen?** *(optional, radio)*
- No
- Yes, a redacted or sandbox example. We'll follow up to agree on what's shown beforehand.

*Helper text:* "Live screen-sharing of production logs happens in 1:1 sessions, not on the group call. If you need that, choose 'Request a 1:1' below."

**10. Request a 1:1 session instead** *(optional checkbox)*
For deep dives into your integration, with your logs on screen, that wouldn't be appropriate for a group.

**11. Email for follow-up** *(required)*
Used only to reply about this question. `[link to privacy notice]`. Retention: `[period]`.

**Submit button:** Send my question

**Confirmation message:** Thanks. We'll read this before the call. If it belongs elsewhere, we'll tell you where to take it.

---

## Notes on the calls I made

- **The invoice dispute (20 minutes).** One person's account issue took a slot from everyone else. The card now sends billing to its own channel and timeboxes topics.
- **The rate-table exposure.** A live, public demonstration of a bypass is a disclosure channel we don't control. It is fixed, but the card now says where such reports go. Consider also confirming internally that the fix was verified and that affected customers were notified. That is outside this task.
- **Logs on screen.** Showing one customer's production logs to a group risks exposing their data and any third parties in it. Hence the 1:1 option, and the form's field 9 only allows redacted or sandbox material on the group call.
- **Logs and config in the form.** Narrowed to a redacted excerpt with an explicit confirmation. If you need full files for support, a ticket system with access controls is the right place, not the form.
- **Sales and Enterprise roadmap.**
  - *Why I advise against it:* The audience is mostly paying non-enterprise customers. A pitch for a tier they aren't on makes the call feel like an ad and undermines trust. Roadmap talk on a call with no commitments also invites "you said it would ship" disputes.
  - *What I included:* the "upcoming changes to the public API" item, which is useful to everyone.
  - *If sales insists:* give them a clearly labelled 5-minute "What's coming" segment at the end that covers features for all plans. Enterprise-only features go through the enterprise account team and its own channel. Whether to allow any segment is your call, so please decide before this goes out.
- **The enterprise customer's connector code.** The code is their IP and may be confidential. A group call is the wrong place to review it, and a review also implies support you may not have contracted for. It goes to their account team. If you want to help them, offer a private session.

---

## Questions for you

1. **Who owns the billing contact, the security contact, and the 1:1 booking link?** I used placeholders.
2. **Is the call recorded?** The card needs to say so either way.
3. **Do you want a "What's coming" segment for all plans?** That is the compromise with sales. I left it out of the card.
4. **Should the Enterprise plan field in the form be visible?** I included it for routing. Drop it if you'd rather not ask.