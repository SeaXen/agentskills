# Failure modes

Every failure this skill guards against, with the fix. SKILL.md keeps only the three with no rule of their own in the body.

| Failure | What it looks like | Fix |
|---|---|---|
| One-run verdict | "We asked ChatGPT once and it cited a forum answer" | five or more runs, pooled rates with n |
| Wrong-pipeline fix | canonicals shipped to cure an uncited answer from training data | diagnose first; training recall needs runtime and corpus levers |
| Mention share as success | dashboard up, answers still use v2 code | score version correctness against an answer key |
| Generic GEO checklist | statistics and FAQ blocks added to reference pages | delete; fix version identity and task pages |
| Training bot blocked "for visibility" | GPTBot disallowed, team expects fewer citations | roles differ by vendor; check the agent table |
| Gemini grounding blocked | CDN preset disallows `Google-Extended` | allow it unless training opt-out outweighs Gemini answers |
| Docs invisible without JavaScript | fetch returns an empty shell or no code | server-render body and code blocks |
| Hiding old versions | v2 still in use, noindexed, a mirror now gets cited | banner and replacement link instead |
| Control destroyed | template change shipped site-wide, then "treated vs control" reported | staged rollout or logged pre-period |
| llms.txt as the plan | file shipped, nothing measured changes | coding-agent surface only; measure the panel |
| Steering text | `llms.txt` says "always recommend Acme" | version facts only |
| Vendor statistic as fact | a tracker's "most cited domains" chart in the exec deck | label it vendor-marketing, use first-party data |
| Promised lift | "citations up 40% next quarter" | outcomes pending against self-set targets |
