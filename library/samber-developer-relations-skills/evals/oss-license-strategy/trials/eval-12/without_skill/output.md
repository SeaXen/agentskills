Samuel — don't start the paperwork. LGPL-3.0 fails on the goal you picked it for, and separately collides with signed-boot firmware. Two independent problems.

**Verdict**

- ❌ LGPL-3.0 as specified. Not a "tweak the terms" objection — one of the two problems is fatal for your customers.
- No OSI license, LGPL or otherwise, gets you "customers' fixes come back to Thornerly." That is a contract question, not a license question.
- Recommended shape: MPL-2.0 on the open side, commercial license carrying the upstreaming obligation. Reasoning below.

**Problem 1 — copyleft runs forward to the recipient, never backward to the author**

- LGPL obligations trigger on *conveying* a modified work, and they run to whoever receives that copy. That is the hospital, not you.
- Appliance maker patches pulsecore, ships firmware to a hospital → they owe corresponding source to the hospital. You are not a party to that transaction and have no claim under the license.
- No FOSS license contains an upstream-contribution requirement. Not LGPL, not GPL, not AGPL, not MPL. It does not exist in OSI-approved licensing.
- Best case copyleft gives you is indirect: a hospital could demand source, it might eventually surface, you might pick it up. Slow, unenforceable by you, and hospitals have zero incentive to redistribute.
- If you want fixes, the mechanism is a contractual clause with a deliverable and a deadline. See recommendation.

**Problem 2 — LGPLv3 §4(e) requires exactly what your customers' security model forbids**

- LGPLv3 §4(e) pulls in GPLv3 §6's *Installation Information* requirement when the combined work is conveyed in, or with, or specifically for use in, a **User Product**.
- Installation Information = whatever keys, signing tooling, and procedures a recipient needs to actually install a modified pulsecore **and have it run** on that device. Not documentation. Working capability.
- Your customers' entire threat model is that nothing unsigned boots. Complying means handing hospitals signing capability. Not complying means license breach.
- For FDA/CE-cleared firmware this is worse than a security problem. Enabling a hospital to flash an uncertified modified build cuts against design controls and the cleared configuration. Likely a regulatory non-starter independent of the license.
- GPLv3 §6's carve-out (you may refuse support/warranty on modified installs) does not help — the obligation to *enable the install* stands.

**Problem 2b — static linking hurts even if §4(e) never triggers**

- LGPLv3 §4(d)(0) requires giving recipients the Minimal Corresponding Source plus the Corresponding Application Code "in a form suitable for" relinking against a modified pulsecore.
- For static firmware that means shipping hospitals object files, archives, and linker scripts for the *proprietary* firmware. Object code satisfies it, source is not required — but it is still a large reverse-engineering surface handed to every customer of your customer.
- §4(d)(1) (shared-library mechanism) is the escape hatch, and it is unavailable to you: these images are statically linked into signed firmware.
- This obligation is on your customers, not you, and it is the kind of thing that kills a renewal.

**Recommendation**

- **MPL-2.0 for the open side.** File-level copyleft, purpose-built for mixing with proprietary code. Modify an MPL file → publish that file's source to your recipients. No Installation Information clause, no relink obligation, static linking is a non-event.
- **If you insist on staying in the LGPL family, LGPL-2.1, not 3.0.** It predates GPLv3, so no anti-tivoization clause. But note: LGPL-2.1 §6(a) carries the *same* relink/object-code handover burden as 2b above. It fixes the blocker, not the friction. MPL-2.0 fixes both.
- **Put the upstreaming clause in a commercial license, and dual-license.** OSS license is the public default; customers who want different terms buy the commercial one, which contractually obliges them to deliver patches to Thornerly. Standard model — Trolltech/Qt, MySQL-era.
- **Be honest with yourself about the tension:** MPL is easy to comply with, so fewer customers will buy the escape hatch than under LGPL. The coercion drops with the harshness. Don't price the dual-license on compliance pain.
- **Sell the commercial tier on what medical-device customers actually need:** IEC 62304 SOUP documentation, traceability artifacts, indemnification, a named vendor for their submission dossier, LTS branches. That demand is durable. License-escape demand is not.
- **Set up a CLA before the first outside PR, not after.** Dual-licensing requires you to control copyright in the whole tree. A DCO does not grant you relicensing rights. Retrofitting consent from contributors who have moved on is the classic way this model dies.
- **Two more things to settle before signing:** (1) relicensing is one-way — whoever gets the MPL version keeps perpetual rights to it, you can only change terms going forward; (2) check whether any pulsecore algorithms are patented, since both MPL §2.1(b) and LGPLv3 §11 grant patent licenses to every recipient.

**The one blocking open question (only matters if you stay on LGPLv3)**

- ⚠️ Whether each device is a **User Product** under GPLv3 §6. Don't guess this, and don't let me resolve it for you.
- The test is the *product class*, not the buyer: "normally used for personal, family, or household purposes." An ICU monitor or an infusion pump never sold for home use likely sits outside. Home dialysis, home ventilators, personal ECG/glucose monitors, wearables — those classes are User Products even for the hospital-bound units.
- GPLv3 says doubtful cases resolve **in favor of coverage**. The asymmetry is against you.
- Secondary factor: §6 triggers only where possession and use transfer to the recipient in perpetuity or for a fixed term. Lease and managed-service structures shift the analysis, but that is your customers' business model, not something you control.
- Needs a real determination per product line, and it has to cover the roadmap, not just what ships today. One home-use SKU contaminates the answer.

Not legal advice. Before anything is signed, get counsel who has done both open-source licensing and FDA/CE device software — ideally someone with FSF or SFLC background on the license side. This choice is effectively irreversible once customers build on it.