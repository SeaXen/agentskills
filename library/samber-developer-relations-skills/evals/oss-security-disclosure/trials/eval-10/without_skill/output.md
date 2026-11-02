# skerridge header-injection plan

**Next action (2 min):** write down the timestamp of this morning's follow-up email. It is your T0. Then tell your CTO that the plan below replaces the 90-day timeline.

I'm not your lawyer, and my CRA knowledge stops around mid-2026. Get EU counsel on the phone today. Verify the article numbers and ENISA platform status below against current text before you file.

## Where the CTO is wrong

1. **"CRA doesn't apply because open source."** Wrong.
   - The CRA exempts only non-commercial open source. Recital 18 counts paid editions and paid technical support (beyond recouping costs) as commercial activity.
   - You sell an Enterprise edition and support contracts, so you are a **manufacturer** under Art. 3. At minimum the Enterprise edition is in scope.
   - A company that develops the open-source code and monetizes it is a manufacturer for that code too. Don't count on the community edition being carved out.
2. **"Steward, no duty until December 2027."** Wrong twice.
   - "Open-source steward" (Art. 3, Art. 24) is for entities that support open source without being its manufacturer, such as a foundation. You aren't one.
   - The reporting duty in Art. 14 has applied since **11 September 2026**. December 2027 is when the rest of the CRA applies, such as conformity assessment and the Art. 13 obligations.
   - Art. 69(3) also pulls products placed on the market before December 2027 under Art. 14. Verify this.
   - Even a real steward is bound by Art. 14(1) and (3) when it is involved in development. Verify this.
3. **"The 24-hour clock started Tuesday, we blew it, no point."** Wrong.
   - The Art. 14 trigger is an **actively exploited vulnerability** (Art. 3: reliable evidence that a malicious actor exploited it without the system owner's permission). Tuesday's private report had no exploitation evidence.
   - Wednesday's reproduction confirmed a vulnerability, not exploitation.
   - Today's customer logs are the first evidence of exploitation, so awareness starts at T0.
   - Assume lateness is the worst case, and document it honestly. A late report is far better than none. Silence adds a second breach of Art. 14 on top of the first. Fines for Art. 13 and 14 breaches reach €15M or 2.5% of worldwide turnover.

## The 90-day timeline is dead

Active exploitation means the coordinated-disclosure norm shifts to days. Tell the reporter now. The 90 days stays only as an outer bound for any sibling bugs found during the fix that nobody has exploited.

## Timeline (T0 = this morning's email)

1. **T0 to T+2h: set up.**
   - Name one incident lead and one scribe.
   - Start a timeline log with exact times for Tuesday's report, Wednesday's repro, and today's email. Never rewrite it. The regulator will see these dates.
   - Call counsel.
   - Reply to the reporter. Ask for IoCs, log samples, the exploit shape, and what disclosure timing they want. Confirm you treat this as an incident.
2. **Decide the CSIRT (T+2h to T+4h).**
   - Art. 14(7) sends the report to the CSIRT of the Member State of your **main establishment**. Where your customers sit (DE and NL) does not decide this.
   - Tell me where the company is established and I can narrow it. If you have no EU establishment, fallback rules apply, so ask counsel.
3. **T+24h at latest: early warning.**
   - File on the ENISA Single Reporting Platform. It goes to the CSIRT and ENISA at the same time.
   - Content is light: actively exploited, suspected malicious act, Member States where the product is available. File it even if parts are unknown.
   - If the platform isn't reachable, contact the CSIRT directly and keep proof of every attempt. Verify platform status.
   - Don't wait to "finish confirming". Confirm Wednesday's repro matches the customer's logged payload, then file. An early warning can be updated, but you can't undo a missed deadline.
4. **Parallel from T+2h: mitigation first, patch second.**
   - Target a config-level mitigation in 24 to 48h. For example, reject or strip CR/LF in header names and values at the edge, and ship it as a documented rule.
   - Target a patch in 3 to 7 days.
   - Fix at the root by normalizing and validating headers at the sink. Audit every similar sink.
   - Cover every supported branch, the open-source build and the Enterprise build.
   - Add regression tests built from the exploit payload.
   - Hunt for exploitation across your own infrastructure and any telemetry you hold.
5. **T+72h: vulnerability notification.**
   - Include: nature of the bug, exploit details, corrective or mitigating measures, and how sensitive the information is.
   - Mark it sensitive. The CSIRT and ENISA decide further dissemination.
6. **Advisory and customer notice.**
   - Art. 14(8) requires you to inform impacted users without undue delay, and all users where appropriate, with mitigations.
   - Use a private GitHub security advisory and request a CVE.
   - Notify all ~40 support customers at the same moment as the public release. Don't give a long private head start, because it leaks.
   - Give the dozen DE/NL customers what they need for their own NIS2 reporting: IoCs, a timeline, and a contact.
   - Security fixes must be **free of charge** and public (Art. 13). Don't gate the patch behind Enterprise or support.
7. **Within 14 days after the fix or mitigation ships: final report.**
   - Include severity, impact, what is known about the attacker, and the fix details.
8. **After that:** post-mortem, a published `SECURITY.md` and disclosure policy, and a gap list for the December 2027 obligations (SBOM, vulnerability handling process, support period).

## Open questions

1. Where is the company's main EU establishment?
2. Is the ENISA reporting platform reachable today?
3. Do you hold telemetry from Enterprise deployments, or only customer-sent logs?

**Next:** answer question 1. Meanwhile, send the reporter the reply from step 1.