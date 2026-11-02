# Ratchet's AI-drafted dev.to posts: what to change

**Short answer:** yes, change four things. You can keep 3 posts a week, but the number depends on whether each post passes a real review. A PM skimming doesn't count as one.

I did not check dev.to's live policy text in this session. Confirm the AI-content and promotion guidelines before you roll this out. As I recall them, they require disclosure of AI assistance, a human in the loop, and posts that aren't purely promotional.

## What's wrong today

1. **No AI disclosure.** dev.to's guidelines on AI-assisted posts ask authors to say so, usually at the top of the post. Unflagged AI posts risk being unpublished or the account being restricted. Because the posts run from engineers' personal accounts, the penalty falls on them, not on Ratchet.
2. **No affiliation disclosure.** Engineers posting about their employer's product, with a CTA to its pricing page, are advertising. A reader can't tell that. Several legal regimes also require the disclosure:
   - **US:** the FTC Endorsement Guides, 16 CFR 255, require employees to disclose their material connection.
   - **EU:** the Unfair Commercial Practices Directive prohibits undisclosed advertorial content.

   Ask legal to confirm what applies to you.
3. **Engineers are named as authors of text they didn't write or check.** This is a consent and reputation risk for them. If a post has a wrong claim or insecure sample code, it carries their name. It also looks like a fake-grassroots pattern.
4. **The review step is too weak.** Ratchet is an API platform, so readers will copy your code samples. A PM can't catch invented endpoints, wrong parameters, outdated auth flows, or broken snippets. LLM drafts get these wrong often.
5. **The pattern looks like spam.** Many accounts post similar structure, tone and the same pricing CTA on a fixed schedule. dev.to moderation and readers will notice. A hard pricing CTA at the end of a tutorial also converts poorly with this audience.

## Changes to make

### 1. Account structure
- Create a **dev.to Organization** for Ratchet. Put the company-drafted, promotional-leaning posts there.
- Keep personal accounts for posts the engineer actually authored or substantially rewrote, with their consent. Engineers can opt out with no penalty.
- Set `canonical_url` to your own blog or docs if you republish there. That avoids duplicate-content problems.

### 2. Disclosure (put it in a template)
- **Top of post, when AI helped draft:** "Drafted with AI assistance; reviewed and edited by [name]."
- **Bottom of post, or near the CTA:** "I work at Ratchet." Use a plain sentence, not a hashtag.
- Add `#ai` or whatever tag dev.to currently asks for, if one exists.

### 3. Review gate (replace "PM skims")
Each post needs two sign-offs before publishing:
- **Technical reviewer, an engineer who knows the topic.** They run every code sample against the real API, check that endpoints, limits and error codes match current docs, and check for security problems such as keys in examples. They also confirm the claims are true.
- **Editorial approver (the PM, as now).** Checks for voice, a real point of view, and no internal or customer information. Anything the LLM invented about customers, benchmarks or roadmap gets cut.

The named author must read and approve the post. If they haven't, it doesn't go under their name.

### 4. Content and CTA
- Make each post useful without the product: a real problem, a worked example, and a specific opinion or measured result. A prompt-and-publish "10 tips" post fails this test.
- Add something the model can't invent: a real incident, a benchmark you ran, or a design decision the team made. Have the engineer supply it before drafting.
- Replace the pricing CTA with one relevant to the post, such as a quickstart, docs page, or the free tier. Link pricing only on posts about cost or plans.
- Use one UTM per post so you can measure which posts bring signups.

## Keeping 3 posts a week

Volume isn't the issue. Rate of unreviewed content is. A workable mix:

| Slot | Source | Account | Gate |
|---|---|---|---|
| 1 | Engineer-written (AI for outline or edit only) | Author's personal | Peer technical review |
| 2 | AI-drafted, engineer-rewritten | Author's personal, disclosed | Technical review plus PM |
| 3 | Company or product content (release notes, how-tos) | Ratchet org | Technical review plus PM |

If reviewers can't keep up, drop to 2 posts a week rather than skipping the technical review. A bad post that gets flagged or corrected publicly costs more than a missed slot.

## Before the next batch
1. Ask each engineer whether they consent to this program. Document it.
2. Ask legal to confirm the disclosure wording for your markets.
3. Write the disclosure and review checklist into the content team's template.
4. Run the technical review on the posts already live. Fix or unpublish any with broken samples, and add disclosure lines retroactively.
5. After 4 to 6 weeks, compare engagement and signups by slot. Move volume toward the slot that works.