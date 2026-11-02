## Short answer

**No license change makes them stop.** Switching Novaquill's license only affects code you release *after* the switch. The consultancy already has a perpetual, irrevocable right to everything under the current Apache-2.0 releases (Apache-2.0 §2, and it survives license changes upstream — this is exactly why Terraform→OpenTofu and Redis→Valkey exist: the community just forked the last permissively-licensed commit and kept going). If you flip to something restrictive tomorrow, they keep selling support on today's codebase forever, legally, and simply stop pulling your future commits.

The thing that's actually broken here isn't the license — it's the name. **"Novaquill Enterprise" is a trademark problem, not a copyright problem**, and you can act on it today with zero relicensing.

## Why trademark is the real lever

Apache-2.0 §6 explicitly does **not** grant any rights to your trademarks, trade names, or product names — it only covers the code. So even under the license exactly as it stands now, the consultancy calling their fork "**Novaquill** Enterprise" and running a landing page that's confusing two of your own prospects is very likely already outside what Apache-2.0 permits them to do with your name. That's trade name infringement / passing-off / unfair competition territory, and it's the direct cause of the harm you described (prospects can't tell you apart).

Action, in order:

1. **Confirm your mark.** Registered trademark on "Novaquill"? If not, you likely still have common-law rights from 6,000 stars of public use — file the registration now regardless, it strengthens everything downstream.
2. **Send a cease-and-desist** over the name and branding, not the code. Demand they rename ("X, built on Novaquill" is fine under Apache-2.0's attribution language; "Novaquill Enterprise" implying affiliation is not) and add a clear non-affiliation disclaimer.
3. **Document the two prospect confusions** now, in writing — that's your actual damages evidence if this goes further than a C&D.

This is faster than any relicensing effort, needs no contributor consent, and directly targets the confusion, not a hypothetical future fork.

## If you still want to relicense going forward

Worth doing in parallel if you want to blunt this pattern for future versions — but go in clear-eyed about two costs:

**Blocker #1 — contributor consent.** At 6,000 stars you almost certainly have outside contributors who hold copyright on parts of the codebase. Unless Novaquill has a CLA (or DCO language) that already grants you relicensing rights, you cannot unilaterally relicense their contributions — you'd need to track down and get sign-off from every external contributor, or rip out and rewrite their code. Check this first; it's the actual critical path, not the license choice itself.

**Blocker #2 — you exit "open source."** Every license strong enough to matter here (below) is source-available, not OSI-approved open source. Expect some contributor and user attrition, and expect a real possibility someone forks the last Apache-2.0 tag into a community-governed project (this is the standard pattern: MongoDB→SSPL, Elastic→ELv2, HashiCorp→BSL all triggered exactly this).

Ranked by fit for *your specific problem* (a consultancy reselling support/consulting against your code, not reselling it as a hosted service):

- **Business Source License 1.1 (BSL)** — strongest fit. The license itself is a template; you write the "Additional Use Grant," which is free-text and can specifically carve out what's allowed (e.g., "any use except offering paid commercial support, consulting, or a competing distribution of the Software or a derivative to third parties"). This is the only one of the four that can be worded to target "selling support contracts against a fork" directly, because the others were written for a narrower target (hosted SaaS). Converts to Apache-2.0 automatically after a Change Date you set (typically 3–4 years), which is good-faith optics for your community. Used by CockroachDB, Sentry (earlier iterations), MariaDB itself.
- **Elastic License v2 (ELv2)** — simpler, three fixed restrictions (no offering it as a hosted/managed service, no circumventing license keys, no removing license notices). Doesn't cleanly stop "we fork it and sell support," since that's neither hosting-as-a-service nor a license-key issue — weaker fit than BSL for this exact scenario.
- **Functional Source License (FSL)** — Sentry's newer template, restricts "competing use" for 2 years then auto-converts to Apache-2.0/MIT. Simpler than BSL, shorter embargo, but "competing use" as drafted is aimed at competing products, and a consultancy selling *support* rather than a competing product may argue it doesn't apply — same fit gap as ELv2, needs custom wording like BSL to bite.
- **SSPL** — don't use it. It's built for "you're running my database as a cloud service," requires open-sourcing the entire surrounding service stack if triggered, is the most community-hostile of the four, not OSI-recognized, and actively discouraged by most legal counsel now given the AWS/MongoDB fallout. Wrong tool for a sidecar that isn't typically offered as a managed service anyway.

**Recommendation: BSL 1.1 with a custom Additional Use Grant naming commercial support/consulting resale specifically**, paired with the trademark action above. Get the exact Additional Use Grant wording reviewed by an IP attorney — this is the one piece of the license that's doing the real work, and it's untested/custom language, not boilerplate.

## Sequence

1. This week: trademark C&D + non-affiliation demand (fixes the prospect-confusion problem directly).
2. In parallel: audit whether Novaquill has a CLA/DCO granting relicensing rights; if not, that's your real timeline driver, not the license text.
3. If clean: draft BSL 1.1 + Additional Use Grant with counsel, apply to the *next* release only, communicate the Change Date publicly to your community before you ship it.
4. Expect and prepare for a possible community fork of the last Apache-2.0 tag — decide in advance whether you'd rather lead that fork (like Redis did with Valkey, sort of) or let it happen without you.