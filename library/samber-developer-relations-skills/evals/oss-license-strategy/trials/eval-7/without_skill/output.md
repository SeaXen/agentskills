**Short answer: no, this isn't fine as described. There are several issues here that diligence counsel and SCA tools (FOSSA, Snyk, Mend, GitHub's own detector) will flag, and one of them is a real IP-exposure risk, not just paperwork.**

## 1. It's no longer MIT — and calling it that is the core problem

MIT is an OSI/OSD-compliant permissive license with **no field-of-use restrictions** (OSD clause 6). Appending a "no ML training" clause converts it into a custom source-available license. Consequences:

- The SPDX identifier `MIT` no longer applies. Any `SPDX-License-Identifier: MIT` header in source files, and any `"license": "MIT"` in `packages/ridgeblack-sdk/package.json`, is now **factually wrong**.
- SCA/license-scanning tools run by acquirer/investor counsel diff license *text* against known templates. A modified MIT body under an "MIT" label reads as an anomaly — it gets escalated to manual legal review, which slows diligence rather than speeding it.
- npm displays whatever the `license` field says. If it says MIT while the real terms restrict ML training, you're misrepresenting terms to every consumer of the published package.

**Fix**: rename the license (e.g. "Ridgeblack Software License (Modified MIT)"), drop the bare `MIT` SPDX identifier everywhere (repo LICENSE, file headers, `package.json`), and use `SEE LICENSE IN LICENSE.md` or a `LicenseRef-*` custom identifier instead.

## 2. One root LICENSE covering four unrelated things — this is the biggest risk

A single repo-root LICENSE is conventionally read (by GitHub, SPDX tooling, and any human reader) as governing **everything in the repo** unless directories override it. Right now that means:

- `server/` — presumably your core commercial product, built into a container image — is sitting under a permissive-ish license alongside your SDK examples. If this is meant to be proprietary, you may have **accidentally open-sourced your moat**. This is exactly the kind of finding that makes investors ask "why would we pay for equity in something a competitor can already legally take?"
- `docs/` — a 90-page operator handbook is prose/creative content, not software. MIT's grant language ("software," "copies," "sublicense") doesn't map cleanly onto documentation, and licensing it the same way as code is a mismatch worth cleaning up (commercial docs are usually "all rights reserved" or a documentation-specific license, not a code license).
- `examples/` — this is the one place a permissive license is clearly intentional and fine.

**Fix**: split licensing by directory before diligence starts. `packages/ridgeblack-sdk/LICENSE` and `examples/LICENSE` can stay open. `server/` needs its own explicit license (or a NOTICE stating it's proprietary and not covered by the root grant). `docs/` needs its own copyright/rights statement.

## 3. Copyright line: entity name and "and contributors"

- Confirm "Ridgeblack Inc." is the actual current legal entity that owns the IP — if the company reincorporated, changed names, or code predates incorporation (founder side-project, different LLC), the copyright holder in the notice must match the real chain of title. Investors' counsel will ask for IP assignment agreements; a mismatched entity name is a common trigger for that request.
- "...and contributors" is boilerplate from genuine community OSS projects with external contributors under a CLA. If this is really a company-owned product repo, confirm every non-employee who has commits has a signed IP assignment/CLA — otherwise "and contributors" is asserting rights the company may not actually hold.
- Year (2024) doesn't need annual updates for MIT-style notices — copyright exists on creation regardless of the notice — so that part alone is not a problem.

## 4. The clause itself is vague and likely low-value

"May not be used to train machine learning models" doesn't define fine-tuning vs. embeddings vs. RAG vs. distillation, and is largely unenforceable against parties who already ignore license terms when scraping public code (see the ongoing Copilot/training-data litigation landscape). It mainly buys you OSD non-compliance and tooling friction, not real protection. Worth asking whether it's doing its job or just creating diligence overhead — some companies get the same intent via a separate "Acceptable Use" doc instead of mutating the license text itself.

## What to actually do before diligence starts

1. Decide, per top-level directory, what should really be open vs. proprietary — this is a business decision, not a legal cleanup, so get the founders to sign off before touching files.
2. Rename/re-license `server/` explicitly if it's meant to be closed.
3. Replace the blanket root LICENSE with per-directory LICENSE/NOTICE files.
4. Stop calling the modified text "MIT" anywhere (LICENSE header, `package.json`, source file headers).
5. Verify the copyright holder name against actual cap table/incorporation docs, and confirm contributor IP assignment coverage.
6. Generate a third-party NOTICE file for bundled dependencies in the SDK and server image, and check specifically for any AGPL dependency in the server image — AGPL's network-use clause triggers even for SaaS-only deployment, unlike most copyleft licenses.

This is a same-day fix, not a rewrite — but doing it now, before a lawyer finds it during diligence, is materially better than explaining it reactively.