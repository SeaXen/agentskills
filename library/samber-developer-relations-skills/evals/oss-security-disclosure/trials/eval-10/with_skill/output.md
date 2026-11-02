**Next action (10 min):** Tell the CTO the plan is no longer "90-day coordinated". Active exploitation moves it to the fast track, and the EU CRA 24-hour clock has started, not expired. Then book a lawyer today and open the Single Reporting Platform filing.

I assumed today is Fri 2026-10-23 and that you learned of the exploitation this morning. Call that moment **T0**.

## 1. The CTO's three claims

| Claim | Verdict | Why |
|---|---|---|
| "CRA doesn't apply, it's open source." | ❌ | You sell an Enterprise edition and support contracts, so you monetise the software. Role test step 1 makes your company a **manufacturer** if the product is on the EU market. Your German and Dutch customers put it there. Open-source status protects non-commercial projects, not a company selling the product. Pure SaaS is outside the CRA, but you ship software to customers. |
| "We'd be a steward, no duty until Dec 2027." | ❌ | Steward is the fallback role, and only for entities that are *not* manufacturers. Manufacturer Art. 14 reporting applies from **11 Sept 2026**, including products already on the market. That date has passed. |
| "The 24h clock started Tuesday, so we blew it." | ❌ | The clock starts when you become aware of **active exploitation**, not at report receipt. Tuesday's report described an unexploited bug and started nothing. This morning's follow-up is the trigger. |

Even a late filing has value. The deadlines are 24 hours for the early warning, 72 hours for the notification, and a final report 14 days after a fix or mitigation exists. If you were late, you would still file now. A micro or small company is exempt from fines for missing the 24-hour early warning, but the duty itself stays.

The classification (which product, which CSIRT, whether you count as micro or small) is a lawyer's call. I'm giving decision inputs, not a legal opinion.

The fast-track plan below does not depend on the CRA. Active exploitation alone justifies it.

## 2. Why the 90 days is wrong

- The 90 days exists to shrink the window between "attackers can learn" and "users can upgrade". An attacker is already inside that window.
- The skill's rule for exploited bugs is a same-day fix, release and advisory, with downstream notice in hours rather than days.
- Your non-customer users are exposed and know nothing. They learn only at publication, so every day of embargo is a day they stay exposed.

## 3. Plan

| When | Action | Owner |
|---|---|---|
| **T0 + 1h** | Open a private advisory draft. Add a second responder. Move the thread out of email. Send the internal note (template 0). Put no detail in issues, PRs, branches, chat or CI. | Lead responder |
| **T0 + 2h** | Reply to the reporter (template 1). Ask for indicators of compromise from their logs, whether they or their employer hold a CVE, credit wording, time zone, and whether anyone else was told. Tell them a same-week fix is the plan. | Lead responder |
| **T0 + 4h** | Call the lawyer. File the CRA **early warning** on the Single Reporting Platform. It can be thin: product, active exploitation, member states affected. Don't wait for the root cause. | CTO + lawyer |
| **T0 + 4h** | Write an interim mitigation, such as a gateway config change or an edge rule that strips or rejects the header. Test it. | Engineer |
| **T0 + 8h** | Send the mitigation and indicators privately to all ~40 customers (template 7, adapted). Use their security contacts, not account managers. Start with the German and Dutch dozen, who are also CRA-relevant to you under Art. 14(8). | Support lead + security contact |
| **T0 + 24h** | Early warning deadline. Confirm it is filed. | CTO |
| **T0 + 1 to 3 days** | Fix in the private fork, with local full test suite, regression test, and backports to every supported line, including Enterprise. Send the fix to the reporter for confirmation (template 6b). | Two engineers |
| **T0 + 72h (Mon morning)** | CRA **notification**: vulnerability details, corrective measures, mitigations. | CTO + lawyer |
| **Release day** | Follow the runbook order: merge, tag and publish every line, confirm the registry serves it, publish the advisory, then release notes and announcement, then tell the reporter. Don't hold for Monday. If the fix is ready Saturday, ship Saturday. | Release owner |
| **Fix + 14 days** | CRA **final report**. The clock starts when the first corrective or mitigating measure is available, so the mitigation at T0 + 8h may start it. Ask the lawyer. | CTO + lawyer |
| **After** | CVE follow-up, ecosystem database check, 15-minute retrospective. | Lead responder |

**Hours check.** If the estimate for fix, tests, backports and review is about 24 to 40 engineer-hours across two people, it fits inside 72 hours. If it doesn't, ship the mitigation advisory first. Don't stretch the timeline.

## 4. Handling details

- **Identifier:** the bug was reproduced Wednesday and accepted, so request the CVE now through the code host's CNA. If the reporter holds one, use theirs and request no duplicate. The release never waits for the CVE.
- **Severity:** score independently, using the worst-case reasonable integration and a full CVSS 3.1 vector. Write the precondition and the Scope reasoning in prose. Do not copy the reporter's score.
- **Customer notice vs. public leak:** the 40 customers are the only people told before publication. Each recipient widens the leak surface, so share the mitigation, indicators and a release date, not the patch or trigger details. Share the patch at release time.
- **Reporter:** they are your customer's SOC. Their logs are the evidence, so keep them close, credit them as agreed, and never threaten or ask for silence.
- **Exploit safety:** read any proof of concept before running it, and run it only in a disposable, network-off environment. Don't test against anyone's live systems.
- **Where to store the incident record:** only in the private advisory draft. Don't put it in CLAUDE.md, memory files, the repo or shared notes.

## 5. Open questions

1. Which release lines are supported, and does the Enterprise edition ship from the same branches?
2. Which versions are affected? Mark anything unchecked as unknown, not safe.
3. What is the reporter's own disclosure deadline?
4. Is a workaround complete enough to publish as a stopgap?
5. Does the company count as micro or small under the CRA?
6. What exactly became known about the exploitation, and when? Record the timestamp now, because the lawyer will need it.

## 6. What to tell the CTO

- The CRA applies to the Enterprise product, and the manufacturer duties are live now.
- The clock started this morning, not Tuesday, so there is still time to file on time.
- Filing late would still beat not filing, and the penalty exposure is for staying silent.
- Moving to the fast track costs nothing legally and protects customers.

**Next:** open the private advisory draft, add the second responder, and send the internal note (template 0).