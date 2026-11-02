Here's the restructured page — two pieces, both ready to paste. The core fix: your one-liner declares *which* license without stating the one clause that actually matters to a deploying team — AGPL's network-use trigger. Nobody reads a license file before deploying; they read it when a business decision (selling access, going multi-tenant) collides with it. Since the trigger condition is never named, that collision happens three weeks in, as a support request instead of a pre-deploy decision. Name the trigger condition explicitly, in plain English, in two places: where people actually look (top of README, before they install) and where convention expects it (bottom `## License`).

## 1. Add a callout right under your badges/tagline, before Installation

```markdown
> **Licensing:** Gridwarden is AGPL-3.0 — free to self-host and modify. If you plan to offer Gridwarden, modified or not, as a hosted service to people outside your organization, AGPL requires you to publish your source. Need to avoid that? See [Licensing](#license) or email licensing@fenwick-analytics.<tld>.
```

## 2. Replace the bottom `## License` section

```markdown
## License

Gridwarden is licensed under [AGPL-3.0](LICENSE).

**What this means in practice:**

- **Self-hosting for your own use** (internal tooling, powering your own product for your own end users) — no obligations beyond attribution. Modify freely, keep changes private.
- **Offering Gridwarden — as-is or modified — as a hosted/managed service to third parties** — AGPL's network-use clause requires you to publish the complete source of your running version, including modifications, under AGPL-3.0.
- **Want to offer it as a hosted service without open-sourcing your changes?** — We sell a commercial license that waives the source-disclosure requirement. Email **licensing@fenwick-analytics.\<tld>** with your use case.

Full legal text: [LICENSE](LICENSE). Common scenarios: [Licensing FAQ](LICENSING.md).
```

## 3. Add `LICENSING.md`, linked from both spots above, for the long tail of questions

```markdown
# Licensing FAQ

Gridwarden is AGPL-3.0. This explains what that means for common deployment
scenarios. Not legal advice — email licensing@fenwick-analytics.<tld> if your
situation isn't covered here.

## I run Gridwarden inside my own company; nobody outside my org touches it.
No obligations. Internal use doesn't trigger AGPL's network-use clause.

## My customers hit Gridwarden's API/UI as part of my product.
This is the case AGPL was written for. Because outside users interact with
the software over a network, AGPL requires you to publish the complete
source of your running version — including modifications — under AGPL-3.0.

## I want to offer Gridwarden to customers without publishing my modifications.
That's the commercial license. It waives the source-disclosure requirement.
Email **licensing@fenwick-analytics.<tld>** with your expected scale and
whether you're modifying the code, and we'll quote you.

## I'm just evaluating it before deciding.
Evaluation and internal use are unrestricted. This only matters once you
serve Gridwarden to people outside your organization.

## Does contributing code back count instead of paying?
Ask us — we're generally open to it for meaningful contributions.
```

## 4. Optional: second badge next to your existing ones

```markdown
[![License: AGPL-3.0](https://img.shields.io/badge/license-AGPL--3.0-blue.svg)](LICENSE) [![Commercial license available](https://img.shields.io/badge/commercial%20license-available-green.svg)](LICENSING.md)
```

Fill in `licensing@fenwick-analytics.<tld>` with your real address before shipping — I left it as a placeholder rather than guess your domain.