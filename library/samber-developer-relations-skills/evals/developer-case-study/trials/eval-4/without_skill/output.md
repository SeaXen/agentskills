Don't ship it as planned. The plan has a hole: pairing a fully anonymized company with a fully named, identifiable individual doesn't anonymize the company — it just moves the identifying detail from "Vantage Payments" to "Ines Duarte, staff engineer, Vantage Payments" on LinkedIn. Anyone who wants to know who "a large European payments company" is types her name into Google and has the answer in one search. Comms didn't say "don't use our name in the company-name field" — they said the company never appears in vendor marketing, full stop. A named-employee quote sitting next to specific architecture and metrics is the company appearing in vendor marketing, just laundered through a loophole. Comms cleared nothing about this specific combination, because this combination is not what they were asked to review.

Three consequences if you ship anyway:
- Vantage's comms team notices post-publish, feels routed around, and the relationship — this case study, the next one, the renewal conversation — takes the hit.
- Ines personally consented as an individual, but she likely doesn't have the authority to waive her employer's comms policy on the company's behalf. If this lands on her manager's desk, she's the one who catches it, not you.
- If there's an NDA or MSA confidentiality clause behind "never appear in vendor marketing," this could be a contract problem, not just an optics one — worth a 30-second check with whoever owns that paperwork before you ship anything.

**The move:**

1. Ship the safe version now: keep the company anonymized, keep every metric and architecture detail security already cleared, but genericize the attribution. Change the pull-quote byline from "Ines Duarte, Staff Engineer at Vantage Payments" to "a staff engineer at the company." Same words, same credibility signal (verbatim technical quote reads as authentic either way), zero re-identification path.

2. If the named quote matters enough to fight for, don't infer permission — ask for it explicitly. Send comms the literal final asset (anonymized company + Ines named + these specific metrics) and ask them to clear that exact configuration. Their original "no" was about the company name field; this is a new question they haven't answered. Draft:

   > Subject: One more sign-off before we publish — Ines's name alongside the anonymized case study
   >
   > Hi [comms contact] — quick follow-up on the case study. You'd confirmed the company name stays out entirely, and your security team cleared the metrics and architecture section as written. Separately, Ines has told us she's personally comfortable being named and quoted.
   >
   > Before we publish, we want to flag one thing directly: if we keep Ines's name and title on the quotes while describing the company only as "a large European payments company," a reader could identify Vantage through her public profile even though the company name never appears in the text. That may or may not be a distinction that matters to you — we'd rather ask than assume.
   >
   > Can you confirm whether it's fine to publish with Ines named as-is, or would you prefer we attribute the quotes to "a staff engineer at the company" instead? Either works on our end — we just want your explicit sign-off on whichever version goes out.

3. Default to publishing option 1 on your current timeline if comms doesn't respond fast enough — don't let this stall the launch. Swap in the named version later only if you get an explicit yes in writing.

4. Independent of the naming question: skim the metrics/architecture section once for uniqueness. "34% drop in fraud false-positives across 40M transactions/day in 12 EU countries" can fingerprint a company on its own, security clearance or not — security cleared it as *disclosable*, not as *unfingerprintable*. Worth one read before it goes out regardless of which attribution you pick.