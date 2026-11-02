## The move: don't ship the plan as stated — the combination breaks the thing comms actually asked for

Stripping "Vantage Payments" from the text while keeping Ines Duarte's real name and title doesn't anonymize the company. It relocates the identifier. Anyone who reads "Ines Duarte, staff engineer" and spends ten seconds on LinkedIn gets the employer for free. Comms didn't say "don't print our name" — they said the company must never appear in vendor marketing, full stop. A named, real, searchable engineer *is* the company appearing, just one hop removed. This is exactly the failure the anonymization ladder warns about: sharpening a descriptor (or, here, leaving a fully identifying human attached to an anonymous descriptor) until the company is identifiable while still claiming anonymity. It reads as compliant and isn't, and that gap is the kind that ends a reference relationship when comms notices it after publication rather than before.

So this isn't "strip the name and ship" — it's a mismatched rung. Named-engineer-plus-anonymized-company isn't one of the five rungs for a reason: the ladder assumes company and human identifiability move together, because in practice they do.

## Where this actually lands

Rung 3 — unnamed company, identifying descriptor, metrics intact — is the right target given what's cleared. To get there cleanly, the engineer attribution has to descend with the company, not stay at rung 1:

- Company: "a large European payments company" (descriptor, not name).
- Engineer: role only — "a staff engineer on the payments team" — not "Ines Duarte."
- Quotes: still hers, still verbatim. Her personal comfort with being named covers permission to quote and attribute the *content* to her — it doesn't buy back the company's separate refusal on identity. Verbatim quotes under a role byline lose nothing security or legal already cleared.
- Architecture and metrics sections: ship as already approved — that clearance was about technical content, not about naming, so it survives the descent untouched.

What this costs: gate 3 ("a named human who will talk") softens rather than fails — there's still someone to quote, just not a name to believe on sight. Per the skill's own accounting, that's a noticeable loss, and the numbers now carry more of the study's credibility than the byline does. Worth it; it's still a real case study, not a pattern post.

## Two things to check before shipping even this version

1. **Get comms to sign off on the descriptor itself, not just the absence of the name.** Their consent-chain permission is "company name, logo, *and published wording*" — the anonymized phrase is published wording about them. Don't self-select "large European payments company" and assume silence-on-that-detail means approval. Send it as an explicit line item.

2. **Sanity-check the descriptor against the metrics that already cleared security review.** "Large European payments company" is broad, but if the specific throughput/volume numbers security already approved narrow the field to a handful of real candidates, the descriptor plus the numbers re-identifies them by elimination even with zero names anywhere. Count how many companies plausibly fit "large + European + payments" at the disclosed scale before locking the wording. If it's a short list, either loosen the descriptor or convert the tightest metric to a ratio instead of an absolute (the skill's own preference anyway — ratios travel better and survive review more often).

There's a second open item worth surfacing to the account owner, not blocking: Ines's personal yes covers her own consent, but the consent chain lists her *manager's* sign-off separately (spending the team's credibility) as a distinct permission, usually a different person and a different timeline. Confirm that's actually been asked, not inferred from her comfort — it's cheap to check now and expensive to discover missing after the draft is out.

## What to send today

Don't let this idle in inbox limbo — bound the ask and set a default, same as any approval round:

```
Subject: Case study — confirming the anonymized version before we ship

Hi <comms contact>,

Understood on the company name — it won't appear anywhere, full stop.
To keep the story intact, here's the version we'd publish instead:

1. Company: described only as "a large European payments company" — no
   name, no logo. Flagging this line for your sign-off specifically,
   since it's still published wording about you.
2. Engineer attribution: role only ("a staff engineer on the payments
   team"), not Ines's name — since naming her would make the company
   identifiable by a two-second LinkedIn lookup, which we think defeats
   the intent of point 1. Ines is personally fine being quoted; this
   is about whether her name can appear at all in this context, which
   is your call, not hers.
3. Metrics and architecture: unchanged from what security already
   cleared.

If we don't hear back by <date>, we'll publish with the descriptor and
role-only attribution above as the default, since that's the version
fully covered by what's already been approved.
```

If comms comes back and says naming Ines is actually fine notwithstanding the searchability issue — take it in writing from them, not from her — then the original plan ships as-is and this whole detour was one email. But ship on that confirmation, not on the assumption.