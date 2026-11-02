## Verdict: stop, don't send Tuesday as planned

Both the guessed-email pattern and the BCC blast are exactly the two things this skill calls out by name as the failure modes that burn relationships and address databases for good. Here's the breakdown, and what to do instead before Tuesday.

## 🔴 The BCC blast is "spray and pray," the skill's #1 named failure mode

> "Spray and pray — One pitch BCC'd to forty addresses. Fix: 20-40 verified humans, one pitch each."

You're not doing this at 40x, you're doing it at **60x that scale** (2,400+). The skill sets the working media-map size at 20-40 people specifically because that's "small enough that one person can actually keep it verified." A purchased database seat and a scraped listicle are not a media map — they're raw material to build one from, nothing more.

What a real media map requires, per reporter, before they're on any send list:

- Last 5 bylines read, dated, and confirmed on this beat (not "covers tech" — the skill's worked bad example is exactly "writes about tech, 4M monthly readers" with a guessed address, scored by reach instead of relevance)
- Current employer confirmed on the outlet's own site
- Stated pitch preferences noted (no-pitch bios, embargo refusals, "email me not the desk")
- A **real, confirmed** contact route

Your 2,400-contact database fails all four at scale, and your scraped "top 50 devtools writers" list is from a **2024** listicle — bylines are already stale. The skill's own line: "beats drift far faster than bios, so the bylines are the truth and the bio is decoration." A person on a 2024 best-of list may have changed outlets, beats, or left journalism since.

## ⚠️ Guessed emails are explicitly banned, not just discouraged

> "Never invent a reporter, an outlet or an email address, and never guess a contact address into a pitch."
> "An unconfirmed contact is a blank field, not a hypothesis."

`firstname.lastname@outlet.com` "because that's the pattern everywhere" is precisely the skill's bad-example move — the worked bad entry has `a.rivera@bigtechdaily.com (guessed pattern)` right next to the note "the address is a hypothesis dressed as a fact." Practical consequences beyond the skill's own framing, worth flagging since you're about to act on this:

- **Deliverability**: a single send with hundreds of guessed, unconfirmed addresses will bounce hard. High bounce rate on one send tanks your sending domain's reputation — which then affects every other email you send from that domain, including product/transactional mail, for weeks after.
- **Wrong-person hits**: guessed addresses land in real inboxes that aren't the journalist — could be a namesake, a departed employee's still-live catch-all, or nobody. None of those outcomes get you coverage; some get you reported as spam.
- **GDPR** (you're in France, this matters): a purchased database + guessed addresses beyond what the database itself lawfully holds is a weaker legitimate-interest basis than a properly scoped, individually-verified press list. This is outside the skill's own scope, but worth a compliance check before a 2,400-recipient send from an EU-based sender.

## What's actually missing before you can pitch anyone

Working through the skill's steps against what you've described:

1. **Step 1 (qualify) hasn't been run.** You haven't said what the news actually is beyond "launch." "We launched" with nothing else is the skill's other named failure mode: *"Announcement mistaken for news — 'We are pleased to announce' with nothing that changed."* Score it against the five tests (newness, consequence, evidence, conflict/shift, tellability) before anything else. Fail two or more, and the honest move is no-pitch or one of the no-news alternatives (data report, defensible position, publish-and-be-found).
2. **Step 2 (angle) hasn't been chosen.** For a feature-flag GA/launch, the playbook's hook is "the problem class now solved at production scale, with a named early user and their numbers" — the trap is "announcing into a category the reader already knows with no differentiator beyond speed adjectives." If Quillrock is "another feature-flag tool," that's the trap. Do you have a named early customer with real numbers, or a genuine angle (the shift, the practitioner, the number)?
3. **Assets don't exist yet, or weren't mentioned.** Press page + briefing pack + technical proof pack (running demo, architecture explanation, comparison table including where you lose, pricing, licence) need to be live *before* the first pitch, not after.
4. **"Tuesday" isn't a timestamp.** If you want any embargo coordination: *"State day, clock time and timezone. 'Tuesday morning' is not an embargo."* Decide now: is this a lift-time send (everyone finds out at once, lowest effort) or an actual embargo (coordinated early access, needs the leak checklist — public repo, registry publish, docs deploy, changelog entry can all blow it early)?
5. **One pitch per reporter, not one pitch to everyone.** Even at the correct 20-40 scale, each pitch is written for that reporter — "why them" tied to their actual recent work, under ~150 words, with the proof links. A single BCC body can't do that for anyone.

## Concrete fix for Tuesday

- Cut the 2,400 contacts and the listicle scrape down to a **20-40 person tiered map**, built the way the skill specifies: work outward from the last 5 articles on feature-flagging/devtools infra, read bylines, confirm employer, tier by score (beat match weighted heaviest).
- Drop every guessed address. If you can't confirm a real contact route for someone, they're off the list, full stop — a blank field, not a fallback pattern.
- Nail the angle before writing a single pitch — what's genuinely new about Quillrock, and do you have a named early customer with numbers?
- Ship the press page and briefing pack (including the technical proof pack) live before send.
- Decide lift-time vs. embargo explicitly, with a stated clock time and timezone, and run the leak check if it's an embargo.

If you want, I can help build the actual 20-40 person media map from the devtools/feature-flag beat, or draft the qualification scoring for whatever Quillrock's specific news is — I just need the one-sentence version of what's actually happening Tuesday.