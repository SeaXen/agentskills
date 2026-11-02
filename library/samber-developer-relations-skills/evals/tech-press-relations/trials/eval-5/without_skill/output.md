Here's the complete rundown, organized by risk — with what to change for Tuesday.

## ⚠️ Legal exposure

**The guessed emails are the biggest problem.** Generating `firstname.lastname@outlet.com` at scale across contacts you don't have a real address for is functionally the same pattern CAN-SPAM's "aggravated violation" provisions (15 U.S.C. §7704(b)) describe as a **dictionary attack** — combining names into permutations to construct addresses you weren't given. Enforcement against small senders is rare, but this isn't a gray area worth testing, and it's trivial to avoid.

- ❌ Don't send to any address you constructed rather than sourced.
- ✅ Run the full list through a verifier (NeverBounce, ZeroBounce, Hunter) and only keep addresses that come back as real. Drop the rest — don't guess a replacement.

**GDPR/PECR for any UK/EU journalists on the list.** Unsolicited commercial email to an individual (a journalist's named inbox counts, even if it's work email) generally needs consent or a narrow "existing relationship" exception — buying a database or scraping a listicle doesn't create either. Low enforcement risk against a single small company, but it's the kind of thing that turns into a bad tweet ("startup spammed my GDPR-protected inbox") faster than it turns into a fine.

- ✅ For EU/UK contacts, only keep ones sourced with a legitimate public press contact (a masthead/contact-page email), not scraped bylines.

**CAN-SPAM formatting, even though this isn't classic spam.** If you send it as one BCC blast, you still need: a real physical postal address in the footer, a working one-click opt-out, a truthful subject/from line, and you must honor opt-outs within 10 business days. Most PR sends skip this because they're not doing a 2,400-person blast — you are, so it applies.

## ⚠️ Deliverability — this will damage your sending domain

- A single message BCC'd to 2,400 addresses will hit per-message recipient caps on most providers (Gmail caps around 500/message) and reads as a textbook spam signal to every mail filter on the receiving end.
- Guessed addresses typically bounce at 20–40%+. A bounce spike that large on launch day will tank your domain's sender reputation — including for your product's transactional email, which rides the same domain.
- ✅ Send launch PR pitches from a dedicated subdomain, not your primary sending domain, so a bad send can't poison anything that matters long-term.
- ✅ Send as individual mail-merged emails (proper ESP or PR tool), never one message with hundreds of BCC recipients.

## ⚠️ The list itself is mostly noise

2,400 tech journalists is not 2,400 people who cover feature-flag/devtools infrastructure — realistically that's a few dozen to ~150 people. A 2024 "top 50 devtools writers" listicle is already stale: writers move outlets, go freelance, or stop covering the beat, which is exactly why the guessed-email failure rate will be high on that segment specifically.

- ✅ Filter by beat first (feature flags, platform engineering, devtools, dev experience). Ignore the rest — mass volume doesn't help you here, it just burns reputation for zero pickup.
- ✅ Verify each listicle byline is still active at that outlet before pitching (quick check of their last 5 articles) — this also tells you if they even still cover this space.

## ⚠️ PR effectiveness — the blast defeats its own purpose

A generic BCC blast fails almost every item on the standard pitch-quality bar: no personalization, no evidence the journalist covers this beat, no way for them to tell it wasn't sent to 2,399 other people. Journalists who get mass-BCC'd routinely mark it spam, publicly call it out, and remember the company name for the wrong reason — the opposite of what a launch pitch is for. It can also get your media-database seat suspended: most vendors (Cision, Muck Rack, Prowly) prohibit BCC/batch-blast use in their ToS specifically because journalists report it.

## ✅ What to do instead for Tuesday

1. **Verify the list** — strip anything unverified/guessed. Expect the addressable, relevant, real list to be a fraction of 2,400.
2. **Tier it**: top 20–30 beat-relevant journalists get individually written pitches referencing their recent work (no BCC, no template feel). Next tier gets a personalized mail-merge (subject + opener customized per beat) sent as individual messages via a proper tool. Everyone else — skip, or point them to a public press release instead of a direct pitch.
3. **Stand up a press page** at launch with the one-paragraph company description, founder bio, logo pack, screenshots, and a real `press@quillrock.com` contact — so the journalists who do respond can self-serve assets fast.
4. **Send from a dedicated subdomain**, include a real postal address and working opt-out, and monitor/honor replies.
5. If you want broad reach beyond the tiered pitch list, use a wire service or your own newsroom post for the announcement — that's what mass distribution is for, not BCC.

Net effect: fewer emails, dramatically higher chance any of them turn into coverage, and no domain/legal cleanup after launch week.